import functions as funcs
import math
import primality
from sortedcontainers import SortedDict

def findnextfactor(factors,next_list):
    minmult = nextprime
    minfact = nextprime
    minpow = 1
    for fact in factors:
        a = fact**(factors[fact]+1)
        if a<minmult:
            minmult = a
            minfact = fact
            minpow = factors[fact]+1
    return [minfact,minpow]
    #if minfact == nextprime:
    #    factors[nextprime] = 1
    #else:
    #    factors[minfact]+=minpow
    #return factors


def next_factor(next_dict):
    return next_dict.popitem(index=0)





test_set = {1: 2, 2: 6, 3: 24, 4: 120, 5: 840, 6: 7560, 7: 83160, 8: 1081080}
n=500500
base = 500500507
primes = iter(primality.primes(9000000))
next(primes)
nextprime = next(primes)
factors = {2:1}
number = 2
D = SortedDict({4: 2, 3:3})
for i in range(n-1):
    if i%10000==0:
        print(i)
    F = next_factor(D)
    next_fact = F[1]
    multiplicand = F[0]
    #print(D,next_fact)
    #print(D)
    #print(factors)
    if next_fact == nextprime:
        factors[nextprime]= 1
        D[nextprime**2] = nextprime
        nextprime = next(primes)
        D[nextprime] = nextprime
    else:
        factors[next_fact] = factors[next_fact]*2+1
        D[next_fact**(factors[next_fact]+1)] = next_fact
        #print(next_fact)
        #print(D)
    number = (number*multiplicand)%base
    #print(i+2,funcs.multiply_factors(factors))
    #print(factors)
    #print(D)
print(factors)
print(n,number)
#for i in range(n-1):
#    if i%10000==0:
#        print(i)
#        print(factors)
#    nextfact = findnextfactor(factors,nextprime)
#    minfact,minpow = nextfact[0],nextfact[1]
#    if minfact == nextprime:
#        factors[nextprime] = 1
#        nextprime = next(primes)
#    else:
#        factors[minfact]+=minpow
    #print(funcs.multiply_factors_mod(factors,base), funcs.num_factors(factors),factors)
#print(funcs.multiply_factors_mod(factors,base))

#for x in range(n):
#    factors = funcs.prime_factors(x)
#    t = funcs.num_factors(factors)
    #if math.log(t,2).is_integer():
#    if t == base:
#        print(x, funcs.num_factors(factors),factors)
#        base*=2