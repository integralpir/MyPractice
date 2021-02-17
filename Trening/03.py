'''
n = int (input())
one = [ ]
zero = [ ]
for i in range (n):
    N = int(input())
    if N == 1:
        one.append('1')
    else:
        zero.append('0')

if len(one) > len(zero):
    print(n - len(one))
else:
    print(n - len(zero))
'''
'''
lst = [int(input()) for i in range(int(input()))]

print(min(sum(lst), len(lst) - sum(lst)))
'''
