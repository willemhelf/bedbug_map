import pandas as pd
from sodapy import Socrata
import matplotlib.pyplot as plt
import numpy as np

client = Socrata("data.cityofnewyork.us", None)

results = client.get("wz6d-d3jb", limit=2000)

results_df = pd.DataFrame.from_records(results)