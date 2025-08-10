import React, { useState } from 'react';
import WalletManager from './components/WalletManager';
import TransactionForm from './components/TransactionForm';
import MineBlock from './components/MineBlock';
import BlockchainViewer from './components/BlockchainViewer';
import ToolsPanel from './components/ToolsPanel';

function App() {
  const [showMainApp, setShowMainApp] = useState(false);
  const [theme, setTheme] = useState("light");

  const isDark = theme === "dark";

  const toggleTheme = () => setTheme(isDark ? "light" : "dark");

  const colors = {
    light: {
      text: "#000",
      cardBg: "rgba(255, 255, 255, 0.95)",
      appBg: "radial-gradient(circle at 20% 20%, #f0f4ff 0%, #ffffff 100%)",
      heroBg: "linear-gradient(270deg, #e0f7ff, #f5f0ff, #e0f7ff)",
    },
    dark: {
      text: "#fff",
      cardBg: "rgba(20, 20, 30, 0.9)",
      appBg: "radial-gradient(circle at 20% 20%, #0f0f17 0%, #1a1a27 100%)",
      heroBg: "linear-gradient(270deg, #0f1c2e, #1a1027, #0f1c2e)",
    }
  };

  if (!showMainApp) {
    return (
      <div
        style={{
          ...styles.heroPage,
          background: colors[theme].heroBg,
          color: colors[theme].text,
          backgroundSize: "600% 600%",
          animation: "gradientMove 15s ease infinite",
        }}
      >
        {/* Theme Toggle */}
        <button style={styles.themeToggle} onClick={toggleTheme}>
          {isDark ? "☀ Light Mode" : "🌙 Dark Mode"}
        </button>

        {/* Title */}
        <h1 style={styles.glitchTitle}>Welcome to BlockWächter</h1>
        <p style={styles.description}>
          Harnessing the power of <strong>Post-Quantum Cryptography</strong> with CRYSTALS-Dilithium
          to create a secure, future-ready blockchain platform.
        </p>

        {/* Feature Cards */}
        <div style={styles.featureContainer}>
          <div style={{ ...styles.featureCard, background: colors[theme].cardBg }}>
            <h3>🔐 Quantum-Safe Security</h3>
            <p>Resistant to quantum computer attacks using next-gen cryptography.</p>
          </div>
          <div style={{ ...styles.featureCard, background: colors[theme].cardBg }}>
            <h3>⚡ Fast & Transparent</h3>
            <p>Real-time transactions with complete blockchain transparency.</p>
          </div>
          <div style={{ ...styles.featureCard, background: colors[theme].cardBg }}>
            <h3>🛠 Developer Friendly</h3>
            <p>Tools and APIs to easily integrate blockchain into your apps.</p>
          </div>
        </div>

        {/* CTA */}
        <button style={styles.ctaButton} onClick={() => setShowMainApp(true)}>
          🚀 Get Started
        </button>

        {/* Footer Tagline */}
        <p style={styles.footerTag}>Future-proof your transactions. Today.</p>

        {/* Background Animation */}
        <style>
          {`
          @keyframes gradientMove {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
          }
          `}
        </style>
      </div>
    );
  }

  return (
    <div
      style={{
        ...styles.app,
        backgroundImage: colors[theme].appBg,
        color: colors[theme].text
      }}
    >
      
      <button style={styles.themeToggle} onClick={toggleTheme}>
        {isDark ? "☀ Light Mode" : "🌙 Dark Mode"}
      </button>

      
      <h1 style={styles.glitchTitle}>BlockWächter</h1>

      <div style={{ ...styles.card, background: colors[theme].cardBg }}><WalletManager /></div>
      <div style={{ ...styles.card, background: colors[theme].cardBg }}><TransactionForm /></div>
      <div style={{ ...styles.card, background: colors[theme].cardBg }}><MineBlock /></div>
      <div style={{ ...styles.card, background: colors[theme].cardBg }}><BlockchainViewer /></div>
      <div style={{ ...styles.card, background: colors[theme].cardBg }}><ToolsPanel /></div>
    </div>
  );
}

const styles = {
  app: {
    fontFamily: "'JetBrains Mono', monospace",
    padding: '4rem 2rem',
    minHeight: '100vh',
    transition: 'background 0.4s ease, color 0.4s ease',
  },
  heroPage: {
    fontFamily: "'JetBrains Mono', monospace",
    minHeight: '100vh',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    textAlign: 'center',
    padding: '2rem',
    transition: 'background 0.4s ease, color 0.4s ease',
  },
  glitchTitle: {
    fontSize: '3.5rem',
    fontWeight: 'bold',
    letterSpacing: '2px',
    background: 'linear-gradient(90deg, #00f2ff, #6f00ff, #00f2ff)',
    WebkitBackgroundClip: 'text',
    WebkitTextFillColor: 'transparent',
    marginBottom: '1.5rem',
    textAlign: 'center',       
    display: 'block', 
  },
  description: {
    fontSize: '1.2rem',
    maxWidth: '650px',
    margin: '0 auto 2rem',
    lineHeight: '1.6',
  },
  featureContainer: {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'center',
    gap: '1.5rem',
    marginBottom: '2rem',
  },
  featureCard: {
    width: '260px',
    padding: '1.5rem',
    borderRadius: '12px',
    boxShadow: '0 6px 15px rgba(97, 97, 255, 0.15)',
    transition: 'transform 0.3s ease',
    cursor: 'default',
  },
  ctaButton: {
    padding: '0.8rem 1.8rem',
    fontSize: '1.1rem',
    borderRadius: '8px',
    border: 'none',
    cursor: 'pointer',
    background: 'linear-gradient(90deg, #00f2ff, #6f00ff)',
    color: '#fff',
    boxShadow: '0 4px 15px rgba(97, 97, 255, 0.4)',
    transition: 'transform 0.2s ease',
  },
  footerTag: {
    marginTop: '3rem',
    fontSize: '0.9rem',
    opacity: 0.7,
  },
  themeToggle: {
    position: 'absolute',
    top: '1.5rem',
    right: '1.5rem',
    padding: '0.5rem 1rem',
    border: 'none',
    borderRadius: '6px',
    background: 'rgba(0,0,0,0.2)',
    color: '#fff',
    cursor: 'pointer',
    fontSize: '0.9rem',
  },
  card: {
    borderRadius: '16px',
    padding: '2.2rem',
    marginBottom: '2.5rem',
    boxShadow: '0 8px 20px rgba(97, 97, 255, 0.15)',
    transition: 'transform 0.4s ease, box-shadow 0.4s ease, background 0.4s ease',
    border: '1px solid rgba(97, 97, 255, 0.2)',
    backdropFilter: 'blur(4px)',
  },
};

export default App;
