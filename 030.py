#import functions as funcs
#for i in range(8):
#    print(i*(9**5))

#ub = 354294
#s = set()
#for i in range(2,ub):
#    powerdigitsum = sum(int(x)**5 for x in str(i))
#    if powerdigitsum==i:
#       s.add(i)

#print(sum(set(i for i in range(2,ub) if (sum(int(x)**5 for x in str(i)) == i))))

#Below is a awaaaaaaaaaaaaaay better solution I found online

def sumPowerDigits(n: int, m: int=1) -> int:
    '''Return the sum of mth power of the digits of n.'''
    total = 0
    while n > 0:
        n, digit = divmod(n, 10)
        total += digit**m
    return total

def isPermutation(n: int | str, m: int | str) -> bool:
    '''Return whether m is a permutaton of n.'''
    nString = str(n)
    mString = str(m)
    if len(nString) == len(mString):
        for digit in mString:
            if digit not in nString:
                return False
            nString = nString.replace(digit, '', 1)
        else:
            return True
    else:
        return False

def answer30(m=5):
    '''Return the sum of all numbers which can be written as the sum of mth powers of their 
    own digits, using the fact that the sum of mth powers of the digits of a k-digit number 
    is at most k*9^m and the sum of mth power of the digits does not depend on the order of 
    the digits.'''
    numberList = []
    k = 1
    while not 10**(k - 1) <= k*9**m < 10**k:
        k += 1
    for digitCombination in itertools.combinations_with_replacement('0123456789', k):
        n = int(''.join(digitCombination))
        sumPowerDigit = sumPowerDigits(n, m)
        if isPermutation(str(sumPowerDigit).replace('0', ''), n):
            numberList.append(sumPowerDigit)
    print(numberList)
    return sum(numberList) - sum([1])

answer30()