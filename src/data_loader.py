import pandas as pd

#This file contains functions related to loading, cleaning, and preprocessing data.
#Since stock market prediction relies on data, you need a clean way to handle it.

def load_data(file_path):
    """Loads stock market data from a CSV file."""
    print(f"Loading data from {file_path}...")
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    """Cleans and preprocesses the data."""
    print("Preprocessing data...")
    # Example: Fill missing values
    data = data.fillna(method='ffill')
    return data
