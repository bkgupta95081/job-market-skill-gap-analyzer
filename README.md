# Job Market & Skill Gap Analyzer

This project looks at job postings and tries to answer a simple question:

**What skills are companies asking for, and which skills are more valuable in the current job market?**

I built this project to practice data cleaning, data analysis, SQL, and data visualization using a real-world job dataset.

## What I did

The project follows a simple process:

**Raw job data → Data cleaning → Skill extraction → Analysis → SQL queries → Charts → Insights**

### 1. Data Cleaning

The original dataset contained 8,950 rows. After checking the data, I found that many rows were exact duplicates.

- Original rows: **8,950**
- Duplicate rows removed: **8,900**
- Unique job postings used for analysis: **50**
- Missing values: **None**

I also cleaned the column names and converted salary and experience information into usable numerical values.

### 2. Skill Analysis

The skills in the dataset were stored together in a single text field, so I extracted recognizable skills using a controlled list of skills found in the dataset.

Some of the frequently appearing skills were:

- Effective Communication
- English Proficiency
- MS-Excel
- Sales
- MS-Office
- Negotiation
- Client Relationship Management (CRM)

### 3. Salary Analysis

For salary ranges, I calculated the midpoint between the minimum and maximum salary.

This helped me compare the average salary associated with different skills.

For example, skills such as:

- Digital Marketing
- Accounting
- Sales Management
- Negotiation
- Data Analytics

showed relatively higher average salaries in this dataset.

## SQL Analysis

I also used SQLite to perform queries such as:

- Most demanded skills
- Average salary by skill
- Salary by experience level
- Locations with the most job postings

## Visualizations

The project includes charts for:

- Top skills by job demand
- Average salary by skill

These charts are saved inside the `analysis` folder.

## Technologies Used

- **Python**
- **Pandas**
- **SQLite / SQL**
- **Matplotlib**
- **Git & GitHub**

## Project Structure

```text
job-market-skill-gap-analyzer
│
├── analysis
│   ├── Python analysis scripts
│   ├── SQL queries
│   └── charts
│
├── data
│   ├── raw
│   └── cleaned
│
├── backend
├── frontend
│
└── README.md
