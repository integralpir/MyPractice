import math

m = float(input())
n = float(input())
p = float(input())
q = float(input())

def get_result(m,n,p,q):
    
        x1 = m / n
        x2 = p / q
        b = -(x1 + x2)
        c = x1 * x2
        if x1 == 0 and x2 == 0:
            a = 1 
        else:
            a = c / x1*x2
        print( int(a), int(b), int(c) )

get_result(m,n,p,q)
# D = b**2 - 4 * a * c
# x1 = m / n
# x2 = p / q
# x1 = -b + math.sqrt(D) / 2 * a
# x2 = -b - math.sqrt(D) / 2 * a