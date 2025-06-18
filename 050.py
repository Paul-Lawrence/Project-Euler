import primality # type: ignore
print('hello world')
primes = primality.primes(1000000)
primeset = set(primes)
longprime = 0
sumlength = 0
for i in range(len(primes)):
    for j in range(i+1,len(primes)):
        if i%10000==0:
            if j%10000==0:
                print(primes[i],j)
        primesum = sum(primes[i:j])
        if primesum in primeset:
            if (j-i > sumlength):
                sumlength = j-i
                longprime = primesum
                print(primesum,sumlength)
                #print([primes[x] for x in range(i,j)])
