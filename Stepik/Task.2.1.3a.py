import math

N = int(input())

if N <= 5:
    print(N)
else:
    a = 0
    summ = 0
    while a != (N - 5):
        a += 1
        summ += 0.25
    if int(summ + 1) == float(summ + 1):
            if (summ + 1) % 2 == 0:
                print(1)
            elif (summ + 1) % 2 != 0:
                print(5)
    else:
        if (math.ceil(summ + 1)) % 2 == 0:
            if N % 2 != 0:
                print(3)
            elif N % 4 != 0:
                print(4)
            elif N % 4 == 0:
                print(2)
        elif (math.ceil(summ + 1)) % 2 != 0:
            if N % 2 != 0:
                print(3)
            elif N % 4 == 0:
                print(4)
            elif N % 4 != 0:
                print(2)

# print(summ + 1)
# print(math.ceil(summ + 1))
#  10 12 18 20 26 28 34 36 нечетный круг
#  6 8 14 16 22 24 30 32 38 40 четный круг
# a = N - 5
# A = a / 4
# num = A / 4 + 1
# print(math.ceil(num))
# N - 5 = A(n) A(n) // 4 = A(N) A(N)/4 + 1 = номер круга
#(5 * 2 (номер круга))-(2 (номер круга)-1) = 9 
#(5 * 3)-(3-1) = 13 