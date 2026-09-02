import pandas as pd
import sqlite3

# Load cleaned datasets
jobs = pd.read_csv("data/cleaned/jobs_analysis.csv")
skills = pd.read_csv("data/cleaned/skill_analysis.csv")

# Create SQLite database
conn = sqlite3.connect("data/job_market.db")

# Store datasets as SQL tables
jobs.to_sql(
    "jobs",
    conn,
    if_exists="replace",
    index=False
)

skills.to_sql(
    "job_skills",
    conn,
    if_exists="replace",
    index=False
)

print("SQLite database created successfully!")

# Example SQL query 1
query1 = """
SELECT
    skill,
    COUNT(DISTINCT job_id) AS job_count
FROM job_skills
GROUP BY skill
ORDER BY job_count DESC
LIMIT 10;
"""

print("\n----- TOP 10 SKILLS USING SQL -----")

result1 = pd.read_sql_query(query1, conn)
print(result1.to_string(index=False))


# Example SQL query 2
query2 = """
SELECT
    experience_years,
    COUNT(*) AS job_count
FROM jobs
GROUP BY experience_years
ORDER BY experience_years;
"""

print("\n----- JOBS BY EXPERIENCE USING SQL -----")

result2 = pd.read_sql_query(query2, conn)
print(result2.to_string(index=False))


conn.close()

print("\nSQL analysis completed successfully!")