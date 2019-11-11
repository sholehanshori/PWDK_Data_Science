# -------------------------- Jumat, 1 November 2019 -----------------------------------


def pangkat(x, y):
    pangkat = 1
    for i in range(y):
        pangkat *= x
    print(f'Jawaban dari {x} pangkat {y} adalah {pangkat}')
pangkat(2, 3)

# Function yang memanggil dirinya sendiri dinamakan "Rekursif Fungsi"
def pangkatB(x, y):
    if (y == 1):
        return x
    else:
        return x * pangkatB(x, y-1)
print(pangkatB(2,3))

# Penjelasan
'''
pangkatB(2,3) = return 2 * pangkatB(2,2)        = 2 * 4 = 8
pangkatB(2,2) = return 2 * pangkatB(2,1)        = 2 * 2
pangkatB(2,1) = return 2
'''