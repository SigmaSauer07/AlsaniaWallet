import hashlib
import json
import time
import random
from ethereum import utils

class Wallet:
    def __init__(self):
        self.private_key = self.generate_private_key()
        self.public_key = self.generate_public_key()
        self.address = self.generate_address()

    def generate_private_key(self):
        """Generate a random private key."""
        return ''.join(random.choices('0123456789abcdef', k=64))

    def generate_public_key(self):
        """Generate the public key from the private key."""
        return utils.privtoaddr(self.private_key)

    def generate_address(self):
        """Generate the wallet address from the public key."""
        return utils.checksum_encode(self.public_key)

    def sign_transaction(self, transaction):
        """Sign a transaction with the wallet's private key."""
        serialized_tx = json.dumps(transaction, sort_keys=True).encode()
        signature = hashlib.sha256(serialized_tx + self.private_key.encode()).hexdigest()
        return signature

    def send_transaction(self, blockchain, recipient, amount):
        """Create and send a transaction to the blockchain."""
        transaction = {
            'sender': self.address,
            'recipient': recipient,
            'amount': amount,
            'timestamp': time.time()
        }
        signature = self.sign_transaction(transaction)
        transaction['signature'] = signature

        # Send the transaction to the blockchain
        blockchain.add_transaction(transaction)

        return transaction
