import React, { useState } from 'react';
import axios from 'axios';

function MineBlock() {
  const [minerAddress, setMinerAddress] = useState('');
  const [result, setResult] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const mine = async () => {
    if (!minerAddress.trim()) {
      setError("⚠ Miner address can't be empty.");
      return;
    }

    setLoading(true);
    try {
      const res = await axios.post('http://localhost:5000/mine', {
        miner_address: minerAddress
      });
      setResult(`✅ Mined Block #${res.data.index}`);
      setError('');
    } catch (err) {
      console.error(err);
      setError('❌ Mining failed. Is the backend running?');
    }
    setLoading(false);
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>⛏️ Mine Block</h2>
      <input
        type="text"
        placeholder="Enter miner address"
        value={minerAddress}
        onChange={(e) => {
          setMinerAddress(e.target.value);
          setError('');
        }}
        style={styles.input}
      />

      <button
        onClick={mine}
        style={{
          ...styles.button,
          background: loading
            ? 'rgba(150,150,150,0.5)'
            : 'linear-gradient(90deg, #ff9800, #ff5722)',
        }}
        disabled={loading}
      >
        {loading ? '⏳ Mining...' : '🚀 Start Mining'}
      </button>

      {result && (
        <div style={styles.success} className="fadeIn">
          {result}
        </div>
      )}

      {error && <div style={styles.error}>{error}</div>}

      <style>{`
        .fadeIn {
          animation: fadeIn 0.6s ease-in-out;
        }
        @keyframes fadeIn {
          from { opacity: 0; transform: translateY(8px); }
          to { opacity: 1; transform: translateY(0); }
        }
        input:focus {
          border: 1px solid #ff9800 !important;
          box-shadow: 0 0 8px rgba(255,152,0,0.5);
        }
        button:hover:not(:disabled) {
          transform: scale(1.05);
          box-shadow: 0 4px 15px rgba(255,152,0,0.4);
        }
      `}</style>
    </div>
  );
}

const styles = {
  container: {
    padding: '2rem',
    borderRadius: '16px',
    maxWidth: '500px',
    margin: '2rem auto',
    textAlign: 'center',
    backdropFilter: 'blur(10px)',
    background: 'rgba(255, 255, 255, 0.08)',
    border: '1px solid rgba(255,255,255,0.2)',
    boxShadow: '0 8px 32px rgba(0,0,0,0.2)',
    fontFamily: "'JetBrains Mono', monospace",
    color: '#fff',
  },
  title: {
    fontSize: '1.8rem',
    marginBottom: '1.5rem',
    background: 'linear-gradient(90deg, #ff9800, #ff5722)',
    WebkitBackgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
  },
  input: {
    padding: '0.75rem',
    width: '80%',
    fontSize: '1rem',
    marginBottom: '1rem',
    borderRadius: '6px',
    border: '1px solid rgba(255,255,255,0.3)',
    outline: '1px solid black',
    background: 'rgba(255,255,255,0.05)',
    color: '#6b6b6bff',
    transition: 'all 0.2s ease',
  },
  button: {
    padding: '0.7rem 1.5rem',
    fontSize: '1rem',
    cursor: 'pointer',
    color: 'white',
    border: 'none',
    borderRadius: '6px',
    transition: 'all 0.3s ease',
  },
  success: {
    marginTop: '1.5rem',
    background: 'rgba(0,255,0,0.1)',
    padding: '1rem',
    borderRadius: '6px',
    color: '#7CFC00',
    fontWeight: '500',
    border: '1px solid rgba(0,255,0,0.3)',
  },
  error: {
    marginTop: '1rem',
    background: 'rgba(255,0,0,0.1)',
    padding: '0.75rem',
    borderRadius: '6px',
    color: '#ff6b6b',
    fontWeight: '500',
    border: '1px solid rgba(255,0,0,0.3)',
  },
};

export default MineBlock;
