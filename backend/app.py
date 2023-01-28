from datetime import datetime

from encryption.hill import Hill
from encryption.vignere import Vignere
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

# General Setting
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSION = "txt"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Health check
@app.route("/", methods=["GET"])
def health_check():
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    return jsonify({"Time": now, "Status": "Healthy"})


# Vignere decryption or encryption
# Args:
# 1. key = cipher key
# 2. text = text to encrypt or decrypt
# 3. encrypt = set to "True" for encryption, decryption otherwise
# Returns:
# 1. Result: decryption/encryption result
@app.route("/vignere", methods=["POST"])
def vignere():
    keyToCheck = ["key", "text", "encrypt"]
    data = request.form
    for key in keyToCheck:
        if key not in request.form.keys():
            return jsonify({"Error": "Invalid request body"})

    key = data["key"]
    text = data["text"]
    encrypt = data["encrypt"] == True
    if "file" in request.files:
        # process
        pass

    # Sanitize the type file
    if type != "Text" and type != "File":
        return jsonify({"Result": "Invalid type"})

    try:
        cipher = Vignere(key)
        if encrypt:
            if type == "Text":
                return jsonify({"Result": cipher.encrypt(text)})

            return send_from_directory("static", "a.txt", as_attachment=True)
        else:
            return jsonify({"Result": cipher.decrypt(text)})
    except:
        return jsonify({"Error": "Key or text error"})


# Auto-Vignere decryption or encryption
# Args:
# 1. key = cipher key
# 2. text = text to encrypt or decrypt
# 3. encrypt = set to "True" for encryption, decryption otherwise
# Returns:
# 1. Result: decryption/encryption result


@app.route("/auto_vignere", methods=["POST"])
def auto_vignere():
    key = request.form["key"]
    text = request.form["text"]
    encrypt = request.form["encrypt"] == "True"
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


@app.route("/extended_vignere", methods=["POST"])
def extended_vignere():
    key = request.form["key"]
    text = bytes.fromhex(request.form["text"])
    encrypt = request.form["encrypt"] == "True"
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


# Hill cipher decryption or encryption
# Args:
# 1. key = cipher key
# 2. text = text to encrypt or decrypt
# 3. encrypt = set to "True" for encryption, decryption otherwise
# Returns:
# 1. Result: decryption/encryption result


@app.route("/hill", methods=["POST"])
def hill():
    key = request.form["key"]
    text = request.form["text"]
    encrypt = request.form["encrypt"] == "True"
    try:
        cipher = Hill(key)
        if encrypt:
            return jsonify({"Result": cipher.encrypt(text)})
        else:
            return jsonify({"Result": cipher.decrypt(text)})
    except:
        return jsonify({"Error": "Invalid key or text"})


app.run("localhost", port=8000)
