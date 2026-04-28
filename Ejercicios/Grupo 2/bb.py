cases = int(input())

def binary_search(X) :
    N = 2 * (10 ** 5)
    a = -1
    b = N
    while b - a > 1:
        c = (a+b) // 2
        if c ** 2 > X :
            b = c
        else :
            a = c
    if b < N and b ** 2 == X:
        return b
    return -1

""" from functools import reduce """

for i in range(cases):
    squares = 0
    buckets = int(input())
    """ for j in range(buckets): """
    """ squares += int(input) """
    squares = sum(map(int, input().split()))
    """ squares = reduce(lambda x, y: x*y, map(int, input().split())) """
    
    if (binary_search(squares) != -1):
        print("yes")
    else:
        print("no")
    
    