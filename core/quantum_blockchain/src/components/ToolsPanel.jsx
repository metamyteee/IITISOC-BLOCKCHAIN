import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ToolsPanel() {
  const [walletName, setWalletName] = useState('');
  const [balance, setBalance] = useState(null);
  const [wallets, setWallets] = useState([]);
  const [pending, setPending] = useState([]);

  useEffect(() => {
    // Fetch wallets initially
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
    } catch (err) {
      console.error(err);
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
      <h2>🛠️ Tools Panel</h2>

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
        <button onClick={checkBalance} style={styles.button}>Check Balance</button>
        {balance !== null && <p>💰 Balance of <strong>{walletName}</strong>: {balance}</p>}
      </div>

      <div style={styles.section}>
        <button onClick={listWallets} style={styles.button}>List All Wallets</button>
        <ul>
          {wallets.map((w, i) => (
            <li key={i}>🔑 {w.name}: <code>{w.address.slice(0, 20)}...</code></li>
          ))}
        </ul>
      </div>

      <div style={styles.section}>
        <button onClick={fetchPendingTransactions} style={styles.button}>Show Pending Transactions</button>
        <ul>
          {pending.map((tx, i) => (
            <li key={i}>
              🧾 {tx.sender} → {tx.recipient} | 💸 {tx.amount}
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
    padding: '1rem',
    background: '#fff',
    borderRadius: '8px',
    boxShadow: '0 2px 10px rgba(0,0,0,0.1)'
  },
  section: {
    marginBottom: '1rem'
  },
  input: {
    padding: '0.5rem',
    marginRight: '0.5rem',
    width: '60%'
  },
  button: {
    padding: '0.5rem 1rem',
    backgroundColor: '#2196f3',
    color: 'white',
    border: 'none',
    cursor: 'pointer'
  }
};

export default ToolsPanel;
