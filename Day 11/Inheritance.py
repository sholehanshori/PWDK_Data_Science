#  ------------------------ Rabu, 6 November 2019 -----------------------------------

# Class Inheritance
class Manusia:
    def __init__(self, nama):
        self.nama = nama

class Wanita(Manusia):
    def __init__(self, nama):
        Manusia.__init__(self, nama)
        self.gender = 'Perempuan'

class Pria(Manusia):
    def __init__(self, nama):
        super().__init__(nama)        # atau      Manusia.__init__(self, nama)
        self.gender = 'Laki-Laki'

objA = Manusia('Andi')
objB = Pria('Andi')
objC = Wanita('Caca')

# print(vars(objA))
# print(vars(objB))
# print(vars(objC))

class X:
    def __init__(self, x):
        self.x = x

class Y:
    def __init__(self, x, y):
        X.__init__(self, x)
        self.y = y

class Z:
    def __init__(self, x, y, z):
        Y.__init__(self, x, y)
        self.z = z

objD = Z('Andi', 'PNS', True)     # Vars berfungsi untuk memprint semua value yg ada di dalam variabel tsb
# print(vars(objD))


class Karnivora:
    def __init__(self):
        self.daging = True

class Herbivora:
    def __init__(self):
        self.tumbuhan = True

class Omnivora(Karnivora, Herbivora):
    def __init__(self):
        Karnivora.__init__(self)
        Herbivora.__init__(self)
        self.McD = True

objE = Omnivora()
# print(vars(objE))


#################################################
import datetime as dt
x =  dt.datetime.now()

# print(x.strftime('%d')) # tanggal
# print(x.strftime('%A')) # hari
# print(x.strftime('%m')) # bulan
# print(x.strftime('%B')) # nama bulan
# print(x.strftime('%Y')) # tahun


# print(x.strftime('%H')) # 24 jam
# print(x.strftime('%I')) # 12 jam
# print(x.strftime('%p')) # am/pm
# print(x.strftime('%M')) # min
# print(x.strftime('%S')) # sec

# print(x.strftime('%c'))
# print(x.strftime('%x'))
# print(x.strftime('%X'))

# print(x.strftime('Hari ini adalah %A'))
# print(x.strftime('Sekarang jam %H:%M:%S WIB'))

##################### Tugas ####################
# file py => class/object
# waktu.hari      =
# waktu.tanggal   =
# waktu.bulan     =
# waktu.tahun     =
# waktu.jam       =
# waktu.menit     =
# waktu.detik     =

import statistics

AB = [1, 3, 9, 2, 6, 4, 7, 8, 5, 5]

# print(statistics.mean(AB))
# print(statistics.median(AB))
# print(statistics.mode(AB))

#################################
from functools import reduce

class Statistik:
    def rataRata(self, x):
        total = reduce(lambda a,b: a+b, x)
        return total/len(x)
    def nilaiTengah(self, x):
        x.sort()
        if len(x) % 2 != 0:
            iTengah = [int(len(x)/2)]
        else:
            iTengah = [int(len(x)/2)-1, int(len(x)/2)]
        aTengah = list(map(lambda a: x[a], iTengah))
        total = reduce(lambda x,y: x+y, aTengah)
        return total/ len(aTengah)

stat = Statistik()
print(stat.rataRata([1,2,3,4,5]))
print(stat.nilaiTengah([1,2,3,4,5]))