
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Soal dari website https://brainly.co.id/tugas/18212234

# Dijabarkan matematisnya
'''
# Andi dan Ayah = 50
# Andi - 4 = 6*(Ayah - 4)

# An + Ay = 50
# An - 4 = 6 * (Ay - 4)      
# 6Ay - 24 + 4 + Ay = 50     
# 7Ay = 50 + 20

# An - 4 = 6 Ay - 24
# An = 6 Ay + 20
# An = 6*(50 - An) - 20
# An = 300 - 6An - 20
# 7An = 280
'''

# Dibuat codingan dari matematis
perbedaan_umur = 50
kali_umur_x = 6
mundur_tahun_x = 4

persamaan = (kali_umur_x*mundur_tahun_x) - mundur_tahun_x
umur_An = (perbedaan_umur + persamaan) / (kali_umur_x + 1)
#umur_Ay = abs(perbedaan_umur - umur_An)

umur_Ay = (perbedaan_umur*kali_umur_x - persamaan) / (kali_umur_x + 1)

print(f'Umur Ayah adalah {int(umur_Ay)}, dan umur Andy adalah {int(umur_An)}')



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Soal dari modul

totalhari = int(input('Ketik jumlah hari : '))
tahun = int(totalhari / 360)
sisa_1 = int(totalhari - tahun*360)
bulan = int(sisa_1 / 30)
sisa_2 = int(sisa_1 - bulan*30)
minggu = int(sisa_2 / 7)
sisa_3 = int(sisa_2 - minggu*7)

print(f'Tahun = {int(tahun)}, Bulan = {int(bulan)}, Minggu {int(minggu)}, Hari = {int(sisa_3)}')