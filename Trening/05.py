

x,y,z,w = map(int, input().split())
'''
count = 0
for a in range(w//x + 1):
    for b in range (101):
            t = w -(a*x + b*y)
            if t >= 0 and t % z:
                count += 1
print(count)
'''

def get(a,b,c):
    global lst
    if a * x + b * y + c * z == w:
        lst.add( (a,b,c) )
    if (a + 1) * x + b * y + c * z <= w:
        get(a + 1, b, c)
    if a * x + (b + 1) * y + c * z <= w:
        get(a, b + 1, c)
    if a * x + b * y + (c + 1) * z <= w:
        get(a, b, c + 1)

lst = set(x,y,z)
