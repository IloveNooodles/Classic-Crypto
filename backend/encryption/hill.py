import string
import numpy as np
import math
from encryption.sanitize import Sanitize

class Hill:
    def __init__(self, key: str):
        key = Sanitize.sanitize_alphabet(key)
        size = round(math.sqrt(key))
        assert(size*size == key)
        self._charset = string.ascii_uppercase
        self._key = np.zeros(shape=(size,size))
        self._size = size
        for i in range(len(key)):
            self._key[i//size, i%size] = self._charset.find(key[i])
        self._inv_key = self._mod_inv(self._key)

    def _mod_matmul(self, a, b, m=26):
        c = np.matmul(a, b)
        return np.fromiter(map(lambda x: round(x)%m, c), dtype=np.int32)

    def _minor(self, arr, i, j):
        # ith row, jth column removed
        return arr[np.array(list(range(i))+list(range(i+1,arr.shape[0])))[:,np.newaxis],
                np.array(list(range(j))+list(range(j+1,arr.shape[1])))]


    def _mod_inv(self, a, m=26):
        assert(a.shape[0] == a.shape[1])
        c = np.zeros(a.shape)
        invdet = pow(round(np.linalg.det(a)), -1, m)
        for i in range(a.shape[0]):
            for j in range(a.shape[1]):
                c[i, j] = (pow(-1, (i+j)) * np.linalg.det(self._minor(a, i, j))) % 26
                c[i, j] = (c[i, j] * invdet) % 26
        return np.matrix.transpose(c)
        
    def encrypt(self, plaintext: str) -> str:
        # input sanitazion
        text = Sanitize.sanitize_alphabet(plaintext)

        # encryption
        ciphertext = ""
        for i in range(0, len(text), self._size):
            cur = [23 for _ in range(self._size)]
            for j in range(i, min(len(text), i+self._size)):
                cur[j-i] = self._charset.find(text[j])
            enc = self._mod_matmul(self._key, cur)
            for c in enc:
                ciphertext += self._charset[c]
        
        return ciphertext
    
    def decrypt(self, ciphertext: str) -> str:
        # input sanitazion
        assert(Sanitize.check_alphabet(ciphertext))
        text = Sanitize.remove_whitespace(ciphertext)
        assert(len(ciphertext) % self._size == 0)

        # decryption
        plaintext =  ""
        for i in range(0, len(text), self._size):
            cur = [0 for _ in range(self._size)]
            for j in range(i, min(len(text), i+self._size)):
                cur[j-i] = self._charset.find(text[j])
            enc = self._mod_matmul(self._inv_key, cur)
            for c in enc:
                plaintext += self._charset[c]
        
        return plaintext