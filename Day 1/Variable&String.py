# -------------------------- Senin, 21 Oktober 2019 -----------------------------------

# materi Variabel
nama = 'Budi Santoso'
usia =  20
tinggi = 68.5
jomblo = True
print(type(nama))
print(type(usia))
print(type(tinggi))
print(type(jomblo))

# Perbedaan + dan , untuk penggabungan string dengan integer
print('umurku ' + str(usia))
print('umurku', usia)

# jenis penggabungan string dan integer
print ('saya ' + nama + ' usia ' + str(usia))
print ('saya', nama, 'usia', usia)
print ('saya %s usia %d' %(nama, usia))
print ('saya {} usia {}'.format(nama, usia))
print (f'saya {nama} usia {usia}')

# edit besar kecil huruf
print (nama.lower())
print (nama.upper())

# untuk cek status UPPER or lower
z = 'hihihi'
print (z.isupper())
print (z.islower())

# menghitung karakter huruf
coba = 'Python Oke Sekali'
print(len(nama))

#[start : stop : step]
print (coba[0:17])
print (coba[14:len(nama):2])
print (nama.index('S'))

# cara menghitung jumlah huruf tanpa spasi
print (len(coba.replace(' ', '')))