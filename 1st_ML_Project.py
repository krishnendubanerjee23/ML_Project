#importing required packages
import pandas as pd
import pandas_profiling
import numpy as np

# Takes the file's folder
filepath = r"C:\Users\Krishnendu\Desktop\Dataset\Dataset\data7\train.csv"

#importing the data
df = pd.read_csv(filepath)

#descriptive statistics
profile = pandas_profiling.ProfileReport(df, explorative=True)
profile.to_file("output.html")

