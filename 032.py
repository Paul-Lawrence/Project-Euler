import itertools 
import math
products = set()
perms = [''.join((f'{i}' for i in set)) for set in list(itertools.permutations('123456789'))]
for perm in perms:
    #print(perm)
    #perm = int(''.join((f'{i}') for i in set))
    for i in range(1,7):
        for j in range(i+1,8):
            a = int(perm[0:i+1])
            b=int(perm[i+1:j+1])
            product = int(perm[j+1:])
            if a*b==product:
                print(a,b,product)
                products.add(product)
#print(math.prod(products))
print(sum(products))
