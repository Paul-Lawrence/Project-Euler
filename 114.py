n=30
#print(tiles)
tiles = [1,1,2]+[0]*(n-3)
head_tiles = [0,0,1,2,3,4]+[0]*(n-6)
for i in range(3,n):
    if i>=6:    
        head_tiles[i]=i-1+sum(head_tiles[i-x]*(x-3) for x in range(4,i-1))
    tiles[i] = head_tiles[i]+tiles[i-1]
    #sum([tiles[x] for x in range(i)])-tiles[i-2]-head_tiles[i-4]+1
print(head_tiles)
print(tiles)