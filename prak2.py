# Inisislisasi Harga perkota Tujuan
surabaya = 50000
malang = 60000
bali = 90000
yogyakarta = 90000
solo = 80000

# Inisialisasi dari pengguna
tujuan = input("masukkan tujuan (surabaya), (malang), (bali), (yogyakarta), (solo) : ")
jumlah_tiket = input("masukkan jumlah tiket : ")

if tujuan == "surabaya":
        harga = surabaya * int (jumlah_tiket)
        if harga >= 300000:
                harga = harga - harga * 0.1
                if harga >= 600000:
                        harga = harga - harga * 0.1

if tujuan == "malang":
        harga = malang * int (jumlah_tiket)
        if harga >= 300000:
                harga = harga - harga * 0.1
                if harga >= 600000:
                        harga = harga - harga * 0.1

if tujuan == "bali":
        harga = bali * int (jumlah_tiket)
        if harga >= 450000:
                harga = harga - harga * 0.15
                if harga >= 900000:
                        harga = harga - harga * 0.1

if tujuan == "yogyakarta":
        harga = yogyakarta * int (jumlah_tiket)
        if harga >= 250000:
                harga = harga - harga * 0.05
                if harga >= 500000:
                        harga = harga - harga * 0.1

if tujuan == "solo":
        harga = solo * int (jumlah_tiket)
        if harga >= 250000:
                harga = harga - harga * 0.05
                if harga >= 500000:
                        harga = harga - harga * 0.1

print("harga tiket ke", tujuan, "adalah : Rp ", int (harga))
