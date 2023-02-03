import string

from encryption.sanitize import Sanitize


class Playfair:
    def __init__(self, key: str):
        self._charset = string.ascii_uppercase

        key = Sanitize.sanitize_alphabet(key)
        self._key = self._construct_key(key)
        self._inverse_key = {}
        for i in range(5):
            for j in range(5):
                self._inverse_key[self._key[i][j]] = (i, j)
        
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

    def encrypt(self, plaintext: str) -> str:
        # Sanitazion
        text = Sanitize.sanitize_alphabet(plaintext)
        text = text.replace("J", "I")

        # Padding
        padded_text = "" + text[0]
        for i in range(1, len(text)):
            if len(padded_text) % 2 == 1 and padded_text[-1] == text[i]:
                padded_text += "X"
            padded_text += text[i]
        
        if len(padded_text) % 2:
            padded_text += "X"
        
        # Encryption
        ciphertext = ""
        for i in range(0, len(padded_text), 2):
            a = padded_text[i]
            b = padded_text[i+1]
            assert(a != b)
            ai, aj = self._inverse_key[a]
            bi, bj = self._inverse_key[b]

            if ai==bi:
                ciphertext += self._key[ai][(aj+1) % 5]
                ciphertext += self._key[bi][(bj+1) % 5]
            elif aj==bj:
                ciphertext += self._key[(ai+1) % 5][aj]
                ciphertext += self._key[(bi+1) % 5][bj]
            else:
                ciphertext += self._key[ai][bj]
                ciphertext += self._key[bi][aj]
            
        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        # Sanitazion check
        assert(Sanitize.check_alphabet(ciphertext))
        text = Sanitize.remove_whitespace(ciphertext)
        assert("J" not in text)

        # Padding check
        assert(len(text)%2 == 0)
        for i in range(len(text), 2):
            assert(text[i] != text[i+1])
        
        # Decryption
        plaintext = ""
        for i in range(0, len(text), 2):
            a = text[i]
            b = text[i+1]
            assert(a != b)
            ai, aj = self._inverse_key[a]
            bi, bj = self._inverse_key[b]

            if ai==bi:
                plaintext += self._key[ai][(aj-1) % 5]
                plaintext += self._key[bi][(bj-1) % 5]
            elif aj==bj:
                plaintext += self._key[(ai-1) % 5][aj]
                plaintext += self._key[(bi-1) % 5][bj]
            else:
                plaintext += self._key[ai][bj]
                plaintext += self._key[bi][aj]
        
        return plaintext
