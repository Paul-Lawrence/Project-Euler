n=50
tiles = [1,2,4,8]+[0]*(n-4)
for i in range(4,n):
    tiles[i]=tiles[i-1]+tiles[i-2]+tiles[i-3]+tiles[i-4]
print(tiles)