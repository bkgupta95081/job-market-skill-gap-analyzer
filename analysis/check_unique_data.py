import pandas as pd

df = pd.read_csv("data/raw/Job_dataset.csv")

# Remove exact duplicate rows
df_unique = df.drop_duplicates()

print("Original rows:", len(df))
print("Rows after removing duplicates:", len(df_unique))

print("\n----- EXPERIENCE VALUES -----")
print(df_unique["Experience"].value_counts())

print("\n----- SALARY VALUES -----")
print(df_unique["Salary"].value_counts())

print("\n----- SAMPLE UNIQUE RECORDS -----")
print(df_unique.to_string(index=False))