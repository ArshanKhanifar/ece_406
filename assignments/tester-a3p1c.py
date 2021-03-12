#! /usr/bin/python3

import sys
import random
from assignments.a3p1c import robotpath

"""
Some tests.
"""


def main():
    # First, a couple of simple 2x2 grid tests
    n = 2
    c = dict()
    c[str([[1,1],[2,1]])] = 1
    c[str([[1,1],[2,2]])] = 1000
    c[str([[1,2],[2,1]])] = 1000
    c[str([[1,2],[2,2]])] = 1

    print('Test 1:', end = ' ')
    src = [1,1]
    p = robotpath(n, src, c)

    if p and len(p) == 2 and p[0] == [1,1] and p[1] == [2,1]:
        print('Passed')
    else:
        print('Failed')

    print('Test 2:', end = ' ')
    src = [1,2]
    p = robotpath(n, src, c)

    if p and len(p) == 2 and p[0] == [1,2] and p[1] == [2,2]:
        print('Passed')
    else:
        print('Failed')

    print('Test 3:', end = ' ')
    # A 4x4 grid
    n = 4
    src = [1,2]

    c = dict()

    # 1st row
    for i in range(1,5):
        c[str([[1,i],[2,i]])] = 1
        if i - 1 > 0:
            c[str([[1,i],[2,i-1]])] = 1
        if i + 1 <= n:
            c[str([[1,i],[2,i+1]])] = 1
    c[str([[1,2],[2,2]])] = 1000

    #2nd row
    for i in range(1,5):
        c[str([[2,i],[3,i]])] = 1000
        if i - 1 > 0:
            c[str([[2,i],[3,i-1]])] = 1000
        if i + 1 <= n:
            c[str([[2,i],[3,i+1]])] = 1000
    c[str([[2,2],[3,2]])] = 1

    #3rd row
    for i in range(1,5):
        c[str([[3,i],[4,i]])] = 1000
        if i - 1 > 0:
            c[str([[3,i],[4,i-1]])] = 1000
        if i + 1 <= n:
            c[str([[3,i],[4,i+1]])] = 1000
    c[str([[3,2],[4,2]])] = 1

    p = robotpath(n, src, c)

    if p and len(p) == 4 and p[0] == [1,2] and p[2] == [3,2] and p[3] == [4,2]:
        print('Passed')
    else:
        print('Failed')

    print('Test 4: correctness will be checked at marking-time.')
    # A random grid between 3x3 and 10x10
    n = random.randint(3,10)

    # a random source square
    src = [1,random.randint(1,n)]

    # random costs between 1 and 10
    c = dict()
    for i in range(1,n):
        for j in range(1,n+1):
            # [i,j] is our "from" square
            c[str([[i,j],[i+1,j]])] = random.randint(1, 10)
            if j - 1 > 0:
                c[str([[i,j],[i+1,j-1]])] = random.randint(1, 10)
            if j + 1 <= n:
                c[str([[i,j],[i+1,j+1]])] = random.randint(1, 10)

    p = robotpath(n, src, c)
    print('Grid is', n, 'x', n, '. Source square is', src)
    print('Path found:', p)


if __name__ == '__main__':
    main()
