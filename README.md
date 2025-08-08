# 🛡️ Post-Quantum Secure Blockchain using CRYSTALS-Dilithium

## 🔍 Overview
This project is a prototype blockchain system that integrates **post-quantum cryptography (PQC)** using the **CRYSTALS-Dilithium** digital signature scheme. Designed as a secure alternative to traditional ECDSA-based blockchain wallets, this system aims to withstand potential threats from quantum computing by replacing vulnerable signature schemes with quantum-resistant cryptographic primitives. We’ve developed a fully functional blockchain with:
- **Post-Quantum Wallets** using Dilithium
- **Transaction Signing and Verification**
- **Block Mining and Validation**
- **Frontend UI** for wallet management and blockchain interaction

## 🎯 Purpose
The purpose of this project is to:
- Explore and implement **quantum-safe cryptographic techniques** in blockchain infrastructure
- Provide a **research-oriented demo** of how blockchains can evolve to counter quantum threats
- Enable developers and researchers to understand and test the integration of **Dilithium** in real-world blockchain use cases

## ⚙️ Getting Started Locally

### 🧪 Prerequisites
- Python 3.10+
- Node.js 18+
- npm
- Git

### 💻 Local Setup Instructions
**Step 1: Open Dual Terminal**  
Use `Ctrl + Shift + 5` in VS Code to open **two terminals side-by-side**.

**Terminal 1: Setup Backend**
```bash
cd backend
pip install -r requirements.txt
```

**Terminal 2: Setup Frontend**
```bash
cd quantum_blockchain
npm install
```

### 🚀 Run the Project
After dependencies are installed:

**Terminal 1 (Backend):**
```bash
python app.py
```

**Terminal 2 (Frontend):**
```bash
npm start
```

Now, the project is fully running on your local machine!

## 📂 Project Structure
```
.
├── backend/                # Python Flask backend (Dilithium integration, blockchain logic)
│   └── app.py              # Entry point for backend server
├── quantum_blockchain/     # React frontend (wallet manager, blockchain UI)
│   └── src/
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## 🔐 Tech Stack
- **Post-Quantum Cryptography**: CRYSTALS-Dilithium (via PQCrypto library)
- **Backend**: Python, Flask
- **Frontend**: React.js, Axios, Framer Motion
- **Blockchain Layer**: Custom Python implementation

## 🧠 Contributors & Credits
Developed as part of a research initiative to explore **quantum-safe blockchain models**.  
Inspired by NIST’s post-quantum standardization project.
