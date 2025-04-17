kontak = [
    # {"nama": "Budi", "nomor": "0812345678"},
    # {"nama": "Ani", "nomor": "0898765432"}
]
def muat_kontak_dari_file(nama_file="daftar_kontak.txt"):
    try:
        with open(nama_file, "r") as file:
            lines = file.readlines()
            for line in lines:
                if "-" in line:
                    nama, nomor = line.strip().split(" - ")
                    kontak.append({"nama": nama, "nomor": int(nomor)})
        print(f"Kontak berhasil dimuat dari file '{nama_file}'\n")
    except FileNotFoundError:
        print(f"File '{nama_file}' belum ada. Kontak akan dimulai dari kosong.\n")
    except ValueError:
        print("Format data di file tidak sesuai. Beberapa kontak mungkin tidak dimuat.")
        
def tambah_kontak():
    try:
        inputName = input("Masukkan nama = ").strip()
        if not inputName:
            print("Nama tidak boleh kosong!\n")
            return
        
        inputNo = input("Masukkan nomor = ").strip()
        if not inputNo:
            print("Nomor tidak boleh kosong!\n")
            return

        nama = str(inputName)
        nomor = int(inputNo)  # Akan error kalau bukan angka

        kontak.append({"nama": nama, "nomor": nomor})
        print("Kontak berhasil ditambahkan!\n")

    except ValueError:
        print("Nomor harus berupa angka!\n")

def lihat_kontak():
    if not kontak:
        print("Belum ada kontak.")
        return
    print("\nDaftar Kontak:")
    for idx, k in enumerate(kontak):
        print(f"{idx+1}. {k['nama']} - {k['nomor']}")
    print()

def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus: ")
    for k in kontak:
        if k["nama"].lower() == nama.lower():
            kontak.remove(k)
            print("Kontak berhasil dihapus!\n")
            return
    print("Kontak tidak ditemukan.\n")

def cari_kontak():
    keyword = input("Cari nama kontak: ").strip().lower()
    if not keyword:
        print("Input pencarian tidak boleh kosong!\n")
        return
    
    ditemukan = False
    for k in kontak:
        if keyword in k["nama"].lower():
            print(f"Nama: {k['nama']}, Nomor: {k['nomor']}")
            ditemukan = True
    
    if not ditemukan:
        print("Kontak tidak ditemukan.\n")

def edit_kontak():
    nama_lama = input("Masukkan nama kontak yang ingin diedit: ").strip()
    if not nama_lama:
        print("Nama tidak boleh kosong!\n")
        return

    for k in kontak:
        if k["nama"].lower() == nama_lama.lower():
            nama_baru = input("Masukkan nama baru (tekan enter jika tidak ingin mengubah): ").strip()
            nomor_baru = input("Masukkan nomor baru (tekan enter jika tidak ingin mengubah): ").strip()

            if nama_baru:
                k["nama"] = nama_baru
            if nomor_baru:
                try:
                    k["nomor"] = int(nomor_baru)
                except ValueError:
                    print("Nomor tidak valid, tidak diubah.")
            
            print("Kontak berhasil diedit!\n")
            return

    print("Kontak tidak ditemukan.\n")

def simpan_kontak_ke_file(nama_file="daftar_kontak.txt"):
    try:
        with open(nama_file, "w") as file:
            for k in kontak:
                file.write(f"{k['nama']} - {k['nomor']}\n")
        print(f"Kontak berhasil disimpan ke file '{nama_file}'\n")
    except Exception as e:
        print("Gagal menyimpan kontak:", e)



def menu():
    while True:
        print("=== Menu Kontak ===")
        print("1. Tambah Kontak")
        print("2. Lihat Kontak")
        print("3. Hapus Kontak")
        print("4. Cari Kontak")
        print("5. Edit Kontak")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tambah_kontak()
            simpan_kontak_ke_file()
        elif pilihan == "2":
            lihat_kontak()
        elif pilihan == "3":
            hapus_kontak()
            simpan_kontak_ke_file()
        elif pilihan == "4":
            cari_kontak()
        elif pilihan == "5":
            edit_kontak()
            simpan_kontak_ke_file()
        elif pilihan == "6":
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid!\n")

muat_kontak_dari_file()  # load kontak dari file kalau ada

menu()