import React from "react";

function Result({ data }) {
  if (!data) return null;

  return (
    <div className="result-box">
      <h2>Results</h2>

      <h3>Skills</h3>
      <ul>
        {data.skills.map((skill, index) => (
          <li key={index}>{skill}</li>
        ))}
      </ul>

      <h3>Job Recommendations</h3>
      <ul>
        {Object.entries(data.recommendations).map(([job, score]) => (
          <li key={job}>
            {job}: {score}%
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Result;