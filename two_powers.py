import math
import sys
sys.set_int_max_str_digits(1000000000)

class two_pow():
    def __init__(self, upper_bound):
        self.table = {}
        

def fast2mod(pow, mod):
    y = int(math.log(pow, 2))
    #print(y)
    x = 2
    for i in range(y):
        x = (x**2)%mod
    return x

def fast2binmod(pow, mod):
    x = 1
    b = str(bin(pow))[:1:-1]
    #print(b)
    for i in range(len(b)):
        #print(i)
        if b[i]=='1':
            x = (x*fast2mod(2**i,mod))%mod
        else:
            pass
    return x

def fast2(pow):
    y = int(math.log(pow, 2))
    #print(y)
    x = 2
    for i in range(y):
        x = (x**2)
    return x

def fast2bin(pow):
    x = 1
    b = str(bin(pow))[:1:-1]
    #print(b)
    for i in range(len(b)):
        #print(i)
        if b[i]=='1':
            x = (x*fast2(2**i))
        else:
            pass
    return x

def main():
    n = 10**14
    #print(2**n)
    print(fast2bin(n,1234567891))



if __name__=='__main__':
    main()
