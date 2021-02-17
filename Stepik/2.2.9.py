n = int(input())
A = []
if n % 2 == 0:
    for i in range(n):
        B = []
        if i % 2 == 0:
            for j in range(n):
                if j % 2 == 0:
                    B.append(' ')
                else:
                    B.append('X')
        else:
            for j in range(n):
                if j % 2 != 0:
                    B.append(' ')
                else:
                    B.append('X')
        A.append(B)
else:
    for i in range(n):
        B = []
        if i % 2 != 0:
            for j in range(n):
                if j % 2 == 0:
                    B.append(' ')
                else:
                    B.append('X')
        else:
            for j in range(n):
                if j % 2 != 0:
                    B.append(' ')
                else:
                    B.append('X')
        A.append(B)

for i in range(len(A)):
    print(*A[i], sep = '')