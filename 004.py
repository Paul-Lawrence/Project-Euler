def ispal(n):
    return recurse(str(n))

def recurse(s):
    if len(s)==0 or len(s)==1:
        return True
    elif s[0]==s[-1]:
        return recurse(s[1:-1])
    else:
        return False
    
def twodigit_method():
    for i in range(100,1000):
        for j in range(100,1000):
            x = i*j
            if ispal(x):
                print(x)

twodigit_method()
#string = '00'
#print(string[0])