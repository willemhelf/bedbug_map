import pandas as pd
from geodatasets import get_path
import geopandas as gpd
import geoplot as gplt
from sodapy import Socrata
import matplotlib.pyplot as plt
import numpy as np


# get full dataframe from API. Returns 2000 items, 1000 is default
# change number of results by editing limit variable on line 15
# more results will result in higher processing time
client = Socrata("data.cityofnewyork.us", None)
results = client.get("wz6d-d3jb", limit=2000) 
results_df = pd.DataFrame.from_records(results)
nyc = gpd.read_file(get_path("geoda nyc"))

# create map using latitude and longitude colums of each row of dadta
nyc_map = gpd.GeoDataFrame(
    results_df, geometry=gpd.points_from_xy(results_df["longitude"], results_df["latitude"], crs=4326)
)


# function to output html file with interactive map of lat/long points
def map_output(borough):
    m = borough.explore()
    output_path = r'bedbugs\base_map.html'
    m.save(output_path)

map_output(nyc_map)