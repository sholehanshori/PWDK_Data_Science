# -------------------------- Rabu, 23 Oktober 2019 -----------------------------------

#### TUGAS ####

days = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']

# sekarang hari 'sabtu', hari apakah 100 hari lagi?
now = 'sabtu'
week = 7
totalhari = 100

currentindex = days.index(now.lower())
hari =  (totalhari%week) + currentindex
if (hari >6):            # atau ((totalhari%week) + currentindex) % week
    hari -=7



########################################################

# rasio umur 10 Andi & 4 Budi, sehingga 0.4
# total umur keduanya 49 tahun
'''
10 Andi = 4 Budi
Andi = 4/10 Budi

Andi + Budi = 49
4/10 Budi + Budi = 49
4 Budi + 10 Budi = 490
14 Budi = 490
Budi = 35
'''

Andi = 10
Budi = 4
TotalUmur = 49

Budi_1 = (TotalUmur*Andi) / (Andi+Budi)
#print(Budi_1)

Andi_1 = (TotalUmur*Budi) / (Andi+Budi)
#print(Andi_1)

print(f'Umur Andi dan Budi 2 tahun berikutnya adalah {Andi_1+2} dan {Budi_1+2}')