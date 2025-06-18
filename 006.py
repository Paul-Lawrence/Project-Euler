def main():
    n = 100
    sum_of_squares = n*(n+1)*(2*n+1)/6
    squared_sum = (n*(n+1)/2)**2
    difference = squared_sum-sum_of_squares
    print(squared_sum)
    print(sum_of_squares)
    print(difference)
    

main()