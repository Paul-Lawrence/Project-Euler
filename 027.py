import primality

def countprimes(a,b, primes, n=0):
    num = n**2 +a*n + b
    if num not in primes:
        return n
    return countprimes(a,b,primes, n+1)

target = 1000
primes = set(primality.primes(1000000))
a_set = [n for n in range(1, target+1) if n%2==1] + [-n for n in range(1,target) if n%2==1]
b_set = [p for p in primality.primes(target+1)] + [-p for p in primality.primes(target+1)]
max_a = 0
max_b = 0
longchain = 0
for a in a_set:
    for b in b_set:
        n = countprimes(a,b,primes)
        if n > longchain:
            longchain = n
            max_a = a
            max_b = b
print(f'a: {max_a}, b: {max_b}, chain: {longchain}')
print(f'Chainproduct: {max_a*max_b}')