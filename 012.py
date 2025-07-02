import sympy
import sympy.ntheory 

n = 1
upper = 50000
for i in range(2, upper):
    n += i
    pfactors = sympy.ntheory.factorint(n)
    divs = 1
    for v in pfactors.values():
        divs *= (v+1)
    #print(divs)
    if divs >= 500:
        print(n,divs)