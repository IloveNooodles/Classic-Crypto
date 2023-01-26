import string
from encryption.sanitize import Sanitize

class Hill:
    def __init__(self, key: str, size: int):
        key = Sanitize.sanitize_alphabet(key)
        assert(len(key) == size * size)
        self._charset = string.ascii_uppercase
        self._key = [[0 for _ in range(size)] for _ in range(size)]
        self._size = size
        for i in range(len(key)):
            self._key[i//size][i%size] = self._charset.find(key[i])
        
    def encrypt(self, plaintext: str) -> str:
        # input sanitazion
        text = Sanitize.sanitize_alphabet(plaintext)

        # encryption
        ciphertext = ""