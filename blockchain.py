import hashlib
import datetime



"""
here we try to implement the implementation of a blockchain without any application consideration
"""
string = "pythonpool.com"
encoded = string.encode()
result = hashlib.sha256(encoded)
# le hachage est un processus irreversible on peut prendre une chaine de caracter le hasher pour avoir
# le resultat sous format hexadecimal on saura que le mdp correspond au hash et non l'inverse
# print(result.hexdigest())


class Block:

    def __init__(self, index, data, prehash=''):
        self.index = index
        self.prehash = prehash
        self.timestamp = datetime.datetime.now()
        self.data = data

        def calculatehash():
            return hashlib.sha256((str(self.index) + str(self.prehash) + str(self.timestamp) + str(self.data)).encode()).hexdigest()

        self.hash = calculatehash()


class Blockchain:
    # genesis block block without previous's block hash
    genesis_block = Block(0, "Genesis block")

    def __init__(self):
        self.chain = [self.genesis_block]

    # maintenant pour l'ajout de nouveaux blocks

    def addblock(self, newblock):
        newblock.prehash = self.chain[len(self.chain) - 1].hash
        newblock.hash = newblock.hash
        self.chain.append(newblock)
        print(newblock.hash)
        print(self.chain[len(self.chain) - 1].index)

    # validating the entire chain
    def isvalid(self):
        pass


ndiayecoin = Blockchain()
ndiayecoin.addblock(Block(1, 'salut'))
ndiayecoin.addblock(Block(2, 'blockchain ma passion '))
