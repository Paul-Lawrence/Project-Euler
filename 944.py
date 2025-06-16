def elevize(n):
    appearances = {}
    appearances[1] = (2**(n-1)-1)%1234567891
    print('hello world')
    for i in range(2,n//2+1):
        print(i)
        nums = set(x for x in range(n-n//i,n-1))
        appearances[i] = sum((2**x)%1234567891 for x in nums)
    total = sum(i*appearances[i] for i in range(1,n//2+1))%1234567891
    return total

def main():
    n = 10**14
    print(elevize(n))

if __name__=='__main__':
    main()