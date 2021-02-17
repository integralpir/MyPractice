odd = 0
even = 0
A = [ ]
A = input().split(' ')
N = len(A)
for i in range(N):
    A[i] = int(A[i])
    if A[i] % 2 == 0:
        even += 1
    else:
        odd += 1
if even > odd:
    print('even')
if odd > even:
    print('odd')
if odd == even:
    print('equal')           