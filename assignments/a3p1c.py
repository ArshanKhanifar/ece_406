"""
ECE406, W'21, Assignment 3, Problem 1(c) 
Skeleton solution file.
"""

"""
You are not allowed to import anything. If we see any import
statement, you earn an automatic 0.
"""


def robotpath(n, src, c):
    """
    You need to implement this method.

    You are certainly allowed to define any subroutines you want
    above this method in this file.

    We will test with inputs that match the spec only --- a string
    str([[a,b], [c,d]]) is a valid key of c if and only if a move
    [a,b] to [c,d] is valid. src is a valid source square, i.e.,
    s[0] == 1. You should return a list, which is a path from the src
    square to one of the destination squares that is the cheapest
    from src to one of the destination squares.
    """
    L = {}
    T = {}
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1:
                L[(i, j)] = float('inf')
                T[(i, j)] = None
                if [i, j] == src:
                    L[(i, j)] = 0
                continue
            current = (i, j)
            bottom = (i - 1, j)
            bottom_left = (i - 1, j - 1)
            bottom_right = (i - 1, j + 1)
            prev_options = {"bottom": bottom}
            if j == 1:
                prev_options["bottom_right"] = bottom_right
            elif j == n:
                prev_options["bottom_left"] = bottom_left
            else:
                prev_options["bottom_right"] = bottom_right
                prev_options["bottom_left"] = bottom_left
            costs = {}
            for option in prev_options:
                prev = prev_options[option]
                cost = L[prev] + c[str([list(prev), list(current)])]
                costs[option] = cost
            min_cost = min(*costs.values())
            L[(i, j)] = min_cost
            min_option = [option for option in costs.keys() if costs[option] == min_cost][0]
            T[(i, j)] = prev_options[min_option]

    min_destination = []
    min_dest_cost = float('inf')
    for j in range(1, n + 1):
        target = (n, j)
        target_cost = L[target]
        if target_cost < min_dest_cost:
            min_dest_cost = target_cost
            min_destination = target

    best_path = []
    it = min_destination
    while it is not None:
        best_path[:0] = [it]
        it = T[it]
    return [[*s] for s in best_path]


if __name__ == '__main__':
    n = 2
    c = dict()
    c[str([[1,1],[2,1]])] = 1
    c[str([[1,1],[2,2]])] = 1000
    c[str([[1,2],[2,1]])] = 1000
    c[str([[1,2],[2,2]])] = 1
    print(c)
    src = [1,1]
    p = robotpath(n, src, c)

    if p and len(p) == 2 and p[0] == [1,1] and p[1] == [2,1]:
        print('Passed')
    else:
        print('Failed')


