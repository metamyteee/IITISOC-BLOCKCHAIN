
import time
import random
from blockchain.chain import Blockchain
from wallet.wallet import QuantumWallet
from transaction.transaction import Transaction, TransactionPool
from crypto.pqcrypto import generate_keys, public_key_to_address

def demonstrate_quantum_crypto():
    """Demonstrate post-quantum cryptography"""
    print("🔐 Quantum-Resistant Cryptography Demo")
    print("=" * 50)
    
    
    public_key, private_key = generate_keys()
    address = public_key_to_address(public_key)
    
    print(f"✅ Generated quantum-resistant key pair")
    print(f"📍 Address: {address}")
    print(f"🔑 Public Key: {public_key[:50]}...")
    print(f"🗝️  Private Key: {private_key[:50]}...")
    
    return public_key, private_key, address

def demonstrate_transactions():
    """Demonstrate transaction creation and signing"""
    print("\n💳 Transaction Demo")
    print("=" * 50)
    
   
    alice_wallet = QuantumWallet("alice")
    bob_wallet = QuantumWallet("bob")
    
   
    alice_addr = alice_wallet.create_new_address("Alice Main")
    bob_addr = bob_wallet.create_new_address("Bob Main")
    
    print(f"👩 Alice address: {alice_addr}")
    print(f"👨 Bob address: {bob_addr}")
    
    
    transaction = alice_wallet.send_transaction(bob_addr, 25.0, alice_addr)
    
    print(f"✅ Transaction created and signed")
    print(f"📄 Transaction ID: {transaction.transaction_id}")
    print(f"💰 Amount: {transaction.amount}")
    print(f"✍️  Signature valid: {transaction.verify_signature()}")
    
    return transaction, alice_addr, bob_addr

def demonstrate_mining():
    """Demonstrate blockchain mining"""
    print("\n⛏️  Mining Demo")
    print("=" * 50)
    
    blockchain = Blockchain()
    miner_wallet = QuantumWallet("miner")
    miner_addr = miner_wallet.create_new_address("Miner")
    
    print(f"⛏️  Miner address: {miner_addr}")
    print(f"📊 Initial chain length: {len(blockchain.chain)}")
    
    
    print("🔨 Mining block... (this may take a moment)")
    start_time = time.time()
    
    block = blockchain.mine_block(miner_addr)
    
    end_time = time.time()
    mining_time = end_time - start_time
    
    print(f"✅ Block mined successfully!")
    print(f"⏱️  Mining time: {mining_time:.2f} seconds")
    print(f"🧱 Block index: {block['index']}")
    print(f"🔗 Block hash: {blockchain.hash(block)[:20]}...")
    print(f"💰 Miner balance: {blockchain.get_balance(miner_addr)}")
    
    return blockchain, miner_addr

def demonstrate_full_blockchain():
    """Demonstrate complete blockchain workflow"""
    print("\n🔗 Complete Blockchain Demo")
    print("=" * 50)
    
    
    blockchain = Blockchain()
    transaction_pool = TransactionPool()
    
    
    alice_wallet = QuantumWallet("demo_alice")
    bob_wallet = QuantumWallet("demo_bob")
    miner_wallet = QuantumWallet("demo_miner")
    
    alice_addr = alice_wallet.create_new_address("Alice")
    bob_addr = bob_wallet.create_new_address("Bob")
    miner_addr = miner_wallet.create_new_address("Miner")
    
    print(f"👥 Created 3 participants:")
    print(f"  👩 Alice: {alice_addr[:20]}...")
    print(f"  👨 Bob: {bob_addr[:20]}...")
    print(f"  ⛏️  Miner: {miner_addr[:20]}...")
    
    
    print("\n🔨 Mining initial blocks for Alice...")
    for i in range(3):
        
        initial_tx = Transaction(
            sender="System",
            recipient=alice_addr,
            amount=100.0
        )
        blockchain.add_transaction(initial_tx.to_dict())
        blockchain.mine_block(miner_addr)
        print(f"  ✅ Block {i+2} mined")
    
    print(f"\n💰 Initial balances:")
    print(f"  Alice: {blockchain.get_balance(alice_addr)}")
    print(f"  Bob: {blockchain.get_balance(bob_addr)}")
    print(f"  Miner: {blockchain.get_balance(miner_addr)}")
    
    
    print("\n💳 Processing transactions...")
    transactions = [
        (alice_addr, bob_addr, 50.0, alice_wallet),
        (alice_addr, bob_addr, 25.0, alice_wallet),
        (bob_addr, alice_addr, 10.0, bob_wallet)  
    ]
    
    for sender_addr, recipient_addr, amount, sender_wallet in transactions:
        try:
            if sender_addr == bob_addr and blockchain.get_balance(bob_addr) < amount:
                print(f"  ❌ Transaction failed: Insufficient balance")
                continue
                
            tx = sender_wallet.send_transaction(recipient_addr, amount, sender_addr)
            blockchain.add_transaction(tx.to_dict())
            print(f"  ✅ Added transaction: {amount} coins")
        except Exception as e:
            print(f"  ❌ Transaction failed: {e}")
    
  
    print(f"\n🔨 Mining block with {len(blockchain.current_transactions)} transactions...")
    block = blockchain.mine_block(miner_addr)
    
    print(f"✅ Block {block['index']} mined with {len(block['transactions'])} transactions")
    
   
    print(f"\n💰 Final balances:")
    print(f"  Alice: {blockchain.get_balance(alice_addr)}")
    print(f"  Bob: {blockchain.get_balance(bob_addr)}")
    print(f"  Miner: {blockchain.get_balance(miner_addr)}")
    
    
    print(f"\n🔍 Blockchain validation: {'✅ Valid' if blockchain.is_chain_valid(blockchain.chain) else '❌ Invalid'}")
    print(f"📊 Total blocks: {len(blockchain.chain)}")
    print(f"🔐 Quantum-resistant: ✅ Yes (Dilithium signatures)")
    
    return blockchain

