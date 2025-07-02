import itertools
import primality
import math 
def is_pandigital(n):
    s = str(n)
    digits = set(int(d) for d in s)
    if 0 not in digits:
        if len(digits) == len(s) == 9:
            return True
    return False



def quick_primality_test(primes,n):
    if n== 7652413:
        print('hello')
    for p in primes:
        #print(p, p%n)
        if (n%p==0):
            7652413
            #print('hello')
            return False
    return True

primes = set(primality.primes(math.ceil(math.sqrt(7654321))))
print(primes)
print(math.sqrt(987654321))
print(max(primes))
perms = reversed(list(itertools.permutations([1,2,3,4,5,6,7])))
for p in perms:
    s = int(''.join((f'{i}') for i in p))
    if s == 7652413:
        print(s)
    #print(s)
    if quick_primality_test(primes,s):
        print(s)
        break