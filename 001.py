def main():
    threes = set(range(3,1000,3))
    fives = set(range(5,1000,5))
    merged = threes.union(fives)
    print(merged)
    print(sum(merged))

if __name__=='__main__':
    main()
