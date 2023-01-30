from datetime import datetime
from time import time_ns

from encryption.affine import Affine
from encryption.hill import Hill
from encryption.playfair import Playfair
from encryption.vignere import Vignere
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "static"
ALLOWED_EXTENSION = "txt"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def get_file_extension(filename: str):
    return filename.rsplit('.', 1)[1].lower()

def allowed_file(filename: str):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() == ALLOWED_EXTENSION

def write_file(filename, content):
    newfile = filename.split(".")[0] + "_result_" + str(time_ns()) + get_file_extension(filename)
    if type(content) is str:
        with open(f"static/{newfile}", "w+") as f:
            f.write(content)
    else:
        with open(f"static/{newfile}", "wb+") as f:
            f.write(content)

    return newfile

def make_response(result, message="Cipher successful", type = "text"):
    return jsonify({"result":result, "message": message, "type": type})

def make_error(message, result="", type="error"):
    return jsonify({"result":result, "message": message, "type": type})


def check_request(data):
    keyToCheck = ["key", "encrypt"]
    for key in keyToCheck:
        if key not in data.keys():
            return False
    return True

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
    data = request.form
    if not check_request(data):
        return make_error("Invalid request body")

    key = data["key"]
    encrypt = data["encrypt"].upper() == "True".upper()

    # Process file
    if "file" in request.files:
        file = request.files["file"]
        if file.filename == "":
            return make_error("Filename cannot be empty")
        
        if not allowed_file(file.filename):
            return make_error("Only txt files allowed")
        
        file_content = file.read().decode().strip().upper()
        try:
          cipher = Vignere(key)
          if encrypt:
              result = cipher.encrypt(file_content)
          else:
              result = cipher.decrypt(file_content)
        except Exception as e:
            return make_error("Key or text error")
        
        newfile = write_file(file.filename, result)
        # open file
        return send_from_directory(UPLOAD_FOLDER, newfile, as_attachment=True)
    elif "text" in data:
        text = data['text']
        try:
            cipher = Vignere(key)
            if encrypt:
                return make_response(cipher.encrypt(text))
            else:
                return make_response(cipher.decrypt(text))
        except Exception as e:
            return make_error("Key or text error")
    else:
        return make_error("Invalid request body")

# Auto-Vignere decryption or encryption
# Args:
# 1. key = cipher key
# 2. text = text to encrypt or decrypt
# 3. encrypt = set to "True" for encryption, decryption otherwise
# Returns:
# 1. Result: decryption/encryption result
@app.route("/auto_vignere", methods=["POST"])
def auto_vignere():
    data = request.form
    print(data)
    if not check_request(data):
        return make_error("Invalid request body")

    key = data["key"]
    encrypt = data["encrypt"].upper() == "True".upper()

    # Process file
    if "file" in request.files:
        file = request.files["file"]
        if file.filename == "":
            return make_error("Filename cannot be empty")
        
        if not allowed_file(file.filename):
            return make_error("Only txt files allowed")
        
        file_content = file.read().decode().strip().upper()
        try:
          cipher = Vignere(key)
          if encrypt:
              result = cipher.encrypt_auto(file_content)
          else:
              result = cipher.decrypt_auto(file_content)
        except Exception as e:
            return make_error("Key or text error")
        
        newfile = write_file(file.filename, result)
        # open file
        return send_from_directory(UPLOAD_FOLDER, newfile, as_attachment=True)
    elif "text" in data:
        text = data['text']
        try:
            cipher = Vignere(key)
            if encrypt:
                return make_response(cipher.encrypt_auto(text))
            else:
                return make_response(cipher.decrypt_auto(text))
        except:
            return make_error("Key or text error")
    else:
        return make_error("Invalid request body")


# Extended-Vignere decryption or encryption
# Args:
# 1. key = cipher key
# 2. text = text to encrypt or decrypt, in hex
# 3. encrypt = set to "True" for encryption, decryption otherwise
# Returns:
# 1. Result: decryption/encryption result, in hex


@app.route("/extended_vignere", methods=["POST"])
def extended_vignere():
    data = request.form
    if not check_request(data):
        return make_error("Invalid request body")
    
    key = request.form["key"]
    encrypt = request.form["encrypt"] == "True"
    # Process file
    if "file" in request.files:
        file = request.files["file"]
        if file.filename == "":
            return make_error("Filename cannot be empty")
        
        file_content = file.read()
        try:
          cipher = Vignere(key)
          if encrypt:
              result = cipher.encrypt_extended(file_content)
          else:
              result = cipher.decrypt_extended(file_content)
        except Exception as e:
            return make_error("Key or text error")
        
        newfile = write_file(file.filename, result)
        # open file
        return send_from_directory(UPLOAD_FOLDER, newfile, as_attachment=True)
    elif "text" in data:
        text = bytes.fromhex(request.form["text"])
        try:
            cipher = Vignere(key)
            if encrypt:
                return jsonify({"Result": cipher.encrypt_extended(text).hex()})
            else:
                return jsonify({"Result": cipher.decrypt_extended(text).hex()})
        except:
            return make_error("Key or text error")
    else:
        return make_error("Invalid request body")

