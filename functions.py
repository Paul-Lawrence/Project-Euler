import math
import sympy.ntheory.factor_ as factor

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def divcount(n): #Gives me the sums of divisors for every number less than n
    # Set how many numbers we are testing
    # Initialize a list to avoid memory reallocation
    # Set 1 as initial value as all numbers are divisible by 1
    SUMS = [1] * (n + 1)
# Take every number and add it to all its multiples not grater than MAX
# No number not grater than MAX will have a divisor higher than MAX / 2
    for i in range(2, (n + 1) // 2):
    # Don't start at i to avoid adding i to its own sum
        for index in range(i * 2, n + 1, i):
        # i is a divisor of index
            SUMS[index] += i
    return SUMS


def divisors(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    #print(large_divisors)
    #for divisor in reversed(large_divisors):
    #    yield divisor
    return large_divisors

def prime_factors(n):
    return factor.factorint(n)

def num_factors(primefactors):
    return math.prod(primefactors[x]+1 for x in primefactors)

def multiply_factors(primefactors):
    x = 1
    for fact in primefactors:
        x*=(fact**primefactors[fact])
    return x

def multiply_factors_mod(primefactors, base):
    x = 1
    for fact in primefactors:
        #if fact
        x= (x*(fact**primefactors[fact]))%base
        #print(fact,primefactors[fact],x)
    return x