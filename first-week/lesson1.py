# List
print("# List")
buah = ["apel", "jeruk", "mangga"]
buah.append("pisang")
buah.append("kacang")
print(buah[4])  # jeruk

# Dictionary
print("# Dictionary")
user = {
    "nama": "Anam",
    "usia": 25,
    "aktif": True
}
print(user["usia"])


# Contoh function
def sapa(nama):
    print(f"Halo, {nama}!")

sapa("Anam")

# Contoh inputan
# nama = input("Siapa namamu? ")
# print("Halo", nama)


# Latihan Kecil buat inputan nama sama umur

# nama = input("Siapa namamu? ")
# umur = input("Berapa Umurmu")

# print("hallo", nama, "dan Umurku" , umur , "tahun")

# ini lebih modern 

nama = input("Siapa namamu? ")
umur = input("Berapa umurmu? ")

print(f"Halo {nama}, umurku {umur} tahun")
