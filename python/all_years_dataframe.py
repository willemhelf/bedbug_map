import pandas as pd
from sodapy import Socrata

# define NYC Open Data as our API client
client = Socrata("data.cityofnewyork.us", None)
# make a request to the API for 50,000 items
results = client.get("wz6d-d3jb", limit=50000)
# turn our results into a Pandas dataframe
results_df = pd.DataFrame.from_records(results)
# display our results in the console
print(results_df)