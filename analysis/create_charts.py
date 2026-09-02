import pandas as pd
import matplotlib.pyplot as plt

# Load analysis results
skills = pd.read_csv("data/cleaned/skill_demand.csv")
salary = pd.read_csv("data/cleaned/salary_by_skill.csv")


# -----------------------------
# Chart 1: Top 10 Skills
# -----------------------------

top_skills = skills.head(10).sort_values("job_count")

plt.figure(figsize=(10, 6))

plt.barh(
    top_skills["skill"],
    top_skills["job_count"]
)

plt.xlabel("Number of Job Postings")
plt.ylabel("Skill")
plt.title("Top 10 Skills by Job Demand")

plt.tight_layout()

plt.savefig(
    "analysis/top_skills.png",
    dpi=150
)

plt.close()


# -----------------------------
# Chart 2: Average Salary by Skill
# -----------------------------

top_salary = salary.head(10).sort_values("average_salary")

plt.figure(figsize=(10, 6))

plt.barh(
    top_salary["skill"],
    top_salary["average_salary"]
)

plt.xlabel("Average Salary (INR)")
plt.ylabel("Skill")
plt.title("Average Salary by Skill")

plt.tight_layout()

plt.savefig(
    "analysis/salary_by_skill.png",
    dpi=150
)

plt.close()

print("Charts created successfully!")
print("Created:")
print("1. analysis/top_skills.png")
print("2. analysis/salary_by_skill.png")