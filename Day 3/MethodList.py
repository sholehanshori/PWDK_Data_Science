# -------------------------- Rabu, 23 Oktober 2019 -----------------------------------

x = 12
x = 13   # yg dipakai x terakhir terdata

x += 2   # x = x + 2
x -= 2   # x = x - 2
x *= 2   # x = x * 2
x /= 2   # x = x / 2

y = 'abcdefghijgklmgnopgqrstuvwgxyz'
print(y[::2]) # sama seperti y[0:len(y):2]
print('g' in y)
print(y.count('g'))


# Latihan
days = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']

# sekarang hari 'sabtu', hari apakah 100 hari lagi?
now = 'sabtu'
week = 7
totalhari = 100

currentindex = days.index(now.lower())
hari =  (totalhari%week) + currentindex
if (hari >6):            # atau ((totalhari%week) + currentindex) % week
    hari -=7

print(f'Maka {totalhari} hari lagi adalah hari {days[hari]}')


# Menambahkan data ke dalam list dan menghilangkannya
days.append('senin2')       # memasukkan senin2 ke dalam list days
days.insert(4, 'senin3')    # menyisipkan senin3 ke dalam index tertentu di list days

days.remove('senin2')       # untuk menghapus senin2 di dalam list days
days.pop(0)                 # untuk menghapus data tertentu berdasarkan index di dalam list days

days.sort()                 # untuk mengurutkan konten data sesuai ascending
days.sort(reverse = True)   # untuk mengurutkan konten data secara descending
days.reverse()              # untuk membalik urutan konten

a = [ 1, 2, 3, 4, 5, 6, 3]
def cariIndex (list, i):
    return(x for x, y in enumerate() if y == i)

print(cariIndex(a, 3))

a = [1, 2, 3]
b = (1, 2, 3)    # perbedaan () dan [], untuk () adalah type 'tuple'
                 # tuple - immutable, atau konten tidak dapat di rubah