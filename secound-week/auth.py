# File: login_register.py

def load_users():
    users = {}
    try:
        with open("users.txt", "r") as file:
            for line in file:
                if ":" in line:
                    username, password = line.strip().split(":")
                    users[username] = password
    except FileNotFoundError:
        pass  # kalau file belum ada, abaikan
    return users

def save_user(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username}:{password}\n")

def register():
    users = load_users()
    username = input("Buat username baru: ")
    if username in users:
        print("Username sudah digunakan. Coba yang lain.")
        return
    password = input("Buat password: ")
    save_user(username, password)
    print("Registrasi berhasil!")

def login():
    users = load_users()
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username] == password:
        print("Login berhasil! Selamat datang,", username)
    else:
        print("Username atau password salah.")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")
        pilihan = input("Pilih opsi: ")
        if pilihan == "1":
            register()
        elif pilihan == "2":
            login()
        elif pilihan == "3":
            print("Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")

# Jalankan program
menu()
