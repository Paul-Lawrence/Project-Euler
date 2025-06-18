import scipy 
def first_try(n):
    grid = [[0 for i in range(n-1)]+ [1] for i in range(n-1)]
    grid.append([1 for i in range(n)])
    print(grid)
    for i in range(n-2,-1,-1):
        for j in range(n-1,-1,-1):
            if j==n-1:
                grid[i][j]=1
            else:
                grid[i][j]=grid[i+1][j]+grid[i][j+1]
                #print(i,j,grid[i+1][j],grid[j][i+1],grid[i+1][j]+grid[i][j+1])
    #grid[2][2]=grid[3][2]+grid[2][3]
    return grid[0][0]

def better_solution(n):
    count = 1
    numerator = 1
    denom = 1
    for i in range(1,n+1):
        numerator *= (n+i)
        denom *= i
        count= count* ((n+i)/i)
    return(numerator/denom)
    #return count

n = 21
print(first_try(n))
print(better_solution(n-1))