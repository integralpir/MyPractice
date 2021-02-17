N = int(input())
X = input().split()
sum = 0
for i in range (10):
    x = int(X[i])
    sum = sum + x
    if sum > N:
        break 
    
if sum >= N:
    print (i+1)
else:
    print('-1')
    
    


#1 2 3 4 5 6 7 8 9 10