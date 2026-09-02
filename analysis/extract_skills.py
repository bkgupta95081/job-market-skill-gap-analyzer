import pandas as pd

# Load analysis-ready job data
df = pd.read_csv("data/cleaned/jobs_analysis.csv")

# Skills that we can reliably identify from the dataset
known_skills = [
    "MS-Office",
    "MS-Excel",
    "MS-PowerPoint",
    "MS-Word",
    "Data entry",
    "Data Analytics",
    "Data Analysis",
    "Power BI",
    "MS SQL Server",
    "SQL",
    "HTML",
    "Linux",
    "GIS",
    "ArcGIS",
    "SSMS",
    "Accounting",
    "Tally",
    "Financial planning",
    "Financial Reporting",
    "Digital Marketing",
    "Market research",
    "Marketing Strategies",
    "Sales Management",
    "Sales Support",
    "Sales Strategy",
    "Sales",
    "Field Sales",
    "Inside Sales",
    "Business Development",
    "Lead Generation",
    "Cold Calling",
    "Customer Support",
    "Customer Acquisition",
    "Client Relationship Management (CRM)",
    "Client Relationship",
    "Effective Communication",
    "English Proficiency (Spoken)",
    "English Proficiency (Written)",
    "Hindi Proficiency (Spoken)",
    "Presentation skills",
    "Problem Solving",
    "Time Management",
    "Coordination",
    "Adaptability",
    "Conflict Management",
    "Leadership",
    "Team Management",
    "E-commerce",
    "Mentorship",
    "Public Speaking",
    "Client Interaction",
    "Negotiation",
    "Negotiations",
    "Recruitment",
    "Resume screening",
    "Interview Coordination",
    "Teaching",
    "Online Teaching",
    "Content Writing",
    "Content Management",
    "Creative Writing",
    "Proofreading",
    "Research and Analytics",
    "Search Engine Optimization (SEO)",
    "SEO",
    "Canva",
    "Figma",
    "Adobe Photoshop",
    "Adobe Illustrator",
    "Adobe InDesign",
    "Branding",
    "UI & UX Design",
    "Graphic Design",
    "Interior design",
    "Digital Illustration",
    "Motion Graphics",
    "Video Editing",
    "Medical Terminology",
    "Investment Banking",
    "Network protocols",
    "Legal Research",
    "Company Law",
    "Legal Drafting",
    "Statutory compliances",
    "Legal Writing",
    "Contract Management",
    "Planning",
    "Storyboarding",
    "Design Thinking"
]

# Check longer skill names first.
# This prevents shorter skills from being matched inside longer ones.
known_skills = sorted(
    known_skills,
    key=len,
    reverse=True
)

skill_rows = []

for _, row in df.iterrows():

    skill_text = str(row["skills"]).lower()

    matched_skills = []

    for skill in known_skills:

        if skill.lower() in skill_text:

            matched_skills.append(skill)

    # Remove nested/overlapping matches.
    # Example:
    # "MS SQL Server" should not also create "SQL".
    final_skills = []

    for skill in matched_skills:

        is_part_of_larger_skill = False

        for other_skill in matched_skills:

            if (
                skill != other_skill
                and skill.lower() in other_skill.lower()
                and len(other_skill) > len(skill)
            ):
                is_part_of_larger_skill = True
                break

        if not is_part_of_larger_skill:
            final_skills.append(skill)

    for skill in final_skills:

        skill_rows.append({
            "job_id": row["job_id"],
            "company_name": row["company_name"],
            "locations": row["locations"],
            "salary_min": row["salary_min"],
            "salary_max": row["salary_max"],
            "salary_avg": row["salary_avg"],
            "experience_years": row["experience_years"],
            "skill": skill
        })


# Create skill-level dataset
skills_df = pd.DataFrame(skill_rows)

# Standardize similar skill names
skill_mapping = {
    "Negotiations": "Negotiation",
    "Search Engine Optimization (SEO)": "SEO"
}

skills_df["skill"] = skills_df["skill"].replace(skill_mapping)

# Remove duplicates created by standardization
skills_df = skills_df.drop_duplicates()

# Save result
skills_df.to_csv(
    "data/cleaned/job_skills.csv",
    index=False
)

print("Skill extraction completed!")
print("Number of skill records:", len(skills_df))

print("\n----- TOP SKILLS -----")
print(skills_df["skill"].value_counts().head(15))

print("\n----- SQL CHECK -----")
print(
    skills_df[
        skills_df["skill"].isin(["SQL", "MS SQL Server"])
    ]["skill"].value_counts()
)

print("\n----- SAMPLE RECORDS -----")
print(
    skills_df[
        [
            "job_id",
            "company_name",
            "skill",
            "salary_avg",
            "experience_years"
        ]
    ].head(10).to_string(index=False)
)