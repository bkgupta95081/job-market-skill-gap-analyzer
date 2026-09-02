import pandas as pd

# Load raw dataset
df = pd.read_csv("data/raw/Job_dataset.csv")

print("Original rows:", len(df))

# Remove exact duplicate records
df = df.drop_duplicates().copy()

print("Rows after removing duplicates:", len(df))

# Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Remove unnecessary spaces from text columns
text_columns = ["company_name", "locations", "salary", "experience", "skills"]

for column in text_columns:
    df[column] = df[column].astype(str).str.strip()

# Save cleaned dataset
df.to_csv("data/cleaned/jobs_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
print("Columns:", list(df.columns))