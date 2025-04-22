Mantap! Ini penting banget buat dipahami, karena **dictionary** dan **array (list)** adalah dua struktur data yang paling sering dipakai di Python (dan bahasa lain juga).

---

## 🆚 Perbedaan **Dictionary** vs **Array (List)**

| Fitur                | `Dictionary` (`dict`)                          | `Array` / `List` (`list`)                         |
|---------------------|------------------------------------------------|--------------------------------------------------|
| Cara akses data     | Pakai **key** (nama, label)                    | Pakai **index** (angka mulai dari 0)             |
| Format              | `{key: value}`                                 | `[item1, item2, item3]`                          |
| Urutan data         | Tidak wajib urut (tapi sejak Python 3.7 urut)  | Urutan sangat penting                            |
| Cocok untuk         | Data yang punya nama/label (berpasangan)       | Data sejenis yang diurutkan                      |
| Contoh penggunaan   | Data mahasiswa (`nama`, `umur`, dll)           | Daftar nilai, daftar buah, daftar angka          |

---

## ✅ Contoh **Dictionary**
```python
mahasiswa = {
    "nama": "Anam",
    "umur": 20,
    "jurusan": "Informatika"
}
print(mahasiswa["nama"])  # Output: Anam
```
> Cocok untuk menyimpan data **berlabel** atau berpasangan, seperti data profil.

---

## ✅ Contoh **List (Array)**
```python
buah = ["apel", "jeruk", "mangga"]
print(buah[0])  # Output: apel
```
> Cocok untuk data **berurutan** tanpa label khusus, misalnya daftar item.

---

## 🚀 Kapan Menggunakan?

| Kebutuhan | Pakai |
|----------|-------|
| Kamu mau data berurutan, kayak daftar nilai, daftar nama | `list` |
| Kamu mau data dengan label, kayak biodata, info produk | `dict` |
| Kamu mau nyimpan banyak mahasiswa, tiap mahasiswa ada `nama`, `umur`, `alamat` | `list of dict` |
```python
mahasiswa_list = [
    {"nama": "Anam", "umur": 20},
    {"nama": "Della", "umur": 22}
]
```

---

## 🎯 Tips Mudah Ingat:
- **List** = "daftar"
- **Dict** = "data lengkap berlabel"

---

Kalau kamu mau latihan interaktif buat bedain list dan dictionary, atau mau aku buatin kuis kecil biar makin ngerti, tinggal bilang aja 😎