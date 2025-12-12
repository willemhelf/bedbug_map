import pandas as pd
from geodatasets import get_path
import geopandas as gpd
import geoplot as gplt
from sodapy import Socrata
import matplotlib.pyplot as plt
import numpy as np
import folium
from folium import plugins

client = Socrata("data.cityofnewyork.us", None)
results = client.get("wz6d-d3jb", limit=2000) 
results_df = pd.DataFrame.from_records(results)

geo_df = gpd.GeoDataFrame(
    results_df, geometry=gpd.points_from_xy(results_df["longitude"], results_df["latitude"], crs=4326)
)
map_center = [40.7128, -74.0060]

m = folium.Map(location=map_center, zoom_start=13)
heat_data = [[point.xy[1][0], point.xy[0][0]] for point in geo_df.geometry]
heat_data
plugins.HeatMap(heat_data).add_to(m)

m.save("heat_map_all_years.html")