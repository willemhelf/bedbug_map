import pandas as pd
import geodatasets
import geopandas
from sodapy import Socrata
import matplotlib.pyplot as plt
import numpy as np


## get full dataframe from API. Returns 2000 items, 1000 is default

client = Socrata("data.cityofnewyork.us", None)
results = client.get("wz6d-d3jb", limit=2000) 
results_df = pd.DataFrame.from_records(results)


# generate individual dataframe for each borough

queens = results_df[results_df['borough'] == "QUEENS"]
bronx = results_df[results_df['borough'] == "BRONX"]
brooklyn = results_df[results_df['borough'] == "BROOKLYN"]
manhattan = results_df[results_df['borough'] == "MANHATTAN"]
staten_island = results_df[results_df['borough'] == "STATEN ISLAND"]


#generate map for each borough using above dataframe. Use with map_output function below

nyc_map = geopandas.GeoDataFrame(
    results_df, geometry=geopandas.points_from_xy(results_df["longitude"], results_df["latitude"], crs=4326)
)

queens_map = geopandas.GeoDataFrame(
    queens, geometry=geopandas.points_from_xy(queens["longitude"], queens["latitude"], crs=4326)
)

brooklyn_map = geopandas.GeoDataFrame(
    brooklyn, geometry=geopandas.points_from_xy(brooklyn["longitude"], brooklyn["latitude"], crs=4326)
)

manhattan_map = geopandas.GeoDataFrame(
    manhattan, geometry=geopandas.points_from_xy(manhattan["longitude"], manhattan["latitude"], crs=4326)
)

bronx_map = geopandas.GeoDataFrame(
    bronx, geometry=geopandas.points_from_xy(bronx["longitude"], bronx["latitude"], crs=4326)
)

staten_island_map = geopandas.GeoDataFrame(
    staten_island, geometry=geopandas.points_from_xy(staten_island["longitude"], staten_island["latitude"], crs=4326)
)


# function to output html file with interactive map of lat/long points – call on any borough map above

def map_output(borough):
    m = borough.explore()
    output_path = r'bedbugs\base_map.html'
    m.save(output_path)

map_output(bronx_map)