# -------------------------- Senin, 4 November 2019 -----------------------------------

# Python : Lambda function
x = lambda a : a

# Penggunaan lambda adalah ketika kita tidak perlu function tapi kita perlu function di dalam variabel

def y(a):
    return a

print(x(2))
print(type(x))
print(y(4))
print(type(y))

# atau
x = lambda a,b,c : a+b+c

def z(a, b, c):
    return a+b+c

print(x(2,3,4))
print(z(3,4,5))

# digabung 

def myFunction(x):
    return lambda a : a ** x

pangkat2 = myFunction(2)
pangkat3 = myFunction(3)
pangkat5 = myFunction(5)

print(pangkat5(2))

# Contoh lain, untuk mengecek bilangan genap
x = lambda a : True if a%2 == 0 else False

def b(a):
    if a % 2 == 0:
        return True
    else:
        return False

print(x(5))
print(b(4))

# Map python
def c(a):
    return len(a)

a = ['Andi', 'Budi', 'Caca']

x = map(c, a)
print(x)
print(list(x))


# Fungsi combi

a = ['Coklat', 'Melon', 'Nangka']
b = ['Apel', 'Jeruk', 'Nanas']

def combi(a, b):
    return a+' '+b
x = map(combi, a, b)
print(x)
print(list(x))

# Latihan
x = [2, 4, 6, 8, 10]
out = [4, 16, 36, 64, 100]

def pangkat(a):
    return a**2

y = map(pangkat, x)
print(list(y))

d = map(lambda a:a**2, x)
print(list(d))

#################################
# Untuk filter urutan 1,2,3,4
## Cara 1 ##
x = range(11)
def kurangLima(x):
    if x < 5:
        return False
    else:
        return True

y = filter(kurangLima, x)
print(list(y))

## Cara 2 ##
z = filter(lambda a: True if a >= 5 else False, x)
print(list(z))


angka = [1, 2, 3, 4]
# 1 x 2 x 3 x 4 = 24
hasil = 1
for i in angka:
    hasil *= i
print(hasil)

from functools import reduce            # atau import functools tapi nanti penggunaannya functools.reduce()
z = reduce(lambda x, y: x * y, angka)
print(z)

angka = [1, 2, 3, 4]
# menggabungkan map dan filter dengan 

z = list(filter(lambda x : x > 3, map(lambda x : x * 2, angka)))
print(z)
                #atau
z = list(map(lambda x : x * 2, filter(lambda x : x > 3, angka)))
print(z)

