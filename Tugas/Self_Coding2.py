#########################################
#  ------------------------ Rabu, 6 November 2019 -----------------------------------
import datetime as dt
x =  dt.datetime.now()

day   = x.strftime('%A') # hari
date  = x.strftime('%d') # tanggal
month = x.strftime('%B') # nama bulan
year  = x.strftime('%Y') # tahun

hour = x.strftime('%H') # 24 jam
minu = x.strftime('%M') # min
sec  = x.strftime('%S') # sec