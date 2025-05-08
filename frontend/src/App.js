import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!text.trim()) return;
    setLoading(true);
    try {
      const response = await axios.post('http://localhost:8000/predict', { text });
      setResult(response.data);
    } catch (error) {
      alert("Error: " + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1 className="title">BERT Sentiment Predictor</h1>

      <textarea
        className="input-box"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter your text here..."
      />

      <button className="predict-btn" onClick={handleSubmit} disabled={loading}>
        {loading ? "Analyzing..." : "Predict"}
      </button>

      {result && (
        <div className="result-box fade-in">
          <p><strong>Sentiment:</strong> {result.sentiment}</p>
          <p><strong>Confidence:</strong> {result.confidence}</p>
        </div>
      )}

    <div className="project-info fade-in">
      <h3>Project Members</h3>
      <ul>
        <li><strong>Yuheng Liu</strong> — yl12469</li>
        <li><strong>Hantao Xie</strong> — hx2542</li>
        <li><strong>Changxu Zhu</strong> — cz3106</li>
      </ul>
    </div>

    </div>
  );
}

export default App;
