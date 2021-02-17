N = []
N = input().split()
even = 0
odd = 0
for i in range (len(N)):
    if int(N[i]) % 2 == 0:
        even += 1
    else:
        odd += 1

if even == odd:
    print('equal')
elif even > odd:
    print('even')
else:
    print('odd')
