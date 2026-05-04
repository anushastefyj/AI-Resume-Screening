import React, { useState } from "react";
import UploadResume from "./components/UploadResume";
import Result from "./components/Result";
import "./App.css";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="app-container">
      <h1 className="title">AI Resume Screening System</h1>

      <UploadResume setResult={setResult} />

      <Result data={result} />
    </div>
  );
}

export default App;