''' 
Hill cipher decryption or encryption
Args:
1. m = cipher multiplicative
2. b = cipher additive
3. text = text to encrypt or decrypt
4. encrypt = set to "True" for encryption, decryption otherwise
Returns:@app.route("/affine", methods=["POSDT
1. Result: decryption/encryption result 
'''
@app.route("/affine", methods=["POST"])
def affine():
    keyToCheck = ["m", "b", "encrypt"]
    data = request.form
    for key in keyToCheck:
        if key not in data.keys():
            return make_error("Invalid request body")

    m = int(data["m"])
    b = int(data["b"])
    encrypt = data["encrypt"].upper() == "True".upper()

    # Process file
    if "file" in request.files:
        file = request.files["file"]
        if file.filename == "":
            return make_error("Filename cannot be empty")
        
        if not allowed_file(file.filename):
            return make_error("Only txt files allowed")
        
        file_content = file.read().decode().strip().upper()
        try:
          cipher = Affine(m, b)
          if encrypt:
              result = cipher.encrypt(file_content)
          else:
              result = cipher.decrypt(file_content)
        except Exception as e:
            return make_error("Key is possibly doesn't coprime with 26 or text error")
        
        newfile = write_file(file.filename, result)
        # open file
        return send_from_directory(UPLOAD_FOLDER, newfile, as_attachment=True)
    
    if "text" not in data.keys():
        return make_error("Invalid request body")

    # Process text
    text = data["text"]

    try:
        cipher = Affine(m, b)
        if encrypt:
            return make_response(cipher.encrypt(text))
        else:
            return make_response(cipher.decrypt(text))
    except Exception as e:
        return make_error("Key or text error")


# Playfair cipher decryption or encryption
# Args:
# 1. key = cipher key
# 2. text = text to encrypt or decrypt
# 3. encrypt = set to "True" for encryption, decryption otherwise
# Returns:
# 1. Result: decryption/encryption result
@app.route("/playfair", methods=["POST"])
def playfair():
    data = request.form
    if not check_request(data):
        return make_error("Invalid request body")

    key = data["key"]
    encrypt = data["encrypt"].upper() == "True".upper()
    # Process file
    if "file" in request.files:
        file = request.files["file"]
        if file.filename == "":
            return make_error("Filename cannot be empty")
        
        if not allowed_file(file.filename):
            return make_error("Only txt files allowed")
        
        file_content = file.read().decode().strip().upper()
        try:
          cipher = Playfair(key)
          if encrypt:
              result = cipher.encrypt(file_content)
          else:
              result = cipher.decrypt(file_content)
        except Exception as e:
            return make_error("Key or text error")
        
        newfile = write_file(file.filename, result)
        # open file
        return send_from_directory(UPLOAD_FOLDER, newfile, as_attachment=True)
    elif "text" in data:
        try:
            cipher = Playfair(key)
            if encrypt:
                return make_response(cipher.encrypt(text))
            else:
                return make_response(cipher.decrypt(text))
        except:
            return make_error("Key or text error")
    else:
        return make_error("Invalid request body")


# Hill cipher decryption or encryption
# Args:
# 1. key = cipher key
# 2. text = text to encrypt or decrypt
# 3. encrypt = set to "True" for encryption, decryption otherwise
# Returns:
# 1. Result: decryption/encryption result


@app.route("/hill", methods=["POST"])
def hill():
    data = request.form
    if not check_request(data):
        return make_error("Invalid request body")

    key = data["key"]
    encrypt = data["encrypt"].upper() == "True".upper()
    # Process file
    if "file" in request.files:
        file = request.files["file"]
        if file.filename == "":
            return make_error("Filename cannot be empty")
        
        if not allowed_file(file.filename):
            return make_error("Only txt files allowed")
        
        file_content = file.read().decode().strip().upper()
        try:
          cipher = Hill(key)
          if encrypt:
              result = cipher.encrypt(file_content)
          else:
              result = cipher.decrypt(file_content)
        except Exception as e:
            return make_error("Key or text error")
        
        newfile = write_file(file.filename, result)
        # open file
        return send_from_directory(UPLOAD_FOLDER, newfile, as_attachment=True)
    elif "text" in data:
        try:
            cipher = Hill(key)
            if encrypt:
                return make_response(cipher.encrypt(text))
            else:
                return make_response(cipher.decrypt(text))
        except:
            return make_error("Key or text error")
    else:
        return make_error("Invalid request body")


app.run("localhost", port=8000)
