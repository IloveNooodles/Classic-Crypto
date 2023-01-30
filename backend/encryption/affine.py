import string

from encryption.sanitize import Sanitize

'''
X is the character
cipher = (mX + b) mod N
plain = m^-1 (C - b) mod N

N = 26

choose a that have gcd(m, N) = 1
'''
LEN_ALPHABET = 26

class Affine:
    def _gcd(self, m: int, N: int = 26):
        if(m == 0): return N 
        return self._gcd(N % m, m)
    
    def _egcd(self, a: int, b:int ):
      if a == 0:
        return (b, 0, 1)
      else:
          g, y, x = self._egcd(b % a, a)
          return (g, x - (b // a) * y, y)

    def _modinv(self, a: int, m: int):
        g, x, y = self._egcd(a, m)
        if g != 1:
            raise Exception("Mod inverse doesn't exists")
        else:
            return x % m

    def __init__(self, m: int, b: int):
        self.m = m
        self.b = b
        assert(self._gcd(m, LEN_ALPHABET) == 1)
    
    def encrypt(self, plaintext: string):
        # sanitize input
        text = Sanitize.sanitize_alphabet(plaintext)
        charset = string.ascii_uppercase
        ciphertext = ""
        for c in text:
            idx = self.m * charset.find(c) + self.b
            ciphertext += charset[idx % LEN_ALPHABET]
        
        return ciphertext
    
    def decrypt(self, ciphertext: string):
        # Sanitize input
        assert(Sanitize.check_alphabet(ciphertext))
        text = Sanitize.remove_whitespace(ciphertext)
        charset = string.ascii_uppercase
        plaintext = ""
        for c in text:
            idx = self._modinv(self.m, LEN_ALPHABET) * (charset.find(c) - self.b)
            plaintext += charset[idx % LEN_ALPHABET]
        return plaintext
      

if __name__ == "__main__":
    affine = Affine(3, 10)
    print(affine.encrypt("HALO GAEES GARE DISINI"))
    print(affine.decrpyt("FKRACKWWMCKJWTIMIXI"))