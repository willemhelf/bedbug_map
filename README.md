# NYC Bedbug Complaint Heat Mapping
#### by [Nene Villalobos](https://github.com/avilla22) and [Willem Helf](https://github.com/willemhelf)
#### Final project for Info 628: Data Librarianship and Management at Pratt Institute School of Information
This Github repository contains code that can be used to generate heat maps of New York City 311 bedbug complaints over the course of the years 2018-2024, the data for which is collected from the [NYC Open Data Bedbug Reporting](https://data.cityofnewyork.us/Housing-Development/Bedbug-Reporting/wz6d-d3jb/about_data) dataset via the [SODA API](https://dev.socrata.com/foundry/data.cityofnewyork.us/wz6d-d3jb). 
### File structure
All code is written using Python.

Jupyter Notebook files, which can be found in the `jupyter_notebooks` directory, can be run either directly in your code editor or by running the `jupyter notebook` command in the terminal followed by the name of the file you wish to run, which will open it in your browser. Be sure to select "trust notebook" in the "file" dropdown menu before running. Heatmap images and dataframes will be visualized in the Jupyter Notebook file.

Python files, found in the `python` directory, can be run by entering `python`  followed by the name of the file you'd like to run into the terminal. Each map will generate an interactive HTML file of the selected heatmap, except for `all_years_dataframe.py`, which will print the full dataframe of API results into the console.
### Methodology

The SODA API is called utilizing the Socrata client and the results are turned into a dataframe using [pandas](https://pandas.pydata.org/). 

To create a map of an individual year's worth of data, the dataframe is sorted by the `filing_date` column (the date of a complaint's filing) and filters out any date not in the selected year. For a map that is a coalescence of all years, this step is skipped. [Geopandas](https://geopandas.org/en/stable/) is then used to create a heatmap layer via the `latitude` and `longitude` columns in each row of the resulting data. 

A base map of New York City is generated via inputting the city's latitude and longitude using [Folium](https://python-visualization.github.io/folium/latest/). The previously-generated heatmap is then layered over the base map and then either rendered in the file (Jupyter Notebook) or saved as an interactive HTML map (Python).

### What next?

Code to generate solely the API results in dataframe format were included in this repository to illustrate the shape of the data we worked with to create these maps. Given more time, we hope to use other data shown in these dataframes – zip code, borough, number of units, et al – to explore further data correlation. We view these maps not as the final results of our research but as a springboard for more.

We also hope to explore rendering data further in the browser. An example of a heat map covering all years may be viewed [here](https://www.willemhelf.com/heat_map).
