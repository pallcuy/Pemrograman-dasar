# Inisialisasi Harga per kota Tujuan
print ("""
TIKET BUS DI KOTA PILIHAN 
=========================""")
print ("Kota yang tersedia :")
print ("1. SURABAYA")
print ("2. MALANG")
print ("3. BALI")
print ("4. YOGYAKARTA")
print ("5. SOLO")
print ("0. KELUAR")

surabaya = 50000
malang = 60000
bali = 90000
yogyakarta = 90000
solo = 80000

while True:
    tujuan = int(input("Masukkan pilihan kota tujuan (1 - 5) atau 0 untuk keluar: "))
    
    if tujuan == 0:
        print("Terima kasih! Program selesai.")
        break

    if tujuan < 0 or tujuan > 5:
        print("Pilihan tidak valid! Silakan masukkan angka antara 0 dan 5.")
    else:
        jumlah_tiket = int(input("masukkan jumlah tiket : "))

        if tujuan == 1:
            harga = surabaya * jumlah_tiket
            if harga >= 600000:
                harga = harga * 0.9  # Potongan 10%
            if harga >= 300000:
                harga = harga * 0.9  # Potongan 10%

        if tujuan == 2:
            harga = malang * jumlah_tiket
            if harga >= 900000:
                harga = harga * 0.9  # Potongan 10%
            if harga >= 300000:
                harga = harga * 0.9  # Potongan 10%

        if tujuan == 3:
            harga = bali * jumlah_tiket
            if harga >= 900000:
                harga = harga * 0.9  # Potongan 10%
            if harga >= 450000:
                harga = harga * 0.85  # Potongan 15%

        if tujuan == 4:
            harga = yogyakarta * jumlah_tiket
            if harga >= 500000:
                harga = harga * 0.9  # Potongan 10%
            if harga >= 250000:
                harga = harga * 0.95  # Potongan 5%

        if tujuan == 5:
            harga = solo * jumlah_tiket
            if harga >= 500000:
                harga = harga * 0.9  # Potongan 10%
            if harga >= 250000:
                harga = harga * 0.95  # Potongan 5%

        print("Harga tiket ke", tujuan, "adalah : Rp", int(harga))
