#  ------------------------ Senin, 11 November 2019 -----------------------------------

''' Yang sudah dipelajari '''
# variables:
# list, tuple, set, dict
# fungsi
# def => prog, return, recursive, lambda(map, reduce, filter)
# loop => while, for, map()
# class, objectfile => csv json


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Soal Latihan ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1. Fibonacci
# class Fibo:
#     . . .
# Fibo = Fibo()

'''             '''
# 2. x = 'AbcdEFgHi'
        # return function =>  x = 'aBCDefGhI'
'''             '''
# 3. function cek sudut antara 2 sisi
        # sisi A =  8 cm, sisi B = 10 cm, sudut AB = 60, panjang C = ?
'''             '''
# 4. merotasi list
'''
[                        [
    [1, 2, 3],              [1, 4, 7],
    [4, 5, 6],      =>      [2, 5, 8],
    [7, 8, 9]               [3, 6, 9]
]                        ]
'''

def fibo(urutan):
    if urutan < 2:
        return urutan
    else:
        return fibo(urutan - 1) + fibo(urutan - 2)
print(fibo(8))

class Fibo:
    def fibo(self, urutan):
        if urutan < 2:
            return urutan
        else:
            return self.fibo(urutan - 1) + self.fibo(urutan - 2)

Fibo = Fibo()
print(Fibo.fibo(1))
print(Fibo.fibo(4))
print(Fibo.fibo(8))