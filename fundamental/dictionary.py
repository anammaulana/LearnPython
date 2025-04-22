# indexInput = input("Masukkan index: ")
# keyInput = input("Masukkan key: ")
# valueInput = input("Masukkan value: ")
# mahasiswa = {
#     "nama": "Anam",
#     "umur": 20,
#     "jurusan": "Informatika"
# }
# #  mahasiswa.append("alamat", "Jakarta") dilarang karena append tidak ada di dictionary
# # mahasiswa["alamat"] = "Jakarta" # cara menambah data ke dictionary
# mahasiswa[keyInput] = valueInput
# # print(mahasiswa) # menampilkan semua data di dictionary
# print(mahasiswa[indexInput])


mahasiswa = {
    "nama": "Anam",
    "umur": 20,
    "jurusan": "Informatika"
}

keyInput = input("Masukkan key baru: ")
valueInput = input("Masukkan value: ")
mahasiswa[keyInput] = valueInput

keys = list(mahasiswa.keys())
values = list(mahasiswa.values())

print("\nList data mahasiswa:")
for i in range(len(keys)):
    print(f"{i}. {keys[i]}: {values[i]}")

indexInput = int(input("\nMasukkan index untuk ditampilkan: "))
print(f"Data yang dipilih: {keys[indexInput]} = {values[indexInput]}")
