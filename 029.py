print(99*99)

n = 100
upper_bound = (n-1)**2
#repeatingset = set()
#powerdict = {x**i: i for i in range(2,7) for x in range(2,11) if x**i <=n}
#baseset = set(powerdict.keys())
subtractsum = 0
#for i in range(2,n+1):
#    if i in baseset:
#        subtractsum+=(n//powerdict[i]-1)
#print(subtractsum)
#print(baseset)
#print(powerdict)
#print(upper_bound-subtractsum)


for i in range(2,11):
    for j in range(2,7):
        if i**j <=n:
            subtractsum+= (n//j-1)
print(upper_bound-subtractsum)