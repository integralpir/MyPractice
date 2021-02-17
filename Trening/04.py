'''
s = input()

lst = list(s)

#print(sorted(lst, reverse=True))
s = ''.join(sorted(lst))

print(s[::-1])
'''

print(''.join(sorted(list(input())))[::-1])