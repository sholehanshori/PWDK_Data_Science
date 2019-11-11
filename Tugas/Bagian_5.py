# -------------------------- Jumat, 25 Oktober 2019 -----------------------------------

days = {
    'senin' : 'monday', 'selasa' : 'tuesday', 'rabu' : 'wednesday', 
    'kamis' : 'thursday', 'jumat' : 'friday', 'sabtu' : 'saturday', 'minggu' : 'sunday'
}


'''
hari = input('Ketik nama hari : ')
#eng = days.get(hari)

print(f'Bahasa Inggrisnya {hari.upper()} adalah {days.get(hari.lower()).upper()}')
#atau
print(f'Bahasa Inggrisnya {hari.upper()} adalah {days.get(hari.lower(), "Ga Ada!").upper()}')  #Kalau tidak ada di list

# atau

print(days.get(hari))
print(f'Bahasa Inggrisnya {hari.upper()} adalah {days[hari.lower()].upper()}')

x = hari.lower()
if x == 'monday':
    print('senin')
elif x == 'tuesday':
    print('selasa')
elif x == 'wednesday':
    print('rabu')
elif x == 'thursday':
    print('kamis')
elif x == 'friday':
    print('jumat')
elif x == 'saturday':
    print('sabtu')
elif x == 'sunday':
    print('minggu')
else:
    print('Tidak Ada!')
'''

# Alternative
hari = list(days)
day  = list(days.values())

x = input('Ketik nama hari (ENG/IND) : ')

if x.lower() in hari:
    engHari = day[hari.index(x.lower())]
    print(f'Bhs Inggris {x.upper()} adalah {engHari.upper()}')
elif x.lower() in day:
    idDay = hari[day.index(x.lower())]
    print(f'Bhs Indonesia {x.upper()} adalah {idDay.upper()}')
else:
    print(f'Input \"{x}\" tidak VALID')

# print(day)
# print(hari)

# -----------------------------------------------

nilai = 98

if nilai >= 82:
    print('Nilai anda A')
elif nilai in range(72, 81):    # atau (nilai >= 72) and (nilai <=81)
    print('Nilai anda B')
elif nilai in range(62, 71):    # atau (nilai >= 62) and (nilai <=71)
    print('Nilai anda C')
elif nilai in range(52, 61):    # atau (nilai >= 52) and (nilai <=61)
    print('Nilai anda D')
else:
    print('Nilai anda E')