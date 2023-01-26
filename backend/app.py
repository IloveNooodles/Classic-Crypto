from flask import Flask, request, jsonify
from encryption.vignere import Vignere
app = Flask(__name__)

# Vignere decryption or encryption
# Args:
# 1. key = cipher key
# 2. text = text to encrypt or decrypt
# 3. encrypt = set to "True" for encryption, decryption otherwise
# Returns:
# 1. Result: decryption/encryption result

@app.route("/vignere", methods = ['POST'])
def vignere():
    key = request.form['key']
    text = request.form['text']
    encrypt = request.form['encrypt'] == "True"
    try:
        cipher = Vignere(key)
        if encrypt:
            return jsonify({"Result": cipher.encrypt(text)})
        else:
            return jsonify({"Result": cipher.decrypt(text)})
    except:
        return jsonify({"Error": "Invalid key or text"})

# Auto-Vignere decryption or encryption
# Args:
# 1. key = cipher key
# 2. text = text to encrypt or decrypt
# 3. encrypt = set to "True" for encryption, decryption otherwise
# Returns:
# 1. Result: decryption/encryption result

@app.route("/auto_vignere", methods = ['POST'])
def auto_vignere():
    key = request.form['key']
    text = request.form['text']
    encrypt = request.form['encrypt'] == "True"
    try:
        cipher = Vignere(key)
        if encrypt:
            return jsonify({"Result": cipher.encrypt_auto(text)})
        else:
            return jsonify({"Result": cipher.decrypt_auto(text)})
    except:
        return jsonify({"Error": "Invalid key or text"})


# Auto-Vignere decryption or encryption
# Args:
# 1. key = cipher key
# 2. text = text to encrypt or decrypt, in hex
# 3. encrypt = set to "True" for encryption, decryption otherwise
# Returns:
# 1. Result: decryption/encryption result, in hex

@app.route("/extended_vignere", methods = ['POST'])
def extended_vignere():
    key = request.form['key']
    text = bytes.fromhex(request.form['text'])
    encrypt = request.form['encrypt'] == "True"
    try:
        cipher = Vignere(key)
        if encrypt:
            return jsonify({"Result": cipher.encrypt_extended(text).hex()})
        else:
            return jsonify({"Result": cipher.decrypt_extended(text).hex()})
    except:
        return jsonify({"Error": "Invalid key or text"})


@app.route("/affine")
def affine():
    return "Hello World!"

@app.route("/playfair")
def playfair():
    return "Hello World!"

@app.route("/hill")
def hill():
    return "Hello World!"

app.run("localhost", port=8000)