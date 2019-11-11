# ------------------------------- Rabu, 30 Oktober 2019 -------------------------------

# Tambahan alternativ
kalimat = 'Hai aku Lintang'
# menjadi = 'iaH uka gnatniL'

kalimat = kalimat.split()
print(kalimat)

kalimat = input('Masukkan kalimat : ')
kalimat = kalimat.split()

def balikPosisi(myList):
    z = ''
    for y in myList:
        x = y[::-1] + ' '
        z += x
    return z

print(balikPosisi(kalimat))