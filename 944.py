from two_powers import fast2bin # type: ignore
import math 
def elevize(n):
    appearances = {}
    #appearances[1] = fast2bin(n-1,1234567891)-1
    #print(appearances[1])
    #for i in range()
    #print('hello world')
    #powdict = {}
    #powdict[n//2]=fast2bin(n//2,1234567891)
    #for i in range(n//2+1,n-1):
    #    print(i)
    #    powdict[i]=(powdict[i-1]*2)%1234567891
    #print(powdict)
    #for i in range(n//2,n-1):
        #print(i)
    #    powdict[i]=fast2bin(i,1234567891)
    #print(powdict)
    for i in range(2,n//2+1):
        #print(i)
        nums = set(x for x in range(n-n//i,n-1))
        appearances[i] = sum(fast2bin(x,1234567891) for x in nums)
    total = sum(i*appearances[i]%1234567891 for i in range(1,n//2+1))%1234567891
    return total

def main():
    mod = 1234567891
    n=(100)
    print(n)
    #print(fast2bin(10**14,n))
    #test2(n,mod)
    print(10000000**2%mod)
    print((n-100000)%mod)
    #print(2**(n-n/2))
    #print(2**(n-n//4))
    ##print(2**(n-n//8))
    #print(2**(n-n//16))
    print(2**(n-4))
    print(2**(n-25))
    print((2**n)/(2**(4)))
    #test(n)
    #print(elevize(n))
    #print(bin(480))
    #print(bin(2**9-(2**5)))
    #print(2**9-2**7)
    
def test(n):
    powers = {}
    powers[1] = 2
    for i in range(2,n+1):
        if i%10000000 == 0:
            print(i)
        powers[i] = (2*powers[i-1])%n
    print(powers[50000])
    print(powers[109286])

def test2(n, mod):
    #divs = set(n//i for i in range(2,n//2+1))
    #s = sorted(divs)
    rootset=set()
    for i in range(2,math.floor(math.sqrt(n)+1)):
        #if i%1000000==0:
            #print(i,n//i)
        rootset.add(i)
        #rootset.add(n//i)
    #for i in range(2,n//2+1):
       # print(i, (fast2bin(n-1,mod)-fast2bin(n-(n//i),mod))%mod)
    #for d in s:
    #    print(d, n/d)
    #print(len(divs))
    #print(rootset)
    #print(rootset==divs)
    #r = sorted(rootset)
    powerdict= {}
    powerdict[n-1]=fast2bin((n-1)%mod,mod)
    ro = sorted(rootset)
    for r in ro:
        if r%1000000==0:
            print(r)
        powerdict[r] = fast2bin(r%mod,mod)
        powerdict[n-n//r] = powerdict[n]/powerdict[r]
        #powerdict[n-r]=fast2bin((n-r)%mod,mod)
    print(powerdict)
    #for ro in rootset:
    #    print(ro)
    #for i in range(len(r)):
    #    print(r[i],s[i])
        #print(n - n//830)
    print(len(ro))

if __name__=='__main__':
    main()