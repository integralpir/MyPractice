n = int(input())
A = []
for i in range(n):
    A.append(input())

del A[0]
del A[-1]
summ = 0
for i in range(len(A)):
    A[i] = A[i][1:-1]
    summ += A[i].count('X')

print(summ)