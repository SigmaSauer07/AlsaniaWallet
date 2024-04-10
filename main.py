from wallet import Wallet
from blockchain import Blockchain

if __name__ == "__main__":
    # Instantiate the blockchain
    full_node = Blockchain()

    # Create a wallet instance
    wallet = Wallet()

    # Specify recipient's address and amount to send
    recipient_address = "Recipient's wallet address"
    amount_to_send = 10  # Amount to send to the recipient

    # Send a transaction
    transaction = wallet.send_transaction(full_node, recipient_address, amount_to_send)
    print("Transaction sent successfully:")
    print(transaction)
