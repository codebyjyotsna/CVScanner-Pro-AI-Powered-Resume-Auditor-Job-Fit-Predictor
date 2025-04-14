import React, { useState } from 'react';

function App() {
  const [resume, setResume] = useState(null);
  const [jd, setJd] = useState(null);
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('resume', resume);
    formData.append('jd', jd);

    const response = await fetch('http://localhost:5000/upload', {
      method: 'POST',
      body: formData
    });

    const data = await response.json();
    setResult(data);
  };

  return (
    <div className="App">
      <h1>CVScanner Pro</h1>
      <input type="file" onChange={(e) => setResume(e.target.files[0])} />
      <input type="file" onChange={(e) => setJd(e.target.files[0])} />
      <button onClick={handleUpload}>Analyze</button>

      {result && (
        <div>
          <h2>Results</h2>
          <p>Match Score: {result.match_score}</p>
          <p>Label: {result.labels}</p>
          <h3>Suggestions:</h3>
          <p>{result.suggestions}</p>
        </div>
      )}
    </div>
  );
}

export default App;
