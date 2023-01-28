import string
from encryption.sanitize import Sanitize

class Playfair:
    def __init__(self, key: str):
        self._charset = string.ascii_uppercase

        key = Sanitize.sanitize_alphabet(key)
        self._key = self._construct_key(key)
    
    def _construct_key(self, key: str) -> list:
        key = key.replace("J", "I")
        key = key + self._charset
        new_key = ""
        for c in key:
            if c not in new_key and c != 'J':
                new_key += c

        assert(len(new_key) == len(self._charset) - 1)
        table = [[0 for _ in range(5)] for _ in range(5)]

        for i in range(len(new_key)):
            table[i//5][i%5] = new_key[i]
        
        return table