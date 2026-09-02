import { useEffect, useState } from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";
import "./App.css";

function App() {
  const [activeTab, setActiveTab] = useState("overview");
  const [skills, setSkills] = useState([]);
  const [salary, setSalary] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Promise.all([
      fetch("http://localhost:5000/api/skills").then((response) =>
        response.json()
      ),
      fetch("http://localhost:5000/api/salary").then((response) =>
        response.json()
      ),
    ])
      .then(([skillData, salaryData]) => {
        setSkills(skillData);
        setSalary(salaryData);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error loading data:", error);
        setLoading(false);
      });
  }, []);

  return (
    <div className="app">
      <header className="header">
        <div>
          <h1>Job Market & Skill Gap Analyzer</h1>
          <p>
            Exploring the skills companies ask for and what the job market
            looks like.
          </p>
        </div>
      </header>

      <nav className="nav">
        <button
          className={activeTab === "overview" ? "active" : ""}
          onClick={() => setActiveTab("overview")}
        >
          Overview
        </button>

        <button
          className={activeTab === "skills" ? "active" : ""}
          onClick={() => setActiveTab("skills")}
        >
          Skills
        </button>

        <button
          className={activeTab === "salary" ? "active" : ""}
          onClick={() => setActiveTab("salary")}
        >
          Salary
        </button>
      </nav>

      <main className="container">
        {activeTab === "overview" && (
          <>
            <section className="cards">
              <div className="card">
                <h3>Unique Jobs</h3>
                <strong>50</strong>
                <p>After removing duplicates</p>
              </div>

              <div className="card">
                <h3>Skill Records</h3>
                <strong>184</strong>
                <p>Skills identified from jobs</p>
              </div>

              <div className="card">
                <h3>Average Salary</h3>
                <strong>₹5.31 L</strong>
                <p>Across analyzed jobs</p>
              </div>

              <div className="card">
                <h3>Experience</h3>
                <strong>0–1 Year</strong>
                <p>Jobs in this dataset</p>
              </div>
            </section>

            <section className="panel">
              <h2>What I found</h2>

              <p>
                Communication and English skills appear frequently in the
                dataset, followed by Excel, Sales and other business skills.
              </p>

              <p>
                The original dataset contains 8,950 rows. After removing
                8,900 exact duplicate records, 50 unique job postings remain
                for analysis.
              </p>
            </section>
          </>
        )}

        {activeTab === "skills" && (
          <section className="panel">
            <h2>Most Requested Skills</h2>

            {loading ? (
              <p>Loading skill data...</p>
            ) : (
              <>
                <div className="chart">
                  <ResponsiveContainer width="100%" height={400}>
                    <BarChart data={skills.slice(0, 10)}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis
                        dataKey="skill"
                        angle={-25}
                        textAnchor="end"
                        height={100}
                      />
                      <YAxis />
                      <Tooltip />
                      <Bar dataKey="job_count" />
                    </BarChart>
                  </ResponsiveContainer>
                </div>

                <div className="skill-list">
                  {skills.slice(0, 15).map((skill) => (
                    <div className="skill-row" key={skill.skill}>
                      <span>{skill.skill}</span>
                      <strong>{skill.job_count} jobs</strong>
                    </div>
                  ))}
                </div>
              </>
            )}
          </section>
        )}

        {activeTab === "salary" && (
          <section className="panel">
            <h2>Salary Overview</h2>

            {loading ? (
              <p>Loading salary data...</p>
            ) : (
              <>
                <div className="salary-box">
                  <h3>Average salary across jobs</h3>

                  <div className="salary">₹5.31 L/year</div>

                  <p>
                    Salary ranges were converted into a midpoint before
                    calculating the overall average.
                  </p>
                </div>

                <div className="salary-box">
                  <h3>Average Salary by Skill</h3>

                  <div className="chart">
                    <ResponsiveContainer width="100%" height={400}>
                      <BarChart data={salary.slice(0, 10)}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis
                          dataKey="skill"
                          angle={-25}
                          textAnchor="end"
                          height={100}
                        />
                        <YAxis />
                        <Tooltip />
                        <Bar dataKey="average_salary" />
                      </BarChart>
                    </ResponsiveContainer>
                  </div>

                  {salary.slice(0, 10).map((item) => (
                    <div className="skill-row" key={item.skill}>
                      <span>{item.skill}</span>

                      <strong>
                        ₹
                        {(Number(item.average_salary) / 100000).toFixed(2)} L
                      </strong>
                    </div>
                  ))}
                </div>
              </>
            )}
          </section>
        )}
      </main>

      <footer>
        <p>
          Built as a data analysis project using Python, SQL and React.
        </p>
      </footer>
    </div>
  );
}

export default App;