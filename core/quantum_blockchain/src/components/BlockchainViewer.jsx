import React, { useState } from 'react';
import axios from 'axios';

function BlockchainViewer() {
  const [chain, setChain] = useState([]);
  const [error, setError] = useState('');

  const fetchChain = async () => {
    setError('');
    try {
      const res = await axios.get('http://localhost:5000/chain');
      setChain(res.data.chain || []);
    } catch (err) {
      setError('❌ Failed to fetch blockchain. Is the backend running?');
      setChain([]);
    }
  };

  return (
    <div style={styles.container}>
      <h2 style={{ ...styles.title, background: 'linear-gradient(90deg, #00f2ff, #6f00ff)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>
        🧱 Blockchain Viewer
      </h2>

      <button onClick={fetchChain} style={styles.button}>
        🔍 View Chain
      </button>

      {error && <div style={styles.error}>{error}</div>}

      <div style={styles.scroll}>
        {chain.map((block, idx) => (
          <pre
            key={block.index}
            style={{
              ...styles.block,
              backgroundColor: idx % 2 === 0 ? 'rgba(255,255,255,0.05)' : 'rgba(255,255,255,0.08)'
            }}
          >
            {JSON.stringify(block, null, 2)}
          </pre>
        ))}
      </div>
    </div>
  );
}

const styles = {
  container: {
    marginTop: '2rem',
    padding: '2rem',
    background: 'rgba(255, 255, 255, 0.05)',
    backdropFilter: 'blur(12px)',
    borderRadius: '15px',
    boxShadow: '0 8px 30px rgba(0, 0, 0, 0.2)',
    fontFamily: "'JetBrains Mono', monospace",
    maxWidth: '900px',
    marginLeft: 'auto',
    marginRight: 'auto',
    border: '1px solid rgba(255,255,255,0.1)',
    color: '#eee'
  },
  title: {
    fontSize: '1.8rem',
    marginBottom: '1.5rem',
    textAlign: 'center',
    fontWeight: '700',
  },
  button: {
    padding: '0.7rem 1.8rem',
    background: 'linear-gradient(90deg, #00b4db, #0083b0)',
    color: 'white',
    border: 'none',
    borderRadius: '8px',
    cursor: 'pointer',
    fontSize: '1rem',
    fontWeight: '700',
    transition: 'transform 0.2s ease, box-shadow 0.3s ease',
    display: 'block',
    margin: '0 auto 1.5rem auto',
  },
  scroll: {
    maxHeight: '400px',
    overflowY: 'auto',
    padding: '1rem',
    borderRadius: '8px',
    background: 'rgba(255,255,255,0.02)',
    border: '1px solid rgba(255,255,255,0.06)',
  },
  block: {
    fontFamily: 'monospace',
    fontSize: '0.9rem',
    padding: '1rem',
    marginBottom: '1rem',
    borderRadius: '6px',
    border: '1px solid rgba(255,255,255,0.06)',
    color: '#eaeaea',
  },
  error: {
    background: 'rgba(255, 0, 0, 0.15)',
    color: '#ff7b7b',
    padding: '0.8rem',
    textAlign: 'center',
    borderRadius: '6px',
    marginBottom: '1rem',
    border: '1px solid rgba(255, 0, 0, 0.25)',
    fontWeight: '600',
  }
};

export default BlockchainViewer;
