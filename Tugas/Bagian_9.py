# -------------------------- Senin, 4 November 2019 -----------------------------------

##### Tugas #####
'''
nomor = [1 - 100]
=> angka genap
=> setiap angka genap di kali 2
=> semua angka sebelumnya di jumlahkan
'''
# Menggunakan Lambda
from functools import reduce
nomor = range(2, 101)

gh = reduce(lambda x, y : x + y, map(lambda x : x * 2, filter(lambda x : True if x%2 == 0 else False, nomor)))
print(gh)

hg = filter(lambda x : True if x%7 != 0 or x/7 == 1 else False, filter(lambda x : True if x%5 !=0 or x/5 == 1 else False, filter(lambda x : True if x%3 != 0 or x/3 == 1 else False, filter(lambda x : True if x%2 != 0 or x/2 == 1 else False, nomor))))
print(list(hg))


# Menggunakan fungsi 'def'
def prima(x):
    a = False
    if x > 1:
        if x == 2:
            a = True
        else:
            for i in range(2, x):
                if x % i == 0:
                    a = False
                    break
                else:
                    a = True
    else:
        a = False
    return a

z = list(filter(prima, range(101)))
print(z)



# Alternative cara Lambda
nums = range(2, 101)
for i in range(2,8):
    nums = list(filter(lambda x: x%i !=0 or x/i == 1, nums))
print(nums)