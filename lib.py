# Build lib.py to adjust any system

import polars as pl
import pandas as pd


# Load the dataset, which is .csv.
def load_data(dataset):
    """
    Load data from a file and return a DataFrame.
    """
    data = pd.read_csv(dataset)
    return data
