students = []

def add_student(name, score):
    students.append({"name": name, "score": score})

def get_top_student():
    if not students:
        return None
    return max(students, key=lambda student: student["score"])

def get_min_student():
    if not students:
        return None
    return min(students, key=lambda student: student["score"])

input_name = input("Masukkan nama siswa: ")
input_score = int(input("Masukkan nilai siswa: "))
input_passing = int(input("Masukkan nilai kelulusan: "))

def is_passing(score):
    return score >= input_passing

add_student(input_name, input_score)
add_student("Bob", 70) 
add_student("Charlie", 90)



# print("Siswa terbaik:", get_top_student())
# print("Siswa terbawah:", get_min_student())
print("Siswa is Passing:", is_passing(input_score))
print("Daftar hasil kelulusan siswa:")
for student in students:
    if is_passing(student["score"]):
        print(f"{student['name']} ({student['score']}) - Lulus")
    else:
        print(f"{student['name']} ({student['score']}) - Tidak Lulus")

# def main():
#     while True:
#         print("\nMenu:")
#         print("1. Tambah Siswa")
#         print("2. Tampilkan Siswa Terbaik")
#         print("3. Tampilkan Siswa Terbawah")
#         print("4. Tampilkan Siswa yang Lulus")
#         print("5. Keluar")
#         pilihan = input("Pilih menu (1-4): ")

#         if pilihan == "1":
#             nama = input("Nama siswa: ")
#             nilai = int(input("Nilai siswa: "))
#             add_student(nama, nilai)
#         elif pilihan == "2":
#             top = get_top_student()
#             if top:
#                 print(f"Siswa terbaik: {top['name']} ({top['score']})")
#             else:
#                 print("Belum ada siswa.")
#         elif pilihan == "3":
#             top = get_min_student()
#             if top:
#                 print(f"Siswa Terbawah: {top['name']} ({top['score']})")
#             else:
#                 print("Belum ada siswa.")
#         elif pilihan == "4":
#             print("Siswa yang lulus:")
#             for s in students:
#                 if is_passing(s["score"]):
#                     print(f"{s['name']} ({s['score']})")
#         elif pilihan == "5":
#             print("Keluar dari program.")
#             break
#         else:
#             print("Pilihan tidak valid.")

# if __name__ == "__main__":
#     main()


# inputNama = input("Masukkan nama siswa: ")
# inputNilai = int(input("Masukkan nilai siswa: "))

# if inputNilai >= 75:
#     print(f"{inputNama} lulus")
# else:
#     print(f"{inputNama} tidak lulus")
    
   