import React, { useState } from 'react';
import axios from 'axios';

function MineBlock() {
  const [minerAddress, setMinerAddress] = useState('');
  const [result, setResult] = useState('');

  const mine = async () => {
    try {
      const res = await axios.post('http://localhost:5000/mine', {
        miner_address: minerAddress
      });
      setResult(`✅ Mined Block #${res.data.index}`);
    } catch (err) {
      setResult('❌ Mining failed');
    }
  };

  return (
    <div style={styles.container}>
      <h2>⛏️ Mine Block</h2>
      <input placeholder="Miner Address" value={minerAddress} onChange={e => setMinerAddress(e.target.value)} style={styles.input} />
      <button onClick={mine} style={styles.button}>Mine</button>
      {result && <p>{result}</p>}
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
  input: {
    width: '100%',
    marginBottom: '0.5rem',
    padding: '0.5rem',
    fontSize: '1rem'
  },
  button: {
    padding: '0.5rem 1rem',
    backgroundColor: '#ff9800',
    color: 'white',
    border: 'none',
    cursor: 'pointer',
    fontSize: '1rem'
  }
};

export default MineBlock;
