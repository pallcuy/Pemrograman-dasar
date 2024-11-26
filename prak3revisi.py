print ("""
BALAP MOBIL 
===========""")
print ("Kelas yang tersedia :")
print ("1. Kelas Stock",)
print ("2. Kelas Semi Pro")
print ("3. Kelas Professional")

pilih_kelas = int(input("Masukkan angka 1, 2, dan 3 untuk pilih kelas : "))

kelas_stock = 3  
kelas_semi_pro = 4     
kelas_pro = 5

bahan_bakar = 100
putaran = 0

while bahan_bakar >= 0:
        if pilih_kelas == 1:
                konsumsi_perputaran = 3
        elif pilih_kelas == 2:
                konsumsi_perputaran = 4
        elif pilih_kelas == 3:
                konsumsi_perputaran = 5
        
        putaran += 1
        bahan_bakar -= konsumsi_perputaran

        if putaran % 5 == 0:
                bahan_bakar += 5

        if bahan_bakar < 0:
                putaran -= 1

if pilih_kelas == 1:
        nama_kelas = "Kelas Stock"
elif pilih_kelas == 2:
        nama_kelas = "Kelas Semi Pro"
elif pilih_kelas == 3:
        nama_kelas = "Kelas Profesional"

print("Kelas", nama_kelas,"telah menempuh", putaran,"putaran")

