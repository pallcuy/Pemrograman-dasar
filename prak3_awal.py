# balap mobil 3 kelas
# kelas stock
# kelas semi pro
# kelas pro
# ketiga kelas diatas memiliki konsumsi bahan bakar yang berbeda tiap putaran
# 1. kelas stock 3 liter per putaran
# 2. kelas semi pro 4 liter per putaran
# 3. kelas pro 5 liter per putaran
# setiap 5 putaran, seluruh kendaraan mengisi bahan bakar sebanyak 5 liter
# jika setiap kelas diisi dengan 100 liter bahan bakar berapa banyak putaran yang di tempuh setiap kelas
print ("""
BALAP MOBIL 
===========""")
print ("Kelas yang tersedia :")
print ("1. Kelas Stock",)
print ("2. Kelas Semi Pro")
print ("3. Kelas Profesional")

pilih_kelas = int(input("Masukkan angka 1, 2, dan 3 untuk pilih kelas : "))

kelas_stock = 3  
kelas_semi_pro = 4     
kelas_pro = 5

bahan_bakar = 100
putaran = 0

while bahan_bakar >= 0:
        if pilih_kelas == 1:
                konsumsi_per_putaran = 3
                putaran += 1
                bahan_bakar -= konsumsi_per_putaran
                if putaran % 5 == 0:
                        bahan_bakar += 5
                if bahan_bakar < 0:
                        putaran -= 1
                        
        elif pilih_kelas == 2:
                konsumsi_per_putaran = 4
                putaran += 1
                bahan_bakar -= konsumsi_per_putaran
                if putaran % 5 == 0:
                        bahan_bakar += 5
                if bahan_bakar < 0:
                        putaran -= 1
                        
        elif pilih_kelas == 3:
                konsumsi_per_putaran = 5
                putaran += 1
                bahan_bakar -= konsumsi_per_putaran
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

print("Kelas", nama_kelas,"telah menempuh", putaran, "putaran")
