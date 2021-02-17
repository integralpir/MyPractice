# задача для определения цвета клетки на шахматной доске
n = input()
y = int(n[1])
x = ord(n[0])-64
'''
if y % 2 == 0:
    if x % 2 == 0:
        print('BLACK')
    else:
        print('WHITE')
else:
    if x % 2 == 0:
        print('WHITE')'
    else:
        print('BLACK')
'''
'''
if x%2 == y%2:
    print ('BLACK')
else:
    print ('WHITE')
'''
if (x + y)%2 == 0:
    print('BLACK')
else:
    print('WHITE')