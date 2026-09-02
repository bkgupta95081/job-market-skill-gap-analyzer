-- 1. Top 10 most demanded skills
SELECT
    skill,
    COUNT(DISTINCT job_id) AS job_count
FROM job_skills
GROUP BY skill
ORDER BY job_count DESC
LIMIT 10;


-- 2. Skills appearing in at least 2 jobs
-- with their average salary
SELECT
    skill,
    COUNT(DISTINCT job_id) AS job_count,
    ROUND(AVG(salary_avg), 0) AS average_salary
FROM job_skills
GROUP BY skill
HAVING COUNT(DISTINCT job_id) >= 2
ORDER BY average_salary DESC;


-- 3. Average salary by experience level
SELECT
    experience_years,
    COUNT(*) AS job_count,
    ROUND(AVG(salary_avg), 0) AS average_salary
FROM jobs
GROUP BY experience_years
ORDER BY experience_years;


-- 4. Locations with the most job postings
SELECT
    locations,
    COUNT(*) AS job_count
FROM jobs
GROUP BY locations
ORDER BY job_count DESC
LIMIT 10;