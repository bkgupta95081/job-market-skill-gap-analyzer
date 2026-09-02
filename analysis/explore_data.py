import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/Job_dataset.csv")

# Basic information
print("----- DATASET INFO -----")
print(df.info())

# Missing values
print("\n----- MISSING VALUES -----")
print(df.isnull().sum())

# Duplicate rows
print("\n----- DUPLICATES -----")
print("Duplicate rows:", df.duplicated().sum())

# Number of unique values
print("\n----- UNIQUE VALUES -----")
print(df.nunique())

# First 5 rows
print("\n----- FIRST 5 ROWS -----")
print(df.head())