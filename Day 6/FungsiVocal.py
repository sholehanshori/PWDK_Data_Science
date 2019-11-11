
def vocal(kalimat):
    kalimat = kalimat.lower()
    kalimat = kalimat.replace('a', 'o')
    kalimat = kalimat.replace('i', 'o')
    kalimat = kalimat.replace('u', 'o')
    kalimat = kalimat.replace('e', 'o')
    kalimat = kalimat.replace('o', 'o')
    print(kalimat)

vocal(input('Ketik kalimat : '))