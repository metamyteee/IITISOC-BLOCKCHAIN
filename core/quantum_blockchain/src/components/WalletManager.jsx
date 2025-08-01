import React, { useState } from 'react';
import axios from 'axios';

function WalletManager() {
  const [walletName, setWalletName] = useState('');
  const [walletAddress, setWalletAddress] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const createWallet = async () => {
    if (!walletName.trim()) {
      setError("Wallet name can't be empty.");
      return;
    }

    setLoading(true);
    try {
      const response = await axios.post('http://localhost:5000/wallet/create', {
        name: walletName,
      });
      setWalletAddress(response.data.address);
      setError('');
    } catch (err) {
      console.error(err);
      setError('❌ Failed to create wallet. Is the backend running?');
    }
    setLoading(false);
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>🔐 Wallet Manager</h2>
      <input
        type="text"
        placeholder="Enter wallet name"
        value={walletName}
        onChange={(e) => {
          setWalletName(e.target.value);
          setError(''); // clear error on typing
        }}
        style={styles.input}
      />

      <button
        onClick={createWallet}
        style={{ ...styles.button, backgroundColor: loading ? '#aaa' : '#1976d2' }}
        disabled={loading}
      >
        {loading ? 'Creating...' : '🚀 Create Wallet'}
      </button>

      {walletAddress && (
        <div style={{ ...styles.success, animation: 'fadeIn 0.6s ease-in-out' }}>
          ✅ Wallet Created:
          <br />
          <code>{walletAddress}</code>
        </div>
      )}

      {error && <div style={styles.error}>{error}</div>}

      {/* Animation keyframe */}
      <style>{`
        @keyframes fadeIn {
          from { opacity: 0; transform: translateY(10px); }
          to { opacity: 1; transform: translateY(0); }
        }
      `}</style>
    </div>
  );
}

const styles = {
  container: {
    padding: '2rem',
    background: '#fff',
    borderRadius: '10px',
    maxWidth: '500px',
    margin: '2rem auto',
    textAlign: 'center',
    boxShadow: '0 8px 20px rgba(0,0,0,0.08)',
    fontFamily: `'Segoe UI', sans-serif`,
  },
  title: {
    fontSize: '1.8rem',
    marginBottom: '1.5rem',
    color: '#333',
  },
  input: {
    padding: '0.75rem',
    width: '80%',
    fontSize: '1rem',
    marginBottom: '1rem',
    borderRadius: '6px',
    border: '1px solid #ccc',
    outline: 'none',
    transition: 'border 0.2s ease',
  },
  button: {
    padding: '0.7rem 1.5rem',
    fontSize: '1rem',
    cursor: 'pointer',
    color: 'white',
    border: 'none',
    borderRadius: '6px',
    transition: 'background-color 0.3s ease',
  },
  success: {
    marginTop: '1.5rem',
    backgroundColor: '#e1fbe1',
    padding: '1rem',
    borderRadius: '6px',
    color: '#2e7d32',
    fontWeight: '500',
    wordBreak: 'break-all',
  },
  error: {
    marginTop: '1rem',
    backgroundColor: '#ffe6e6',
    padding: '0.75rem',
    borderRadius: '6px',
    color: '#d32f2f',
    fontWeight: '500',
  },
};

export default WalletManager;
