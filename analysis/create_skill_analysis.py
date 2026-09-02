import pandas as pd

# Load job-level analysis data
jobs = pd.read_csv("data/cleaned/jobs_analysis.csv")

# Load skill-level data
skills = pd.read_csv("data/cleaned/job_skills.csv")

# Select the job information needed for analysis
job_data = jobs[
    [
        "job_id",
        "company_name",
        "locations",
        "salary_min",
        "salary_max",
        "salary_avg",
        "experience_years"
    ]
]

# Join using the unique job ID
skill_analysis = skills.merge(
    job_data,
    on="job_id",
    how="left",
    suffixes=("_skill", "_job")
)

# Remove duplicate company/location/salary columns created by the merge
skill_analysis = skill_analysis[
    [
        "job_id",
        "company_name_skill",
        "locations_skill",
        "salary_min_skill",
        "salary_max_skill",
        "salary_avg_skill",
        "experience_years_skill",
        "skill"
    ]
]

# Rename columns
skill_analysis = skill_analysis.rename(
    columns={
        "company_name_skill": "company_name",
        "locations_skill": "locations",
        "salary_min_skill": "salary_min",
        "salary_max_skill": "salary_max",
        "salary_avg_skill": "salary_avg",
        "experience_years_skill": "experience_years"
    }
)

# Save final skill analysis dataset
skill_analysis.to_csv(
    "data/cleaned/skill_analysis.csv",
    index=False
)

print("Skill analysis dataset created!")

print("\n----- DATASET SHAPE -----")
print(skill_analysis.shape)

print("\n----- SAMPLE -----")
print(
    skill_analysis[
        [
            "job_id",
            "company_name",
            "skill",
            "salary_avg",
            "experience_years"
        ]
    ].head(15).to_string(index=False)
)

print("\n----- TOP SKILLS -----")
print(
    skill_analysis["skill"]
    .value_counts()
    .head(15)
)

print("\n----- AVERAGE SALARY BY SKILL -----")
print(
    skill_analysis
    .groupby("skill")["salary_avg"]
    .agg(["count", "mean"])
    .sort_values("mean", ascending=False)
    .head(15)
)