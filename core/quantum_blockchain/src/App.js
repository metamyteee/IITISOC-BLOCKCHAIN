import React from 'react';
import WalletManager from './components/WalletManager';
import TransactionForm from './components/TransactionForm';
import MineBlock from './components/MineBlock';
import BlockchainViewer from './components/BlockchainViewer';
import ToolsPanel from './components/ToolsPanel';

function App() {
  return (
    <div style={styles.container}>
      <h1 style={styles.title}>💠 Quantum Blockchain DApp</h1>
      <WalletManager />
      <TransactionForm />
      <MineBlock />
      <BlockchainViewer />
      <ToolsPanel />
    </div>
  );
}

const styles = {
  container: {
    fontFamily: 'Arial, sans-serif',
    padding: '2rem',
    backgroundColor: '#f9f9f9'
  },
  title: {
    textAlign: 'center',
    color: '#1976d2'
  }
};

export default App;
