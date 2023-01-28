import string

from encryption.sanitize import Sanitize


class Vignere:
    def __init__(self, key: str):
        key = Sanitize.sanitize_alphabet(key)
        assert(len(key) > 0)
        self._key = key
    
    def encrypt(self, plaintext: str) -> str:
        # ciphertext will be in uppercase
        charset = string.ascii_uppercase

        # input sanitazion
        text = Sanitize.sanitize_alphabet(plaintext)
        # encryption
        ciphertext = ""
        cur = 0
        for c in text:
            idx = charset.find(c) + charset.find(self._key[cur])
            ciphertext += charset[idx % len(charset)]
            cur = (cur + 1) % len(self._key)
        return ciphertext

    def encrypt_auto(self, plaintext: str) -> str:
        # ciphertext will be in uppercase
        charset = string.ascii_uppercase

        # input sanitazion
        text = Sanitize.sanitize_alphabet(plaintext)

        # encryption
        ciphertext = ""
        cur = 0
        key = "".join(list(self._key))
        key += text
        for c in text:
            idx = charset.find(c) + charset.find(key[cur])
            ciphertext += charset[idx % len(charset)]
            cur = (cur + 1)
        return ciphertext

    def encrypt_extended(self, plaintext: bytes) -> bytes:
        # encryption
        ciphertext = b''
        cur = 0
        key = self._key.encode()
        for c in plaintext:
            val = (key[cur] + c) % 256
            ciphertext += val.to_bytes(1, "little")
            cur = (cur + 1) % len(key)

        return ciphertext
    
    def decrypt(self, ciphertext: str) -> str:
        # plaintext will be in uppercase
        charset = string.ascii_uppercase

        # input sanitazion
        assert(Sanitize.check_alphabet(ciphertext))
        text = Sanitize.remove_whitespace(ciphertext)

        # decryption
        plaintext = ""
        cur = 0
        for c in text:
            idx = charset.find(c) - charset.find(self._key[cur])
            plaintext += charset[idx % len(charset)]
            cur = (cur + 1) % len(self._key)
        return plaintext
    
    def decrypt_auto(self, ciphertext: str) -> string:
        # plaintext will be in uppercase
        charset = string.ascii_uppercase

        # input sanitazion
        assert(Sanitize.check_alphabet(ciphertext))
        text = Sanitize.remove_whitespace(ciphertext)

        # decryption
        plaintext = ""
        cur = 0
        key = "".join(list(self._key))
        for c in text:
            idx = charset.find(c) - charset.find(key[cur])
            plaintext += charset[idx % len(charset)]
            key += (plaintext[-1])
            cur = (cur + 1)
        return plaintext

    def decrypt_extended(self, ciphertext: bytes) -> bytes:
        # decryption
        plaintext = b""
        cur = 0
        key = self._key.encode()
        for c in ciphertext:
            val = (c - key[cur]) % 256
            plaintext += val.to_bytes(1, "little")
            cur = (cur + 1) % len(key)

        return plaintext
