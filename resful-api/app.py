from flask import Flask, request, jsonify

app = Flask(__name__)
USER_FILE = "users.txt"

def load_users():
    users = {}
    try:
        with open(USER_FILE, "r") as f:
            for line in f:
                if ":" in line:
                    username, password = line.strip().split(":")
                    users[username] = password
    except FileNotFoundError:
        pass
    return users

def save_user(username, password):
    with open(USER_FILE, "a") as f:
        f.write(f"{username}:{password}\n")

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"success": False, "message": "Username dan password harus diisi!"}), 400

    users = load_users()
    if username in users:
        return jsonify({"success": False, "message": "Username sudah digunakan"}), 409

    save_user(username, password)
    return jsonify({"success": True, "message": "Registrasi berhasil"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    users = load_users()
    if username in users and users[username] == password:
        return jsonify({"success": True, "message": "Login berhasil"}), 200
    else:
        return jsonify({"success": False, "message": "Username atau password salah"}), 401

if __name__ == "__main__":
    app.run(debug=True)
