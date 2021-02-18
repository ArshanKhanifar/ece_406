def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


def test(params):
    for (a, b, ans) in params:
        result = "CORRECT" if ans == gcd(a, b) else "WRONG"
        print(f"{result} - gcd({a}, {b}) = {gcd(a, b)}")


if __name__ == '__main__':
    test([
        (1, 2, 1),
        (3, 4, 1),
        (36, 42, 6),
        (1035, 759, 69)  # nice
    ])
