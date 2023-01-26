import string

class Sanitize:
    def __init__():
        pass

    @staticmethod
    def remove_whitespace(text):
        return "".join(text.split())

    @staticmethod
    def sanitize_alphabet(plaintext):
        plaintext = Sanitize.remove_whitespace(plaintext)
        ret = ""
        accept = string.ascii_letters
        for c in plaintext:
            if c in accept:
                ret += c.upper()
        return ret
    
    @staticmethod
    def check_alphabet(ciphertext):
        ciphertext = Sanitize.remove_whitespace(ciphertext)
        accept = string.ascii_uppercase
        for c in ciphertext:
            if c not in accept:
                return False
        return True