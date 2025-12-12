import pandas as pd
import geopandas as gpd
from sodapy import Socrata
import folium
from folium import plugins

#call NYC Open Data API and return results as dataframe
client = Socrata("data.cityofnewyork.us", None)
results = client.get("wz6d-d3jb", limit=50000) #returns 1000 without limit
results_df = pd.DataFrame.from_records(results)

## filter dataframe for bug reports by year
sorted = results_df.sort_values(by='filing_date').dropna()
bugs_2022 = sorted[sorted["filing_date"].str.contains('2022')]

#create and generate heatmap with 2018 dataframe
df_2022 = gpd.GeoDataFrame(
    bugs_2022, geometry=gpd.points_from_xy(bugs_2022["longitude"], bugs_2022["latitude"], crs=4326)
)
map_center = [40.7128, -74.0060]
m = folium.Map(location=map_center, zoom_start=13)
map_2022 = [[point.xy[1][0], point.xy[0][0]] for point in df_2022.geometry]
plugins.HeatMap(map_2022).add_to(m)
m.save("2022_heat_map.html")