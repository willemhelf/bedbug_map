import pandas as pd
import geodatasets
import geopandas as gpd
from sodapy import Socrata
import matplotlib.pyplot as plt
import numpy as np
import folium
from folium import plugins

#call NYC Open Data API and return results as dataframe

client = Socrata("data.cityofnewyork.us", None)
results = client.get("wz6d-d3jb", limit=50000) #returns 1000 without limit
results_df = pd.DataFrame.from_records(results)

## filter dataframe for bug reports by year

sorted = results_df.sort_values(by='filing_date').dropna()
bugs_2018 = sorted[sorted["filing_date"].str.contains('2018')]
bugs_2019 = sorted[sorted["filing_date"].str.contains('2019')]
bugs_2020 = sorted[sorted["filing_date"].str.contains('2020')]
bugs_2021 = sorted[sorted["filing_date"].str.contains('2021')]
bugs_2022 = sorted[sorted["filing_date"].str.contains('2022')]
bugs_2023 = sorted[sorted["filing_date"].str.contains('2023')]
bugs_2024 = sorted[sorted["filing_date"].str.contains('2024')]

#sample for 2018 – create and generate heatmap with 2018 dataframe

df_2018 = gpd.GeoDataFrame(
    bugs_2018, geometry=gpd.points_from_xy(bugs_2018["longitude"], bugs_2018["latitude"], crs=4326)
)
map_center = [40.7128, -74.0060]
m = folium.Map(location=map_center, zoom_start=13)
map_2018 = [[point.xy[1][0], point.xy[0][0]] for point in df_2018.geometry]
plugins.HeatMap(map_2018).add_to(m)
m.save("2018_heat_map.html")