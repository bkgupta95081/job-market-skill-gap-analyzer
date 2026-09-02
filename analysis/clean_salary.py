import pandas as pd
import re

# Load the cleaned job dataset
df = pd.read_csv("data/cleaned/jobs_cleaned.csv")


def extract_salary(salary_text):
    # Extract all numbers from salary text
    numbers = re.findall(r"\d[\d,]*", str(salary_text))

    numbers = [int(n.replace(",", "")) for n in numbers]

    if len(numbers) == 1:
        return numbers[0], numbers[0]

    elif len(numbers) >= 2:
        return numbers[0], numbers[1]

    return None, None


# Give every unique job posting a unique ID
df.insert(0, "job_id", range(1, len(df) + 1))

# Extract minimum and maximum salary
df[["salary_min", "salary_max"]] = df["salary"].apply(
    lambda x: pd.Series(extract_salary(x))
)

# Calculate average salary
df["salary_avg"] = (
    df["salary_min"] + df["salary_max"]
) / 2

# Convert experience into numeric years
df["experience_years"] = (
    df["experience"]
    .str.extract(r"(\d+)")
    .astype(int)
)

# Save the analysis-ready dataset
df.to_csv(
    "data/cleaned/jobs_analysis.csv",
    index=False
)

print("Salary cleaning completed!")

print("\n----- SALARY SAMPLE -----")
print(
    df[
        [
            "job_id",
            "salary",
            "salary_min",
            "salary_max",
            "salary_avg"
        ]
    ].head(10).to_string(index=False)
)

print("\n----- SALARY SUMMARY -----")
print(df["salary_avg"].describe())

print("\n----- EXPERIENCE SUMMARY -----")
print(
    df["experience_years"]
    .value_counts()
    .sort_index()
)