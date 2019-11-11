# -------------------------- Selasa, 22 Oktober 2019 -----------------------------------

#### TUGAS ####
# Tugas dari website mengenai soal cerita, mencari jumlah ayam dan kambing
# Dengan diketahui jumlah total ayam dan kambing 13 dan total jumlah kaki mereka 32

# 1 kambing + 1 ayam = 13
# 4 kaki k + 2 kaki a = 32

'''
totalHewan  = 13
totalKaki   = 32
kakiAyam    = 2
kakiKambing = 4

divisor = abs(kakiAyam - kakiKambing)

Kambing = abs((totalKaki - totalHewan*kakiAyam) / divisor)
print("Kambing:", Kambing)

Ayam = abs((totalKaki - totalHewan*kakiKambing) / divisor)
print("Ayam:", Ayam)
'''

# Jika digunakan input
totalHewan  = int(input('Ketik total hewan : '))
totalKaki   = int(input('Ketik total kaki hewan : '))
kakiAyam    = int(input('Ketik jumlah kaki hewan A : '))
kakiKambing = int(input('Ketik jumlah kaki hewan B : '))

divisor = abs(kakiAyam - kakiKambing)

Kambing = abs((totalKaki - totalHewan*kakiAyam) / divisor)
#print("Kambing:", Kambing)

Ayam = abs((totalKaki - totalHewan*kakiKambing) / divisor)
#print("Ayam:", Ayam)

print(f'hewan A = {int(Ayam)}, hewan B = {int(Kambing)}')





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Soal dari website https://deni11math.wordpress.com/2019/01/07/soal-cerita-terkait-spldv/
# Penjabaran Matematis
'''
#                 A = 1/7 Ibu + 19
#    atau   1/7 Ibu = A - 19
#               Ibu = (A - 19)/ 1/7

#          (A - 19) = 1/4 (Ibu - 19) - 1/2
#          (A - 19) = 1/4 Ibu - 19/4 - 1/2 
#            A - 19 = 1/4 ((A - 19) / 1/7) - 19/4 - 1/2
#                 A = 7/4 (A - 19) - 19/4 - 1/2
#     A = (1/4 / 1/7 * 19) + 19 * 1/4 + 1/2 - 19     /     (1/4 / 1/7) - 1   
#         7/4 A - A = 133/4 + 21/4 - 19
#            -3/4 A = -154/4 + 19
#                 A = 26

#           1/7 ibu = 1/4 (ibu - 19) - 1/2
#             4 ibu = 7 (ibu - 19) - 14     dikali 28

#           1/7 ibu = 1/4 ibu - 19/4 - 1/2
# 1/7 ibu - 1/4 ibu = - 19/4 - 1/2
#   (1/4 - 1/7) ibu = 19/4 + 1/2       ~~ di kali (-1)
#               ibu = (19/4 + 1/2) / (1/4 - 1/7)
#               ibu = 49

'''
# Dibuat codingan dari penjabaran matematis

agediff_i = 1/7
diff_i    = 19
agediff_a = 1/4
diff_a    = 1/2

equation_1 = (diff_i * agediff_a) + diff_a
equation_2 = (agediff_a - agediff_i)
age_ibu    = round(equation_1 / equation_2)

equation_3 = (((agediff_a / agediff_i) * diff_i) + ((diff_i * agediff_a) + diff_a) - diff_i)
equation_4 = (agediff_a / agediff_i) - 1
age_anak   = int(equation_3 / equation_4)

melahirkan = age_ibu - age_anak

print(f'Umur ibu {age_ibu}, Umur anak {age_anak}')
print(f'Maka umur ibu saat melahirkan anak adalah {melahirkan}')


