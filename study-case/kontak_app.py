# Fitur:
# - Tambah kontak
# - Tampilkan semua kontak
# - Cari kontak berdasarkan nama
# - Hapus kontak
# - Edit kontak

def tambah_kontak(kontak):
    nama = input("Masukkan nama kontak: ")
    nomor = input("Masukkan nomor kontak: ")
    kontak[nama] = nomor
    print(f"Kontak {nama} berhasil ditambahkan.")

def tampilkan_kontak(kontak):
    if not kontak:
        print("Tidak ada kontak yang tersimpan.")
    else:
        print("Daftar Kontak:")
        for nama, nomor in kontak.items():
            print(f"Nama: {nama}, Nomor: {nomor}")

def cari_kontak(kontak):
    nama = input("Masukkan nama yang ingin dicari: ")
    if nama in kontak:
        print(f"Kontak ditemukan: Nama: {nama}, Nomor: {kontak[nama]}")
    else:
        print("Kontak tidak ditemukan.")

def hapus_kontak(kontak):
    nama = input("Masukkan nama kontak yang ingin dihapus: ")
    if nama in kontak:
        del kontak[nama]
        print(f"Kontak {nama} berhasil dihapus.")
    else:
        print("Kontak tidak ditemukan.")

def edit_kontak(kontak):
    nama = input("Masukkan nama kontak yang ingin diedit: ")
    if nama in kontak:
        nomor_baru = input("Masukkan nomor baru: ")
        kontak[nama] = nomor_baru
        print(f"Kontak {nama} berhasil diperbarui.")
    else:
        print("Kontak tidak ditemukan.")

def main():
    kontak = {}
    while True:
        print("\nMenu:")
        print("1. Tambah Kontak")
        print("2. Tampilkan Semua Kontak")
        print("3. Cari Kontak")
        print("4. Hapus Kontak")
        print("5. Edit Kontak")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tambah_kontak(kontak)
        elif pilihan == "2":
            tampilkan_kontak(kontak)
        elif pilihan == "3":
            cari_kontak(kontak)
        elif pilihan == "4":
            hapus_kontak(kontak)
        elif pilihan == "5":
            edit_kontak(kontak)
        elif pilihan == "6":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
