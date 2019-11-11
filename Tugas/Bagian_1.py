# -------------------------- Senin, 21 Oktober 2019 -----------------------------------
#### TUGAS ####

# mencari huruf
kalimat_1 = 'Hari ini Hari tidak masuk sekolah'
cari_1 = 'h'
x = kalimat_1.upper().replace(cari_1.upper(),'')
print(x)

jmlCari_1 = len(kalimat_1) - len(x)
print(f'Jumlah huruf \'{cari_1}\' ada = {jmlCari_1}')

# mencari kata
kalimat_2 = 'Hari ini Hari tidak masuk sekolah karena hari Minggu'
cari_2 = 'hari'
x = kalimat_2.upper().replace(cari_2.upper(), '')
print(x)

jmlCari_2 = int((len(kalimat_2) - len(x)) / len(cari_2)) #menggunakan int supaya hasil bukan float
print(f'Jumlah kata \'{cari_2}\' ada = {jmlCari_2}')