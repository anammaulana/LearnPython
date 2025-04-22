
inputUser = input("Masukkan nama: ")
try:
    umur = int(inputUser)
except ValueError:
    print(inputUser, "Bukan angka, Umur harus berupa angka.")
    exit()
if umur <= 6:
    print("Kamu bocil banget.")
elif umur <= 15:
    print("Kamu Remaja.")
else:
    print("Kamu Wong tuek")
