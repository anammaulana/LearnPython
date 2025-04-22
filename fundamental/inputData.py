nama = input("Siapa namamu? ")
print("Halo,", nama)
print("Selamat datang di program Python ini.")
print("Kami akan melakukan beberapa operasi matematika sederhana.")
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
print("Hasil penjumlahan:", angka1 + angka2)
print("Hasil pengurangan:", angka1 - angka2)
print("Hasil perkalian:", angka1 * angka2)
if angka2 != 0:
    print("Hasil pembagian:", angka1 / angka2)
else:
    print("Pembagian tidak dapat dilakukan karena pembagi adalah nol.")