def interactive_demo():
    """Interactive blockchain demonstration"""
    print("\n🎮 Interactive Quantum Blockchain Demo")
    print("=" * 50)
    
    blockchain = Blockchain()
    wallets = {}
    
    while True:
        print("\n📋 Available Actions:")
        print("1. Create wallet")
        print("2. Check balance")
        print("3. Send transaction")
        print("4. Mine block")
        print("5. View blockchain")
        print("6. Validate chain")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            name = input("Enter wallet name: ")
            wallet = QuantumWallet(f"demo_{name}")
            address = wallet.create_new_address(name)
            wallets[name] = (wallet, address)
            print(f"✅ Created wallet for {name}: {address[:20]}...")
            
        elif choice == '2':
            if not wallets:
                print("❌ No wallets created yet")
                continue
            name = input("Enter wallet name: ")
            if name in wallets:
                _, address = wallets[name]
                balance = blockchain.get_balance(address)
                print(f"💰 {name}'s balance: {balance}")
            else:
                print("❌ Wallet not found")
                
        elif choice == '3':
            if len(wallets) < 2:
                print("❌ Need at least 2 wallets for transactions")
                continue
            
            sender_name = input("Enter sender wallet name: ")
            recipient_name = input("Enter recipient wallet name: ")
            amount = float(input("Enter amount: "))
            
            if sender_name in wallets and recipient_name in wallets:
                sender_wallet, sender_addr = wallets[sender_name]
                _, recipient_addr = wallets[recipient_name]
                
                try:
                    tx = sender_wallet.send_transaction(recipient_addr, amount, sender_addr)
                    blockchain.add_transaction(tx.to_dict())
                    print(f"✅ Transaction added to pool")
                except Exception as e:
                    print(f"❌ Transaction failed: {e}")
            else:
                print("❌ One or both wallets not found")
                
        elif choice == '4':
            if not wallets:
                print("❌ Create a wallet first")
                continue
            
            miner_name = input("Enter miner wallet name: ")
            if miner_name in wallets:
                _, miner_addr = wallets[miner_name]
                print("🔨 Mining... (this may take a moment)")
                block = blockchain.mine_block(miner_addr)
                print(f"✅ Block {block['index']} mined!")
                print(f"💰 Mining reward: {blockchain.mining_reward}")
            else:
                print("❌ Miner wallet not found")
                
        elif choice == '5':
            print(f"\n🔗 Blockchain Overview:")
            print(f"  📊 Total blocks: {len(blockchain.chain)}")
            print(f"  🔄 Pending transactions: {len(blockchain.current_transactions)}")
            
            for i, block in enumerate(blockchain.chain[-3:], len(blockchain.chain)-2):
                if i > 0:  
                    print(f"  🧱 Block {block['index']}: {len(block.get('transactions', []))} transactions")
                    
        elif choice == '6':
            is_valid = blockchain.is_chain_valid(blockchain.chain)
            print(f"🔍 Chain validation: {'✅ Valid' if is_valid else '❌ Invalid'}")
            
        elif choice == '7':
            print("👋 Thanks for using Quantum Blockchain!")
            break
            
        else:
            print("❌ Invalid choice")

def main():
    """Main demonstration function"""
    print("🚀 Quantum-Resistant Blockchain Demonstration")
    print("=" * 60)
    print("This demo showcases a blockchain secured with post-quantum cryptography")
    print("using Dilithium digital signatures to resist quantum computer")
