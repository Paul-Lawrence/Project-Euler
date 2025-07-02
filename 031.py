from numpy.polynomial import Polynomial as P
import numpy
n = 200
coinset = [1,2,5,10,20,50,100,200]
table = [1]+[0]*(n)
for i in range(1,n+1):
    table[i] =table[i-1]
    for coin in coinset:
        if (coin<=i) and (i%coin == 0):
            table[i]+=1
#print(table)
#print(table[-1])
sums = {0: set({1:0,2:0,5:0,10:0,20:0,50:0,100:0,200:0})}
coinsums = [[0 for i in range(len(coinset))] for j in range(n+1)]
for j in range(len(coinset)):
        coinsums[1][j] = 1
        coinsums[0][j] = 1
for j in range(len(coinset)):
     for i in range(2,n+1):
        if coinset[j]>i:
            coinsums[i][j] = coinsums[i][j-1]
        else:
             coinsums[i][j] = coinsums[i][j-1]+coinsums[i-coinset[j]][j]
print(coinsums[n][len(coinset)-1])
#print(coinsums)
