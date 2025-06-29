# IITISOC Blockchain Project

Welcome to the **IITISOC Blockchain** repository! 🚀  
This project is built for the IIT Indore Summer of Code (IITISOC) and is a lightweight prototype of a blockchain system using Python.

## 🧠 Problem Statement

Design and implement a simple yet functional blockchain system in Python.  
The goal is to help contributors understand the inner workings of blockchains such as:

- Block & chain structures
- Transaction validation
- Digital signatures (using PQCrypto - Dilithium)
- Wallet management

## 📁 Project Structure

IITISOC-BLOCKCHAIN/
 │
 ├── blockchain/ # Blockchain logic (blocks, chain)
 ├── crypto/ # Digital signature (Dilithium PQCrypto)
 ├── tests/ # Unit tests
 ├── transaction/ # Transaction logic
 ├── wallet/ # Wallet functionality
 ├── run.py # App entry point
 ├── requirement.txt # Python dependencies
 └── README.md # This file


## 🚀 Getting Started

### 1. Fork This Repo

Click the **Fork** button (top right of this page) to make a personal copy of this repository under your GitHub account.

### 2. Clone Your Fork

form welcome oage in vs code.

python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

pip install -r requirement.txt
### if any missing repo or basic repo , just install it as per that.

### 3. to run tests to ensure no issue is there while intergartion of the code
run this command in vs codes terminal 
pytest -v

### 4. now make the changes , and push the solution to your forked repo 

### 5. then just make a pr on main repo 
