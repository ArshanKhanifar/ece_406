from assignments.a1p5 import expexp


def main():
    print('Test 1:', end = ' ')
    r = expexp(1, 1, 1, 2)

    if r == 1:
        print('Passed')
    else:
        print('Failed')


    print('Test 2:', end = ' ')
    r = expexp(2, 2, 2, 31)

    if r == 16:
        print('Passed')
    else:
        print('Failed')

    print('Test 3:', end = ' ')
    r = expexp(103, 12, 112, 127)

    if r == 1:
        print('Passed')
    else:
        print('Failed')

    print('Test 4:', end = ' ')
    r = expexp(104, 12, 112, 127)

    if r == 4:
        print('Passed')
    else:
        print('Failed')


if __name__ == '__main__':
    main()
