import React, { useState } from 'react';
import axios from 'axios';

function TransactionForm() {
  const [fromAddress, setFromAddress] = useState('');
  const [toAddress, setToAddress] = useState('');
  const [amount, setAmount] = useState('');
  const [status, setStatus] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const sendTransaction = async () => {
    if (!fromAddress.trim() || !toAddress.trim() || !amount.trim()) {
      setError("⚠ All fields are required.");
      return;
    }

    if (isNaN(amount) || Number(amount) <= 0) {
      setError("⚠ Amount must be a valid number greater than 0.");
      return;
    }

    setLoading(true);
    try {
      const response = await axios.post('http://localhost:5000/transaction/send', {
        sender: fromAddress,
        recipient : toAddress,
        amount: Number(amount),
      });

      setStatus(`✅ Transaction sent successfully! TX Hash: ${response.data.txHash}`);
      setError('');
      setFromAddress('');
      setToAddress('');
      setAmount('');
    } catch (err) {
      console.error(err);
      setError('❌ Failed to send transaction. Please check details and try again.');
      setStatus('');
    }
    setLoading(false);
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>🚀 Send Transaction</h2>

      <input
        type="text"
        placeholder="From Address"
        value={fromAddress}
        onChange={(e) => {
          setFromAddress(e.target.value);
          setError('');
        }}
        style={styles.input}
      />
      <input
        type="text"
        placeholder="To Address"
        value={toAddress}
        onChange={(e) => {
          setToAddress(e.target.value);
          setError('');
        }}
        style={styles.input}
      />
      <input
        type="text"
        placeholder="Amount"
        value={amount}
        onChange={(e) => {
          setAmount(e.target.value);
          setError('');
        }}
        style={styles.input}
      />

      <button
        onClick={sendTransaction}
        style={{
          ...styles.button,
          background: loading
            ? 'rgba(150,150,150,0.5)'
            : 'linear-gradient(90deg, #00ff85, #0080ff)',
        }}
        disabled={loading}
      >
        {loading ? '⏳ Sending...' : '📤 Send'}
      </button>

      {status && (
        <div style={styles.success} className="fadeIn">
          {status}
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
          border: 1px solid #0080ff !important;
          box-shadow: 0 0 8px rgba(0,128,255,0.5);
        }
        button:hover:not(:disabled) {
          transform: scale(1.05);
          box-shadow: 0 4px 15px rgba(0,128,255,0.4);
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
    background: 'linear-gradient(90deg, #00ff85, #0080ff)',
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
    wordBreak: 'break-all',
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

export default TransactionForm;
