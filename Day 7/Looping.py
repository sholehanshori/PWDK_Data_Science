# -------------------------- Rabu, 30 Oktober 2019 -----------------------------------

# Untuk mem-print nama kota tanpa ngetik satu-satu kodingan
# Supaya ter-iterasi terus menerus berurutan
kota = ['Jakarta', 'Bandung', 'Surabaya']

# looping menggunakan 'while'
i = 0
while i < len(kota):
    print(kota[i])
    i += 1

# looping menggunakan 'for'
for i in range(len(kota)):
    print(kota[i])

# alternative
for namaKota in kota:
    print(namaKota)

# Apabila 
x = 'purwadhika'
for i in x:
    print(i)

# Maka akan ter-iterasi per-bagian, begitu pula dengan x = [1,2,3,4,5]


# Penggunaan 'continue' untuk skip
for i in range(2, 10):
    if i == 7:
        continue
    print(i)
# Maka hasilnya tidak ada nomor 7


# Cara mem-print terbalik
# cara - 1
x = [1, 2, 3, 4, 5, 6, 7]

x.reverse()
print(x)

# cara - 2
x = [1, 2, 3, 4, 5, 6, 7]
print(x[::-1])

# cara - 3
print(list(reversed(x)))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Memprint angka kelipatan 2 dengan => WOW!
# Menggunakan modulus

def wow(num):
    for i in range(1, num+1):
        if i % 2 == 0:
            print('WOW!')
        else:
            print(i)
#wow(10)

listdata = [1,1]
def fibo(urut):
    for i in range(2, urut):
        listdata.append(listdata[i-2] + listdata[i-1])
    return listdata[urut - 1]

# Bilangan fibonacci (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, )
# Merupakan bilangan yg merupakan penambahan dari 2 bilangan sebelumnya

#print(fibo(8))


# Mengurutkan terbalik tanpa menggunakan reverse etc
# Rumus coding dari modul
import math

def reverseList(theList):
    for i in range(0, math.floor(len(theList)/2)):
        tempList = theList[i]
        theList[i] = theList[len(theList) - 1 - i]
        theList[len(theList) - 1 - i] = tempList
    return theList

print(reverseList(['Andi', 'Budi', 'Caca', 'Doni', 'Eno']))


# Mengurutkan urutan secara terbalik
x = ['Andi', 'Budi', 'Caca', 'Doni', 'Eno']

def terbalik(daftar):
    balik = []
    for i in range(0, len(daftar)):
        daftar_1 = len(daftar) - i - 1
        balik.append(daftar[daftar_1])
    return balik

print(terbalik(x))

# Alternative
def balikPosisi(myList):
    hasil = []
    for i in range(len(myList)):
        hasil.insert(0, myList[i])        
    return hasil
# Penggunaan fungsi seperti append dll, tapi menyisipkan/menambahkan di paling depan

print(balikPosisi(x))