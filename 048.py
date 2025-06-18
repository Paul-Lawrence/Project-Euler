import sympy.ntheory.factor_ as factor
#facts = factor.factorint(100)
n = 1000
mod = 10000000000
#for key in facts.keys():
#    n = n**(key**facts[key])
#    print(n)
#print(n)

sum = 0
for i in range(1,n+1):
    facts = factor.factorint(i)
    j=i
    for key in facts.keys():
        j = j**(key**facts[key])%mod
        print(j)
    sum += j%mod
print(sum%mod)
    