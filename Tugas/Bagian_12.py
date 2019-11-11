#  ------------------------ Senin, 11 November 2019 -----------------------------------

#~~~~~~~~~~~~~~~~ Latihan ~~~~~~~~~~~~~~~~~~
def fibo(urut):
    listdata = [0, 1]
    for i in range(1, urut):
        listdata.append(listdata[i] + listdata[i-1])
    return listdata

# Bilangan fibonacci (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, )
# Merupakan bilangan yg merupakan penambahan dari 2 bilangan sebelumnya

# print(fibo(8))


numberList = [                        
    [1, 2, 3],              
    [4, 5, 6],      
    [7, 8, 9]              
]                        
newList  = [[numberList[j][i] for j in range(len(numberList))] for i in range(len(numberList))]

newList2 = [[numberList[j][i] for j in range(len(numberList))] for i in range(len(numberList)-1,-1,-1)]

newList3 = [[numberList[j][i] for j in range(len(numberList)-1,-1,-1)] for i in range(len(numberList)-1,-1,-1)]
print(newList)

print(newList2)
print(newList3)