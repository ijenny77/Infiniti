import pandas as pd
import os

# print("Files in data/ :", os.listdir("data/"))
#
# df_a = pd.read_csv("data/site_a_readings.csv")
# print("First 5 rows:")
# print(df_a.head())
#
# print(df_a.dtypes)

df_a = pd.read_csv("data/site_a_readings.csv", parse_dates=["timestamp"], index_col = "timestamp")
print(df_a.head())
print("Data types:")
print(df_a.dtypes)
print("Index types:")
print(df_a.index)