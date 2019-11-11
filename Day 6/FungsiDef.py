# ------------------------------- Senin, 28 Oktober 2019 -------------------------------

# function

# f(x) = x ^ 2
def kuadrat(x):
    print(x ** 2)

# Untuk memanggil fungsi
kuadrat(2)
kuadrat(3)

# Selain itu bisa di tulis
def pangkat(angka1, angka2):
    print(angka1 ** angka2)

pangkat(2, 3)

# Digabung dengan input
pangkat(
    float(input('Ketik angka 1: ')),
    float(input('Ketik angka 2: '))
)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def angka(x):
#     if x%2 == 1:
#         print(f'Angka {x} adalah bilangan ganjil')
#     else:
#         print(f'Angka {x} adalah bilangan genap')

# angka(float(input('Masukkan angka : ')))




# Return function

def LuasPersegi(sisi):
    print(f' Luas = {sisi*sisi}')
def LuasPersegiReturn(sisi):
    return sisi * sisi

LuasPersegi(5)
#Return berfungsi untuk menyimpan value


# fungsi While =  selama
i = 1
while i < 10:
    print(i)
    i += 1        # i = i + 1
# akan meng-print sebanyak i kurang dari 10

# Penggunaan while
students = ['Andi', 'Budi', 'Caca']

index = 0
while index < len(students):
    print(students[index])
    index += 1


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
P = []
Q = []
R = []
S = []

for i in range(-4, 5, 1):
    Q.append(i)

for i in range(-7, 1, 1):
    R.append(i)

for i in range(-1, 8, 1):
    S.append(i)

for i in range(-9, 10, 1):
    P.append(i)

print(sorted(set(P)))
print(sorted(set(Q)))
print(sorted(set(R)))
print(sorted(set(S)))

