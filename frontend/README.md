# Job Market & Skill Gap Analyzer

This project is about understanding what skills companies are looking for in job postings and what the current job market looks like for students and freshers.

I built this project to analyze job data and present the results in a simple dashboard.

## What does this project do?

The project mainly focuses on three things:

* Finding the most requested skills in job postings
* Understanding salary patterns
* Getting a quick overview of the job market

For example, from the dataset, skills like **English communication, MS-Excel, Sales, MS-Office and Negotiation** appear frequently.

## My Approach

I started with the job posting dataset and cleaned the data before doing the analysis.

The original dataset had around **8,950 records**. After removing exact duplicate records, I used **50 unique job postings** for the final analysis.

I then analyzed the skills and salary information and created APIs to send this data to the frontend.

## Dashboard

The dashboard has three sections:

### Overview

Shows a quick summary of the dataset:

* Unique jobs
* Skill records
* Average salary
* Experience range

### Skills

This section shows which skills are requested most often.

I used a bar chart to make it easier to compare the demand for different skills.

### Salary

This section shows the average salary and salary information related to different skills.

## Technologies I Used

**Frontend**

* React
* Vite
* Recharts
* CSS

**Backend**

* Node.js
* Express.js
* REST API
* CORS

**Data Analysis**

* Python
* SQL
* CSV
* JSON

## How the Project Works

```text
Job Data
   ↓
Data Cleaning
   ↓
Python / SQL Analysis
   ↓
Cleaned Data
   ↓
Express API
   ↓
React Frontend
   ↓
Dashboard
```

The React frontend gets the data from the backend using API requests.

For example:

```text
React
  ↓
/api/skills
  ↓
Express Backend
  ↓
skill_demand.csv
  ↓
Skills shown on dashboard
```

## Running the Project

### Backend

Open the terminal and go to the backend folder:

```bash
cd backend
```

Install the required packages:

```bash
npm install
```

Start the backend:

```bash
npm run server.js
```

The backend runs on:

```text
http://localhost:5000
```

### Frontend

Open another terminal:

```bash
cd frontend
```

Install the packages:

```bash
npm install
```

Start the frontend:

```bash
npm run dev
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:5173
```

## What I Learned

While building this project, I got practical experience with:

* Cleaning and analyzing real-world data
* Working with Python and SQL
* Creating REST APIs using Express
* Connecting a React frontend with a backend
* Displaying data using charts
* Managing a project using Git and GitHub

## Future Improvements

I would like to improve this project further by adding:

* Job role filters
* Location-based analysis
* A personal skill-gap checker
* Job recommendations based on skills
* More job data for better analysis
* Online deployment

## GitHub

The complete project is available here:

**github.com/bkgupta95081/job-market-skill-gap-analyzer**

## Author

**Prince Gupta**

This project was built as a learning and data-analysis project to understand the job market and the skills companies are looking for.
