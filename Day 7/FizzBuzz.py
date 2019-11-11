# ------------------------------- Rabu, 30 Oktober 2019 -------------------------------


def FizzBuzz(num):
    for i in range(1, num + 1):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)

FizzBuzz(15)