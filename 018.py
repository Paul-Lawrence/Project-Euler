lines = open('0067_triangle.txt', 'r').readlines()
triangle = [[int(num) for num in line.split(' ')] for line in lines]
maxpath = [[0]*len(row) for row in triangle]
maxpath[-1] = triangle[-1]
for i in range(len(triangle)-2,-1,-1):
    for j in range(len(triangle[i])):
        maxpath[i][j] = triangle[i][j]+max(maxpath[i+1][j],maxpath[i+1][j+1])
print(maxpath[0])