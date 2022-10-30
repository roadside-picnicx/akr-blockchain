import json
import time
from hashlib import sha256

"""I hate this shit, worst thing I ever 'wrote' because I had to follow instructions and write this in fucking online compiler
   I swear to god this was the most painful coding experience of my entire life and i hate python so much
   don't know how this piece of garbage works but it does, kinda
"""

class Block(object):
    @property
    def _hash(self):
        return str(sha256((self.data + self.nonce + self.previousHash + self.timestamp).encode('utf-8')).hexdigest())

    def __init__(self, data: str, previousHash: str):
        self.previousHash : str = previousHash
        self.data :str = data
        self.timestamp : str= str(time.asctime())
        self.nonce: str = ""
        self.hash = self._hash

    def mineBlock(self, difficulty : int = 4):
        init = 0
        start_seq = difficulty*"0"
        while not str(sha256((self.data + str(init) + self.previousHash + self.timestamp).encode('utf-8')).hexdigest()).startswith(start_seq):
            init += 1
        self.nonce = str(init)
        self.hash = self._hash
        return self

    def changeBlock(self):
        self.data = "rozbity string pomoc"
        return self

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)



difficulty = 4
blockchain = []


blockchain.append(Block("Ahoj, ja jsem prvni blok", "0"))
print("Tezim blok 1... ")
blockchain[0].mineBlock(difficulty)
print("Blok vytezen! " + blockchain[0].hash)

blockchain.append(Block("Ja jsem druhy", blockchain[0].hash))
print("Tezim blok 2... ")
blockchain[1].mineBlock(difficulty)
print("Blok vytezen! " + blockchain[1].hash)


blockchain.append(Block("A ja treti", blockchain[1].hash))
print("Tezim blok 3... ")
blockchain[2].mineBlock(difficulty)
print("Blok vytezen! " + blockchain[2].hash)




def isChainValid() -> bool:
    for block in blockchain:
        if str(sha256((block.data + block.nonce + block.previousHash + block.timestamp).encode('utf-8')).hexdigest()) != block.hash:
            return False
    return True
print("Kontrola Blockchainu: " + str(isChainValid()))


genesisBlock = Block("Ja som rpvy blok", "0")
print(blockchain[0].toJSON())

secondBlock = Block("Ja jsem druhy.",genesisBlock.hash)
print(blockchain[1].toJSON())

thirdBlock = Block("A ja treti",secondBlock.hash)
print(blockchain[2].toJSON())

blockchain[1].changeBlock()
print("Kontrola Blockchainu: " + str(isChainValid()))

input()
