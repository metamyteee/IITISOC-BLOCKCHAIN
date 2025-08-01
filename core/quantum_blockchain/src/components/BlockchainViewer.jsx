import React, { useState } from 'react';
import axios from 'axios';

function BlockchainViewer() {
  const [chain, setChain] = useState([]);

  const fetchChain = async () => {
    try {
      const res = await axios.get('http://localhost:5000/chain');
      setChain(res.data.chain || []);
    } catch (err) {
      setChain([]);
    }
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>🧱 Blockchain Viewer</h2>
      <button onClick={fetchChain} style={styles.button}>🔍 View Chain</button>
      <div style={styles.scroll}>
        {chain.map((block, idx) => (
          <pre
            key={block.index}
            style={{
              ...styles.block,
              backgroundColor: idx % 2 === 0 ? '#f0f0f0' : '#e0e0e0'
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
    background: '#fdfdfd',
    borderRadius: '10px',
    boxShadow: '0 8px 20px rgba(0, 0, 0, 0.1)',
    fontFamily: `'Segoe UI', Tahoma, Geneva, Verdana, sans-serif`,
    maxWidth: '800px',
    marginLeft: 'auto',
    marginRight: 'auto',
  },
  title: {
    fontSize: '1.8rem',
    color: '#333',
    marginBottom: '1.5rem',
    textAlign: 'center',
  },
  button: {
    padding: '0.7rem 1.5rem',
    background: 'linear-gradient(90deg, #607d8b, #455a64)',
    color: 'white',
    border: 'none',
    borderRadius: '6px',
    cursor: 'pointer',
    fontSize: '1rem',
    fontWeight: 'bold',
    transition: 'background 0.3s ease',
    display: 'block',
    margin: '0 auto 1.5rem auto',
  },
  scroll: {
    maxHeight: '400px',
    overflowY: 'auto',
    backgroundColor: '#f5f5f5',
    padding: '1rem',
    borderRadius: '6px',
    border: '1px solid #ccc',
  },
  block: {
    fontFamily: 'monospace',
    fontSize: '0.95rem',
    padding: '1rem',
    marginBottom: '1rem',
    borderRadius: '4px',
    border: '1px solid #ccc',
    whiteSpace: 'pre-wrap',
    wordWrap: 'break-word',
  },
};

export default BlockchainViewer;
