#  ------------------------ Selasa, 5 November 2019 -----------------------------------

# class / cetakan atau mold

class kendaraan:
    warna: 'merah'
    tahun: 2010

class MobilCustom():
    def __init__(self, warna, tahun, model):  # variabel selain self bisa lebih dari 2
        self.color = warna
        self.year  = tahun
        self.model = model
    # method
    def jadul(self):
        if self.year < 2010:
            return True
        else: return False
    def tes(self):
        print(self.color,self.year,self.model,self.jadul())

mobil1 = MobilCustom('pink', 2018, 'Z')
mobil2 = MobilCustom('blue', 2010, 'Y')
mobil3 = MobilCustom('merah', 1998, 'X')
mobil4 = MobilCustom('kuning', 2000, 'V')

# print(mobil1.color)
# print(mobil2.color)
print(mobil3.jadul())
# print(mobil1.jadul())
# print(mobil3.tes())

'''
class Mobil:
    def __init__(self, warna, seat):
        self.warna = warna
        self.seat  = seat

class Car(Mobil):          # Disebut dengan Inheritance
    pass

mobil5 = Mobil('pink', 4)
car1 = Car('black', 8)

# print(mobil5.warna, mobil5.seat)
# print(car1.warna, car1.seat)

#########################################
class X:
    def __init__(self, nama, gelar):
        self.nama  = nama
        self.gelar = gelar

# Contoh Contoh untuk mengcopy/inheritance X

class Y(X):
    def __init__(self, nama, gelar):
        X.__init__(self, nama, gelar)
'''
# class Y(X):
#     pass

# class Y(X):
#     def __init__(self, nama, gelar):
#         super().__init__(nama, gelar)
'''
objX = X('Andi', 'Prof')
objY = Y('Budi', 'Dr.')



#####################
class Z:
    nama = 'Z'
    usia = 21

objZ = Z()
# print(objZ.nama)
# print(objZ.usia)

del Z.nama
# print(objZ.usia)

class student:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

##### Tugas #####
data = [
    {'nama' : 'Andi', 'usia' : '21'},
    {'nama' : 'Budi', 'usia' : '22'},
    {'nama' : 'Caca', 'usia' : '20'},
    {'nama' : 'Doni', 'usia' : '21'},
]

for i in data:
    stud = student(i['nama'], i['usia'])
    print(f'{stud.nama} {stud.usia}')

# Cara lain

def createObj(x):
    nama = x['nama']
    vars()[nama] = student(x['nama'], x['usia'])
    return vars()[nama]

dataNew = list(map(createObj, data))
# print(dataNew[0].nama)
# print(dataNew[0].usia)

# Cara lain 2

def createObj2(x):
    return student(x['nama'], x['usia'])

dataNew = list(map(createObj2, data))
print(dataNew[1].nama)
print(dataNew[1].usia)

# Cara lain 3

dataNew3 = list(map(
    lambda x: student(x['nama'], x['usia']), data
))

# print(dataNew3[2].nama)
# print(dataNew3[2].usia)


######################################
class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
        self.keliling = self.sisi * 4
        self.luas = self.sisi ** 2

PersegiA = Persegi(4)
PersegiB = Persegi(8)
PersegiC = Persegi(10)

print(vars(PersegiA)); print(vars(PersegiB)); print(vars(PersegiC))

#### Tugas ###
# class keRomawi():
    # ....

# keRomawi(3) => III
# keRomawi(5) => V
# keRomawi(11) => XI
# keRomawi(2019) => MMXIX
'''