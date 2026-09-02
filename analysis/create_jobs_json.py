import pandas as pd

df = pd.read_csv("data/cleaned/jobs_analysis.csv")

df.to_json(
    "data/cleaned/jobs.json",
    orient="records",
    force_ascii=False,
    indent=2
)

print("jobs.json created successfully!")