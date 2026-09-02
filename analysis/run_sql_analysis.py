import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("data/job_market.db")

print("===== JOB MARKET SQL ANALYSIS =====")


# 1. Top 10 most demanded skills
query1 = """
SELECT
    skill,
    COUNT(DISTINCT job_id) AS job_count
FROM job_skills
GROUP BY skill
ORDER BY job_count DESC
LIMIT 10;
"""

print("\n----- TOP 10 DEMANDED SKILLS -----")
print(
    pd.read_sql_query(query1, conn).to_string(index=False)
)


# 2. Skills with higher average salary
query2 = """
SELECT
    skill,
    COUNT(DISTINCT job_id) AS job_count,
    ROUND(AVG(salary_avg), 0) AS average_salary
FROM job_skills
GROUP BY skill
HAVING COUNT(DISTINCT job_id) >= 2
ORDER BY average_salary DESC;
"""

print("\n----- SKILLS AND AVERAGE SALARY -----")
print(
    pd.read_sql_query(query2, conn).head(10).to_string(index=False)
)


# 3. Salary by experience
query3 = """
SELECT
    experience_years,
    COUNT(*) AS job_count,
    ROUND(AVG(salary_avg), 0) AS average_salary
FROM jobs
GROUP BY experience_years
ORDER BY experience_years;
"""

print("\n----- SALARY BY EXPERIENCE -----")
print(
    pd.read_sql_query(query3, conn).to_string(index=False)
)


# 4. Jobs by location
query4 = """
SELECT
    locations,
    COUNT(*) AS job_count
FROM jobs
GROUP BY locations
ORDER BY job_count DESC
LIMIT 10;
"""

print("\n----- TOP JOB LOCATIONS -----")
print(
    pd.read_sql_query(query4, conn).to_string(index=False)
)


conn.close()

print("\nSQL analysis completed successfully!")