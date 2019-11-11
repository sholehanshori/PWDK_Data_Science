# -------------------------- Kamis, 24 Oktober 2019 -----------------------------------


x = [
    (1, ['a', 'b', 'c'], 2, 3, 4, 5, 6)
]

# List dalam tuple dapat di ubah tapi tidak bisa sebaliknya
x[0][1][2] = 'Andi'
print(x)  #liat hasil

x[0][1].append('d')
print(x)  #liat hasil

x = tuple(x)
print(x)  #liat hasil

#  {} ~~ merupakan type 'set'
''' Mempunyai karakteristik 
    1. no indexing
    2. duplicate elements not allowed 
    3. set itu mutable, tapi elemen2 nya immutable
    4. dapat dirubah menjadi 'list' tidak seperti 'tuple' 
    '''

# contoh
z = {1, 2, 3, 1, 2, 3}
print(z)  #liat hasil

# contoh rule .3
z = {1, 2, 3, 1, 2, 3}
z.add('a')              # dapat ditambahkan karena 'a' immutable
z.add(('b', 'c', 'd'))  # dapat ditambahkan karena 'tuple' () immutbale
'z.add([4, 5, 6])'      # tidak dapat ditambahkan karena 'list' [] mutable
print(z)

z = {1, 2, 3, 1, 2, 3}

# Perbedaan 'add' dan 'update'
# Untuk 'add' dia menambahkan satu kesatuan          ('Andi') = ('Andi') ke dalam 'set' {}
# Untuk 'update' dia menambahkan menjadi per-elemen  ('Andi') = ('A', 'n', 'd', 'i') ke dalam 'set' {}
# Pada 'add' tipe data tidak di abaikan, contoh   ([1, 2, 3]) = {[1, 2, 3]}
# Pada 'update' tipe data di abaikan,    contoh   ([1, 2, 3]) = {1, 2, 3}

z.update('Andi')
z.update('andi')

#z.remove('budi')
z.discard('budi')
# Perbedaan 'remove' dan 'discard'
# Untuk 'remove', menghilangkan elemen tertentu di dalam data. Tetapi akan EROR bila tidak ada di dalamnya
# Untuk 'discard', menghilangkan elemen tertentu di dalam data. TIDAK EROR bilang tidak ada di dalamnya

z.pop()   # Menghilangkan elemen secara random


g = list('abcd')
h = list('bcefg')

g = set(g)
h = set(h)

# selisih, fitur pada data tipe 'set' {}
print(g.intersection(h))   # mengambil selisih antara 'g' dan 'h'
print(h.intersection(g))   # dibalik pun sama saja
print(g & h)               # sama seperti intersection, tetapi lebih ringkas
print(h & g)               # bisa di balik juga

# penambahan
print(g.union(h))
print(h.union(g))
print(g | h)
print(h | g)

# symmetric difference, eliminasi yg sama
print(g.symmetric_difference(h))
print(h.symmetric_difference(g))
print(g ^ h)
print(h ^ g)

P = {1, 2, 4, 7, 8, 19}
Q = {5, 7, 8, 12, 16, 17, 19}
R = {3, 6, 8, 19}

print( P & Q)
print(P & Q & R)

# frozenset, agar tidak bisa di otak-atik
x = set([1, 2, 3])
y = frozenset([1, 2, 3, 4,1])

print(type(y))
print(len(y))