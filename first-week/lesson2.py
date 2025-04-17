angka = [3, 1, 4, 2]

# Loop
for a in angka:
    print(a)

# Sort
angka.sort()
print("Urut:", angka)

# Slicing
print("2 elemen pertama:", angka[:4])


#Tuple
data = (1, 2, 3)
print("data :",data)
print("data yang di ambil dari array",data[2])

#Mengakses elemen ketiga dari tuple (index ke-2, karena index mulai dari 0), yaitu 3.
#Catatan: Tuple mirip seperti list, tapi isinya tidak bisa diubah (immutable).

#Set
unik = {1, 2, 2, 3}
print(unik)  # Hasil: {1, 2, 3}


#String Manupulation
teks = "Belajar Python itu keren"

print("1. Kapital semua :",teks.upper())      # Kapital semua
print("2. Huruf kecil semua :",teks.lower())      # Huruf kecil semua
print("3. Replace keren to asyik :",teks.replace("keren", "asyik"))
print("4. Pecah jadi list :",teks.split())      # Pecah jadi list

# 🟢 4. Fungsi Lanjutan
# Parameter default, return value.
def salam(nama="teman"):
    return f"Halo {nama}, selamat datang!"

print(salam("Anam"))
print(salam())

# 🟢 5. Loop dalam List (List Comprehension)
# Lebih singkat dan efisien:
# Buat list kuadrat dari 1 sampai 5
kuadrat = [x**2 for x in range(1, 6)]
print(kuadrat)


# 🟢 6. Error Handling (try-except)
# Supaya program gak berhenti kalau error.
try:
    angka = int(input("Masukkan angka: "))
    print("Dikali 2 =", angka * 2)
except ValueError:
    print("Bukan angka bro!")
    
    
# Latihan mini project
# try:
#     inputAngka = int(input("Masukkan angka = "))
#     if inputAngka % 2 == 0:
#         print("Angka ini genap")
#     else:
#         print("Angka ini ganjil")
# except ValueError :
#     print( "ini bukan angka bro")
    
    inputUser = input("Masukkan angka = ")
try:
    inputAngka = int(inputUser)
    if inputAngka % 2 == 0:
        print("Angka ini genap")
    else:
        print("Angka ini ganjil")
except ValueError:
    print(inputUser, "bukan angka bro!")

    
# Penjelasan singkat:
# int(input(...)) → meminta input dari user dan mengubahnya ke int.

# inputAngka % 2 == 0 → jika habis dibagi 2, berarti genap.

# Selain itu berarti ganjil.
    

