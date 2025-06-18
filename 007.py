import primality # type: ignore

def largeprime(n,index):
    primes = primality.primes(n)
    print(primes)
    return primes[index-1]

def main():
    n=1000000
    index = 10001
    print(largeprime(n,index))

if __name__=='__main__':
    main()