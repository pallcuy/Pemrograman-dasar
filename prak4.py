mahasiswa_list = []

jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa : "))

pilihan = 0

for i in range(jumlah_mahasiswa):
        print("\nData Mahasiswa ke", i + 1)
        nama = input("Masukkan nama : ")
        nim = input("Masukkan nim : ")
        tanggal_lahir = input("Masukkan tanggal lahir : ")
        
        mahasiswa_list.append((nama, nim, tanggal_lahir))

for mahasiswa in mahasiswa_list:
        print("\nData Mahasiswa   : ")
        print("Nama             : ", mahasiswa[0])
        print("NIM              : ", mahasiswa[1])
        print("Tanggal Lahir    : ", mahasiswa[2])
        print()
