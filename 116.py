def calcred(n):
    red = [0]*n 
    red[0],red[1] = 1,2
    for i in range(2,n):
        red[i]=red[i-1]+red[i-2]
    return(red)

def calcgreen(n):
    green = [0]*n
    green[0],green[1],green[2] = 1,1,2
    for i in range(3,n):
        green[i]=green[i-1]+green[i-3]
    return green

def calcblue(n):
    blue = [0]*n
    blue[0],blue[1],blue[2],blue[3] = 1,1,1,2
    for i in range(4,n):
        blue[i]=blue[i-1]+blue[i-4]
    return blue 

n = 50
red = calcred(n)
green = calcgreen(n)
blue = calcblue(n)

print(sum([red[n-1]-1,green[n-1]-1,blue[n-1]-1]))
