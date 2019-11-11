# ------------------------------- Senin, 28 Oktober 2019 -------------------------------

# Latihan
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0
y = []

while index < len(x):
    y.append(x[index]**2)
    index += 1
print(y)


# break continue
i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)


# Latihan
password = '12345'
status   = False

if input('Ketik password: ') != password :
    while status == False:
        userinput = input('Password Salah! Ketik password : ')
        if (userinput == password):
            status = True
            print('Password Benar!')
        else:
            status=False
else:
    print('Password Benar!')

# Alternatif jawaban
inputuser = ' '
while inputuser != password:
    inputuser = input('Ketik Password : ')
    if inputuser != password:
        print('Password Salah!')
    else:
        print('Password Benar!')


# Apabila ada batasan salah
count = 0
if input('Ketik password: ') != password :
    while status == False and count < 3:
        userinput = input('Password Salah! Ketik password : ')
        if (userinput == password):
            status = True
            print('Password Benar!')
        else:
            status=False
            count += 1
    print('Batas maksimum salah!')
else:
    print('Password Benar!')

# Alternative
inputuser = ''
jumlahInput = 0
batasInput = 5
lebih = False

while inputuser != password and not lebih:
    if jumlahInput < batasInput:
        inputuser= input(f'Input ke-{jumlahInput+1} ketik password : ')
        jumlahInput += 1
    else:
        lebih = True
if lebih:
    print('Kesempatan habis, tunggu 24 jam')
else:
    print('Password Benar!')
