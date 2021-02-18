"""
Due to fermat's little theorem, since p is prime, then:
            x ^ (p - 1) = 1 (mod p)
Now by raising the left-hand side to any exponent, we can get multiples of (p - 1) i.e.
            x ^ (p - 1) = x ^ 2(p - 1) = x ^ 3(p - 1) = 1 (mod p)
Therefore for any arbitrary exponent a, we can keep decreasing (p - 1) from it until we
get a smaller value:
            x ^ a = x ^ (a mod (p-1))  (mod p)
My proposed solution works as follows:
    1. we first calculate y ^ z mod (p - 1) = a
    2. we then calculate x ^ a mod p

To calculate modulus exponentiation, I've employed the algorithm modexp(a, b, c) given in the
lecture notes. Let n = log(max(a, b, c)), then the complexity of this algorithm is as follows:
    1. With each call, b loses a bit, so there's a total of n calls
    2. Inside each call, there's one or two multiplications, and a modulus division,
       which are all O(n^2).
Therefore the complexity of modexp(a, b, c) is O(n^3).

The answer of this question, expexp(x, y, z, p) consists of two calls to modexp. Therefore the
complexity of expexp(x, y, z, p) is also O(n^3).
"""


def modexp(a, b, c):
    if b == 0:
        return 1
    k = modexp(a, b >> 1, c)
    sq = (k * k) % c
    if b & 1:
        return (a * sq) % c
    return sq


def expexp(x, y, z, p):
    exponent = modexp(y, z, p - 1)
    return modexp(x, exponent, p)



