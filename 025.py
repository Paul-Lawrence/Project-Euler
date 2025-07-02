a=1
b=1
index = 2
while (len(str(b))<1000):
    c=a+b
    a=b
    b=c
    index +=1
print(index)