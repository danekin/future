from hashlib import sha256
import json
import time


class Chain:

    def __init__(self) -> None:
        self.blockchain = []
        self.pending = []
        
        self.add_block(prevhash='Genesis', proof=123)

    def add_transaction(self, sender, receipent, amount):
        self.pending.append({
            'sender': sender,
            'receipent': receipent,
            'amount': amount,
        })

    def compute_hash(self, block):
        json_block = json.dumps(block, sort_keys=True).encode()

        curhash = sha256(json_block).hexdigest()

        return curhash

    def add_block(self, proof, prevhash=None)