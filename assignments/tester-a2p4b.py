#! /usr/bin/python3
from assignments.a2p4b import nshortestpaths

"""
Some tests.

If you set this file to executable, and have the a1p4b.py file in
the same folder, then you should be able to run this. You can and should
of course try your own tests.
"""


def main():
    print('Test 1:', end = ' ')
    G = [[[1, 2], [3, 1]], [[0, 2], [3,1],[2,2]], [[1,2]], [[1, 1], [0, 1]]]
    a = 0
    b = 1
    n = nshortestpaths(G, a, b)

    if n == 2:
        print('Passed')
    else:
        print('Failed')


    print('Test 2:', end = ' ')
    a = 0
    b = 2
    n = nshortestpaths(G, a, b)

    if n == 2:
        print('Passed')
    else:
        print('Failed')

    print('Test 3:', end = ' ')
    a = 0
    b = 3
    n = nshortestpaths(G, a, b)

    if n == 1:
        print('Passed')
    else:
        print('Failed')

    print('Test 4:', end = ' ')
    G.append([])
    a = 0
    b = 4
    n = nshortestpaths(G, a, b)

    if n == 0:
        print('Passed')
    else:
        print('Failed')

    print('Test 5:', end = ' ')
    # example adapted from textbook
    G = [[[1,4],[2,2]], [[0, 4],[2,1],[3,2],[4,3]], [[0,2],[1,1],[4,5],[3,4]], [[1,2],[2,4],[4,1]], [[1,3],[3,1],[2,5]]]
    a = 0
    b = 4
    n = nshortestpaths(G, a, b)

    if n == 2:
        print('Passed')
    else:
        print('Failed')

    print('Test 6:', end = ' ')
    b = 3
    n = nshortestpaths(G, a, b)

    if n == 1:
        print('Passed')
    else:
        print('Failed')


if __name__ == '__main__':
    main()
