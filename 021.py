import functions

n = 10000
sums = functions.divcount(n)
amicable = set()
for i in range(2,n):
    if sums[i] < n:
        if i == sums[sums[i]] and i!=sums[i]:   
            amicable.add(i)
            amicable.add(sums[i])
print(amicable)
print(sum(amicable))