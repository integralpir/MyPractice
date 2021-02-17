n = int(input())
min1 = 30000
for i in range (n):
    x = int(input())
    if x == 3:
        min1 = x
    if x >= 10 and x % 10 == 3 and x < min1:
        min1 = x
print(min1)