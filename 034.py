import math
upper =  10
#for i in range(10):
#    print(i*math.factorial(9))
for i in range(3,upper):
    if sum(math.factorial(int(d)) for d in str(i)) == i:
        print(i, sum(math.factorial(int(d)) for d in str(i)))

print(145+40585)