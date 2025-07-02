m=50
tiles = [1]*(m)+[2]
n = tiles[-1]
while n < 1000000:
    tiles = tiles + [2*tiles[-1]-tiles[-2]+tiles[-m-1]]
    n = tiles[-1]
print(tiles)
print(len(tiles)-1)