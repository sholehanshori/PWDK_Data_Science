# -------------------------- Kamis, 24 Oktober 2019 -----------------------------------


# S = {bilangan cacah kurang dari 11}
# A = {x|x<10, xEbilangan prima}
# B = {5, 7, 9}

S = []
A = []
B = []

for i in range(0, 11, 1):
    S.append(i)

for i in [2, 3, 5, 7]:
    A.append(i)

for i in [5, 7, 9]:
    B.append(i)

S = set(S)
A = set(A)
B = set(B)

operasi_1 = (A & B)
operasi_2 = (A | B)
operasi_3 = (A & operasi_2)
operasi_4 = (B & operasi_2)
operasi_5 = (operasi_2 & operasi_2)
operasi_6 = (operasi_1 | operasi_2)


print(f'Irisan dari A dan B adalah {operasi_1}')
print(f'Gabungan dari A dan B adalah {operasi_2}')
print(f'Operasi A ∩ (A ∪ B) adalah {operasi_3}')
print(f'Operasi B ∩ (A ∪ B) adalah {operasi_4}')
print(f'Operasi (A ∪ B) ∩ (A ∪ B) adalah {operasi_5}')
print(f'Operasi (A ∩ B) ∪ (A ∪ B) adalah {operasi_6}')