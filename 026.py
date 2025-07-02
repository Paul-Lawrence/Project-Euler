import primality
#print(primality.primes(1000))

def calcorder(n,m):
    base = n%m 
    if base == 1 or base == 0:
        return base
    num = n%m
    for i in range(2,m):
        num = (num*n)%m
        if num == 1:
            return i
        elif num == 0:
            return 0
        elif num == base:
            return 1

print([calcorder(10,i) for i in range(1,1000)])
#for i in range(1,1000):
#    print(i, calcorder(10,i))

#print(calcorder(10,17))