def buatfile(namanya):
    try:
        with open(namanya, 'x') as file:
            nama = input("Masukkan nama kamu: ")
            nim = input("Masukkan NIM kamu: ")
            tahunang = input("Masukkan Tahun Angkatan kamu: ")
            
            file.write(f"Nama: {nama}\n")
            file.write(f"NIM: {nim}\n")
            file.write(f"Tahun Angkatan: {tahunang}\n ")
            
            print(f"File '{namanya}' berhasil dibuat!")
    except FileExistsError:
        print(f"File '{namanya}' sudah ada.")

def bacafile(namanya):
    try:
        with open(namanya, 'r') as file:
            isinya = file.read()
            print("Isi file:")
            print(isinya)
    except FileNotFoundError:
        print("File tidak ditemukan atau kamu belum buat file itu.")

def tambahin(namanya, teks):
    with open(namanya, 'a') as file:
        file.write(teks + '\n')
        print(f"Teks '{teks}' telah ditambahkan ke dalam file!")

while True:
    print("\n===FIle Handling===")
    print("1. Membuat dan menulis file baru")
    print("2. Membaca file")
    print("3. Tambahkan teks file")
    print("4. Keluar dari program")

    pilihan = input("Masukkan pilihan berupa angka (1/2/3/4): ")

    if pilihan == '1':
        namanya = input("Masukkan nama file: ")
        buatfile(namanya)
    elif pilihan == '2':
        namanya = input("Masukkan nama file yang ingin dibaca: ")
        bacafile(namanya)
    elif pilihan == '3':
        namanya = input("Masukkan nama file untuk menambahkan teks: ")
        teksbaru = input("Masukkan teks yang ingin ditambahkan: ")
        tambahin(namanya, teksbaru)
    elif pilihan == '4':
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih angka 1/2/3/4.")