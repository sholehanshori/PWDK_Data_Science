# ------------------------------- Rabu, 30 Oktober 2019 -------------------------------

# Merubah huruf Vokal 2.0

def ubahVokal(kata):
    output = ''
    for huruf in kata.lower():
        if huruf in 'aiueo':
            output = output + 'o'
        else:
            output = output + huruf
    return output

x = input('Masukkan kata : ')
print(ubahVokal(x))


# Mengecek suatu kata apakah Palindrom atau tidak
# Palindrom = kata yg apabila dibalik cara pembacaanya sama

x = 'malama'
y = list(x[::-1])   # Sebenarnya tanpa list, dapat di putar balik 'Kata' nya
y = ''.join(y)      # Dapat mengubah list menjadi string kembali

def palindrom(kata):
    if kata == y:
        return True
    else:
        return False

print(palindrom(x))
'''
# Alternative
def palindrom2(kata):
    for i in range(round(len(kata)/2)):
        palindromkah = False
        if kata[i] == kata[len(kata) - 1 - i]:
            palindromkah = True
        else:
            palindromkah = False
            break
    return palindromkah

print(palindrom2('katak'))
print(palindrom2('susah'))

# Tambahan alternativ
# kalimat = 'Hai aku Lintang'
# menjadi = 'iaH uka gnatniL'

# -----------------------------------------------
# Merubah sandi kata/kalimat menjadi sandi morse

# -----------------------------------------------
# Caesar Cipher positif
# caesharCipher('Lintang', 2) => Nkpvcpi
# menambahkan index tiap huruf menjadi 2
'''