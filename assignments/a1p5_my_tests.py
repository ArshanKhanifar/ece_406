from assignments.a1p5 import modexp


def test_modexp(cases):
    for a, b, c, d in cases:
        out = modexp(a, b, c)
        result = "PASS" if out == d else "FAIL"
        print(f"modexp({a}, {b}, {c}): {out} == {d} - {result}")


if __name__ == '__main__':
    test_modexp([
        (1, 1, 2, 1),
        (2, 1, 3, 2),
        (2, 5, 3, 2),
        (3, 2, 7, 2),
        (3, 3, 6, 3),
        (11, 14, 57, 7)
    ])
