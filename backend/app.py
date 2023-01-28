from datetime import datetime
from time import time_ns

from encryption.hill import Hill
from encryption.vignere import Vignere
from flask import Flask, jsonify, request, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = "static"
ALLOWED_EXTENSION = "txt"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() == ALLOWED_EXTENSION

def write_file(filename, content):
    newfile = filename.split(".")[0] + "_result_" + str(time_ns()) + ".txt"
    with open(f"static/{newfile}", "w") as f:
        f.write(content)

    print(newfile)
    return newfile


# Health check
@app.route("/", methods=["GET"])
def health_check():
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    return jsonify({"Time": now, "Status": "Healthy"})


'''
Vignere decryption or encryption
 Args:
 1. key = cipher key
 2. text = text to encrypt or decrypt
 3. encrypt = set to "True" for encryption, decryption otherwise
 Returns:
 1. Result: decryption/encryption result 
 '''
@app.route("/vignere", methods=["POST"])
def vignere():
    keyToCheck = ["key", "text", "encrypt"]
    data = request.form
    for key in keyToCheck:
        if key not in data.keys():
            return jsonify({"Error": "Invalid request body"})

    key = data["key"]
    text = data["text"]
    encrypt = data["encrypt"] == True

    # Process file
    if "file" in request.files:
        file = request.files["file"]
        if file.filename == "":
            return jsonify({"Error": "Filename cannot be empty"})
        
        if not allowed_file(file.filename):
            return jsonify({"Error": "Only txt files allowed"})
        
        file_content = file.read().decode().strip().upper()
        try:
          cipher = Vignere(key)
          if encrypt:
              result = cipher.encrypt(file_content)
          else:
              result = cipher.decrypt(file_content)
        except Exception as e:
            return jsonify({"Error": "Key or text error"})
        
        newfile = write_file(file.filename, result)
        # open file
        return send_from_directory(UPLOAD_FOLDER, newfile, as_attachment=True)

    try:
        cipher = Vignere(key)
        if encrypt:
            return jsonify({"Result": cipher.encrypt(text)})
        else:
            return jsonify({"Result": cipher.decrypt(text)})
    except Exception as e:
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
