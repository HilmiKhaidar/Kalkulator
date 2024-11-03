# Kalkulator sederhana

# Fungsi untuk operasi penjumlahan
def tambah(x, y):
    return x + y

# Fungsi untuk operasi pengurangan
def kurang(x, y):
    return x - y

# Fungsi untuk operasi perkalian
def kali(x, y):
    return x * y

# Fungsi untuk operasi pembagian
def bagi(x, y):
    return x / y 
# Memulai perulangan agar kalkulator terus berjalan
while True:
    print("\nPilih operasi yang mau dilakukan:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

    if pilihan == '5':
        print("Terima kasih, program selesai.")
        break  # Keluar dari perulangan

    # Input untuk angka pertama dan kedua
    angka1 = input("Masukkan angka pertama: ")
    angka2 = input("Masukkan angka kedua: ")

    # Mengonversi input menjadi float
    angka1 = float(angka1)
    angka2 = float(angka2)

    # Menghitung berdasarkan pilihan yang dipilih
    if pilihan == '1':
        hasil = tambah(angka1, angka2)
        print("Hasil: " + str(int(angka1)) + " + " + str(int(angka2)) + " = " + str(int(hasil)))
    elif pilihan == '2':
        hasil = kurang(angka1, angka2)
        print("Hasil: " + str(int(angka1)) + " - " + str(int(angka2)) + " = " + str(int(hasil)))
    elif pilihan == '3':
        hasil = kali(angka1, angka2)
        print("Hasil: " + str(int(angka1)) + " * " + str(int(angka2)) + " = " + str(int(hasil)))
    elif pilihan == '4':
        # Tanpa pengecekan untuk pembagian dengan nol
        hasil = bagi(angka1, angka2)
        print("Hasil: " + str(int(angka1)) + " / " + str(int(angka2)) + " = " + str(int(hasil)))
    else:
        print("Pilihan tidak valid, coba lagi.")
