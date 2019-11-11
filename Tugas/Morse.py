# ------------------------------- Rabu, 30 Oktober 2019 -------------------------------

# Merubah sandi kata/kalimat menjadi sandi morse

kamus = {
    'A':'._', 'B':'_...', 'C':'_._.', 'D':'_..', 'E':'.', 
    'F':'.._.', 'G':'__.', 'H':'....', 'I':'..', 'J':'.___',
    'K':'_._', 'L':'._..', 'M':'__', 'N':'_.', 'O':'___',
    'P':'.__.', 'Q':'__._', 'R':'._.', 'S':'...', 'T':'_',
    'U':'.._', 'V':'..._', 'W':'.__', 'X':'_.._', 'Y':'_.__', 'Z':'__..', 
    '1':'.____', '2':'..___', '3':'...__', '4':'...._', '5':'.....',
    '6':'_....', '7':'__...', '8':'___..', '9':'____.', '0':'_____'
}

alfabet = list(kamus)
morse   = list(kamus.values())

kata = input('Masukkan kata/kalimat : ')

def sandiMorse(word):
    output = ''
    word = word.upper()
    word = word.split()
    # word = ''.join(word)
    for i in word:
        if i in alfabet:
            morse_1 = morse[alfabet.index(i)]
            output = output + morse_1 + ' / '
        elif i in morse:
            alfabet_1 = alfabet[morse.index(i)]
            output = output + alfabet_1
        elif i == '/':
            output = output + ' '
        else:
            output = output + i + ' / '
    return output

print(sandiMorse(kata))






x = (' _. / ._ / __ / ._ ')
# x = 'awds'
x = x.split()
# print(type(x))
# print(x)
x = ''.join(x)
# print(type(x))
# print(x)

# def sandiMorse(word):
#     output = ''
#     for i in word.upper():
#         if i in alfabet:
#             morse_1 = morse[alfabet.index(i)]
#             output = output + morse_1 + ' / '
#         else:
#             output = output + i + ' / '
#     return output
