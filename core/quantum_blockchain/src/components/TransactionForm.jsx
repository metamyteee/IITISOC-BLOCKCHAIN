import React, { useState } from 'react';
import axios from 'axios';

function TransactionForm() {
  const [from, setFrom] = useState('');
  const [to, setTo] = useState('');
  const [amount, setAmount] = useState('');
  const [message, setMessage] = useState('');

  const sendTransaction = async () => {
    try {
      const res = await axios.post('http://localhost:5000/transaction/send', {
        sender: from,
        recipient: to,
        amount: parseFloat(amount)
      });
      setMessage(`✅ ${res.data.message || 'Transaction added!'}`);
    } catch (err) {
      setMessage('❌ Failed to send transaction');
    }
  };

  return (
    <div style={styles.container}>
      <h2>💸 Send Transaction</h2>
      <input placeholder="From Address" value={from} onChange={e => setFrom(e.target.value)} style={styles.input} />
      <input placeholder="To Address" value={to} onChange={e => setTo(e.target.value)} style={styles.input} />
      <input placeholder="Amount" value={amount} onChange={e => setAmount(e.target.value)} style={styles.input} />
      <button onClick={sendTransaction} style={styles.button}>Send</button>
      {message && <p>{message}</p>}
    </div>
  );
}

const styles = {
  container: {
    marginTop: '2rem',
    background: '#fff',
    padding: '1rem',
    borderRadius: '8px',
    boxShadow: '0 2px 10px rgba(0,0,0,0.1)'
  },
  input: {
    width: '100%',
    marginBottom: '0.5rem',
    padding: '0.5rem',
    fontSize: '1rem'
  },
  button: {
    padding: '0.5rem 1rem',
    backgroundColor: '#4caf50',
    color: 'white',
    border: 'none',
    cursor: 'pointer',
    fontSize: '1rem'
  }
};

export default TransactionForm;
