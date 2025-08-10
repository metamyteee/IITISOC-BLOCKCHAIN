import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ToolsPanel() {
  const [walletName, setWalletName] = useState('');
  const [balance, setBalance] = useState(null);
  const [wallets, setWallets] = useState([]);
  const [pending, setPending] = useState([]);

  useEffect(() => {
    listWallets();
  }, []);

  const checkBalance = async () => {
    try {
      if (!walletName) {
        alert("Please select a wallet name first.");
        return;
      }
      const res = await axios.get(`http://localhost:5000/wallet/balance/name/${walletName}`);
      setBalance(res.data.balance);
    } catch {
      setBalance(null);
    }
  };

  const listWallets = async () => {
    try {
      const res = await axios.get(`http://localhost:5000/wallets`);
      setWallets(res.data.wallets);
    } catch {
      setWallets([]);
    }
  };

  const fetchPendingTransactions = async () => {
    try {
      const res = await axios.get(`http://localhost:5000/transactions/pending`);
      setPending(res.data.pending_transactions);
    } catch {
      setPending([]);
    }
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>
        🛠 Tools Panel
      </h2>

      {/* Balance Section */}
      <div style={styles.section}>
        <select
          value={walletName}
          onChange={(e) => setWalletName(e.target.value)}
          style={styles.input}
        >
          <option value="">Select Wallet</option>
          {wallets.map((w, i) => (
            <option key={i} value={w.name}>{w.name}</option>
          ))}
        </select>
        <button onClick={checkBalance} style={styles.button}>💰 Check Balance</button>
        {balance !== null && (
          <p style={styles.info}>
            Balance of <strong>{walletName}</strong>: {balance}
          </p>
        )}
      </div>

      {/* Wallet List */}
      <div style={styles.section}>
        <button onClick={listWallets} style={styles.button}>📜 List All Wallets</button>
        <ul style={styles.list}>
          {wallets.map((w, i) => (
            <li key={i} style={styles.listItem}>
              🔑 <strong>{w.name}</strong>  
              <span style={styles.address}>{w.address.slice(0, 20)}...</span>
            </li>
          ))}
        </ul>
      </div>

      {/* Pending Transactions */}
      <div style={styles.section}>
        <button onClick={fetchPendingTransactions} style={styles.button}>🧾 Show Pending Transactions</button>
        <ul style={styles.list}>
          {pending.map((tx, i) => (
            <li key={i} style={styles.listItem}>
              {tx.sender} → {tx.recipient} | 💸 {tx.amount}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

const styles = {
  container: {
    marginTop: '2rem',
    padding: '2rem',
    background: 'rgba(255, 255, 255, 0.08)',
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
    background: 'linear-gradient(90deg, #8B0000, #FF0000)',
    WebkitBackgroundClip: 'text',
    WebkitTextFillColor: 'transparent'
  },
  section: {
    marginBottom: '1.8rem',
    paddingBottom: '1rem',
    borderBottom: '1px solid rgba(255,255,255,0.05)'
  },
  input: {
    padding: '0.6rem',
    marginRight: '0.8rem',
    width: '60%',
    borderRadius: '8px',
    border: '1px solid rgba(0, 0, 0, 1)',
    background: 'rgba(255,255,255,0.05)',
    color: '#00000060'
  },
  button: {
    padding: '0.6rem 1.4rem',
    background: 'linear-gradient(90deg, #8B0000, #FF0000)',
    color: 'white',
    border: 'none',
    borderRadius: '8px',
    cursor: 'pointer',
    fontWeight: '700',
    transition: 'transform 0.2s ease, box-shadow 0.3s ease',
  },
  list: {
    marginTop: '0.8rem',
    listStyle: 'none',
    padding: 0
  },
  listItem: {
    background: 'rgba(255,255,255,0.05)',
    padding: '0.8rem',
    marginBottom: '0.5rem',
    borderRadius: '6px',
    border: '1px solid rgba(255,255,255,0.06)'
  },
  address: {
    display: 'block',
    fontSize: '0.85rem',
    color: '#bbb'
  },
  info: {
    marginTop: '0.6rem',
    fontSize: '1rem',
    color: '#aaffaa'
  }
};

export default ToolsPanel;
