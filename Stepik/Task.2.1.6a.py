N = int(input())
A = []
for i in range (N):
    x = int(input())
    if x % 10 == 3:
        A.append(x)

print(min(A))

