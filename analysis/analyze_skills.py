import pandas as pd

df = pd.read_csv("data/cleaned/skill_analysis.csv")

total_jobs = df["job_id"].nunique()

print("Total unique jobs:", total_jobs)

# Count each skill by unique job posting
skill_demand = (
    df.groupby("skill")["job_id"]
    .nunique()
    .reset_index(name="job_count")
)

skill_demand["demand_percent"] = (
    skill_demand["job_count"] / total_jobs * 100
)

skill_demand = skill_demand.sort_values(
    "job_count",
    ascending=False
)

print("\n----- TOP SKILLS BY JOB DEMAND -----")
print(
    skill_demand.head(15).to_string(index=False)
)

# Average salary for skills appearing in at least 2 jobs
salary_by_skill = (
    df.groupby("skill")
    .agg(
        job_count=("job_id", "nunique"),
        average_salary=("salary_avg", "mean")
    )
    .reset_index()
)

salary_by_skill = salary_by_skill[
    salary_by_skill["job_count"] >= 2
]

salary_by_skill = salary_by_skill.sort_values(
    "average_salary",
    ascending=False
)

print("\n----- AVERAGE SALARY BY SKILL -----")
print(
    salary_by_skill.head(15).to_string(index=False)
)

# Experience distribution
experience = (
    df.drop_duplicates("job_id")
    ["experience_years"]
    .value_counts()
    .sort_index()
)

print("\n----- EXPERIENCE DISTRIBUTION -----")
print(experience)

# Save analysis results
skill_demand.to_csv(
    "data/cleaned/skill_demand.csv",
    index=False
)

salary_by_skill.to_csv(
    "data/cleaned/salary_by_skill.csv",
    index=False
)

print("\nAnalysis files created successfully!")