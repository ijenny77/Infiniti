import pandas as pd
import numpy as np
import json
from scipy.stats import zscore

#Load data
df = pd.read_csv("data/sensor_logs_zone.csv", parse_dates=['timestamp'], index_col=['timestamp'])
print(f"Loaded {len(df)} sensor logs with {df['device_id'].nunique()} devices.")

# Sample working functions

def compute_device_stats(df, device_id):
    # Return dict of stats for a single device
    df = df.groupby("device_id").describe()
    device_series = df.to_dict(orient='records')
    return device_series

def get_anomalous_readings(device_series, threshold = 2):
    # Use z-score to identify outliers
    device_series['moisture_z'] = zscore(device_series['moisture'])
    outliers = device_series[device_series['moisture_z'] < threshold]
    df = device_series.drop(outliers.index)
    return outliers, device_series

def analyze_by_zone(df, min_risk_percent = 30):
    # Use boolean indexing to find high-risk zones
    df['min_risk'] = df[df['moisture'] < min_risk_percent]
    df['high_risk'] = df[df['moisture'] > min_risk_percent]

    return df
