const express = require("express");
const cors = require("cors");
const fs = require("fs");
const path = require("path");

const app = express();
const PORT = 5000;

app.use(cors());
app.use(express.json());

/* Home route */
app.get("/", (req, res) => {
  res.json({
    message: "Job Market & Skill Gap Analyzer API is running",
  });
});

/* Jobs API - reads JSON */
app.get("/api/jobs", (req, res) => {
  const filePath = path.join(
    __dirname,
    "..",
    "data",
    "cleaned",
    "jobs.json"
  );

  try {
    const jobs = JSON.parse(fs.readFileSync(filePath, "utf8"));
    res.json(jobs);
  } catch (error) {
    console.error("Error reading jobs:", error);

    res.status(500).json({
      error: "Unable to read jobs data",
    });
  }
});

/* Skills API */
app.get("/api/skills", (req, res) => {
  const filePath = path.join(
    __dirname,
    "..",
    "data",
    "cleaned",
    "skill_demand.csv"
  );

  try {
    const file = fs.readFileSync(filePath, "utf8");
    const lines = file.trim().split(/\r?\n/);
    const headers = lines[0].split(",");

    const skills = lines.slice(1).map((line) => {
      const values = line.split(",");
      const row = {};

      headers.forEach((header, index) => {
        row[header] = values[index] || "";
      });

      return row;
    });

    res.json(skills);
  } catch (error) {
    console.error("Error reading skills:", error);

    res.status(500).json({
      error: "Unable to read skills data",
    });
  }
});

/* Salary API */
app.get("/api/salary", (req, res) => {
  const filePath = path.join(
    __dirname,
    "..",
    "data",
    "cleaned",
    "salary_by_skill.csv"
  );

  try {
    const file = fs.readFileSync(filePath, "utf8");
    const lines = file.trim().split(/\r?\n/);
    const headers = lines[0].split(",");

    const salary = lines.slice(1).map((line) => {
      const values = line.split(",");
      const row = {};

      headers.forEach((header, index) => {
        row[header] = values[index] || "";
      });

      return row;
    });

    res.json(salary);
  } catch (error) {
    console.error("Error reading salary:", error);

    res.status(500).json({
      error: "Unable to read salary data",
    });
  }
});

/* Start server */
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});