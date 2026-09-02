import pandas as pd

df = pd.read_csv("data/cleaned/job_skills.csv")

skills = df["skill"].value_counts()

print("----- SKILLS WITH COUNTS -----")
print(skills.to_string())

print("\n----- TOTAL UNIQUE SKILLS -----")
print("Unique skills:", df["skill"].nunique())