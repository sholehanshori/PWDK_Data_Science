# -------------------------- Selasa, 22 Oktober 2019 -----------------------------------

# mengenai angka

# pow mempunyai fungsi sama seperti pangkat 2
print(pow(2,3))
print(2 ** 3)

# akar pangkat
print (4 ** (1/2))
print (27 ** (1/3))

# pembulatan
print(round(3.678567))
print(round(3.678567, 2)) # supaya pembulatan ada beberapa bilangan dibelakang koma

print(.1 + .2) #untuk 0.1 bisa ditulis .1 pada python
#hasil dari penjumlahan di atas ada anomali 0.300000000004, baca referensi kenapa bisa begitu?


# menggunakan library di python.
import math

print (math.pi)   # menampilkan nilai pi
print (math.floor(3.9))  # pembulatan ke bawah
print (math.ceil(3.1))  # pembulatan ke atas
print (math.sqrt(196))  # pengakaran
print (math.factorial(4))  # factorial  4! =  4 x 3 x 2 x 1 = ??

nama = input('Halo, namamu siapa? : ')
print(f'Selamat datang {nama}')
angka = int(input('Masukkan angka : '))  #menggunakan int untuk mengubah string
print(f'Kuadrat dari {angka} = {angka ** 2}')