#  ------------------------ Rabu, 6 November 2019 -----------------------------------

import Self_Coding2 as dy
# Mengambil data waktu di tab yg lain

listDay = {
    'Monday' : 'Senin', 'Tuesday' : 'Selasa', 'Wednesday' : 'Rabu', 'Thursday' : 'Kamis', 'Friday' : 'Jumat',
    'Saturday' : 'Sabtu', 'Sunday' : 'Minggu'
}

listMonth = {
    'January' : 'Januari', 'February' : 'Februari', 'March' : 'Maret', 'April' : 'April', 'May' : 'Mei', 'June' : 'Juni',
    'July' : 'Juli', 'August' : 'Agustus', 'September' : 'September', 'October' : 'Oktober', 'November' : 'November',
    'December' : 'Desember'
}


class dateTime():
    def __init__(self):
        self.day   = listDay.get(dy.day)
        self.date  = dy.date
        self.month = listMonth.get(dy.month)
        self.year  = dy.year
        self.hour  = dy.hour
        self.minu  = dy.minu
        self.sec   = dy.sec

print(vars(dateTime()))

A = dateTime()      # Harus dibuat objeknya terlebih dahulu
print(f'Sekarang hari {A.day} tanggal {A.date}:{A.month}:{A.year}')