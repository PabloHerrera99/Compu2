"""

Partes de código extraidas de: 

https://github.com/satwikkansal/python_blockchain_app

"""


from hashlib import sha256
import json
import os, signal

r,w = os.pipe()

class NoBlock:

    def __init__(self, seed, nonce=0):
        self.seed = seed
        self.nonce = nonce



    def compute_hash(self):

        """
        A function that return the hash of the block contents.
        """

        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest() #Devuelve el hash del bloque



def proof_of_work(block):

    """
    Function that tries different values of nonce to get a hash
    that satisfies our difficulty criteria.
    """

    difficulty = 3


    computed_hash = block.compute_hash()
    while not computed_hash.startswith('0' * difficulty):

        block.nonce += 1
        computed_hash = block.compute_hash()


    return computed_hash, block.nonce


def handle_signal(signum):
    print(f' Señal {signum} resibida')

    os.close(w)
    nonce = os.read(r, 1024)
    print(nonce.decode())
    exit()

signal.signal(signal.SIGUSR1, handle_signal)

for i in range(2):
    pid = os.fork()
    if pid == 0:
        print(f'{os.getpid()} hijo de {os.getppid()}')

        b = NoBlock(seed='La semilla que quiera', nonce=0)
        h = b.compute_hash()
        new_hash = proof_of_work(b)
        nonce = new_hash[1]
        nonce_str = str(nonce)

        os.kill(os.getppid(), signal.SIGUSR1)
        data = f'El nonce encontrado es: {nonce_str}\nLo encontro: {os.getpid()}'

        try:
            os.close(r)
            os.write(w, data.encode())
            os.close(w)
        except BrokenPipeError:
            print(f'Soy {os.getpid()}, llegue tarde :(')

        exit()
        

"""
os.ppid() # obtiene el pid del padre
os.kill(<señal>, <pid>)
"""