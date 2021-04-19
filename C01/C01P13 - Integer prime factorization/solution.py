"""
Given an integer n, we can factor it in the following form:

n = p1^a1 * p2^a2 * ... * pn^an
Where each p is a prime number and each a is an integer and p^a means p to the power of a.

This is called prime factorization

Lets see few examples:

10 = 2^1 * 5^1
25 = 5^2
356 = 2^2 * 89 ^ 1
"""


def update_dict(dd, factor):
    if factor not in dd:
        dd[factor] = 1
    else:
        dd[factor] += 1


def prime_numbers_generator():
    dd = {}
    q = 2
    while True:
        if q not in dd:
            yield q
            dd[q * q] = [q]
        else:
            for p in dd[q]:
                dd.setdefault(p + q, []).append(p)
            del dd[q]
        q += 1


def prime_factorization(n):
    primes = prime_numbers_generator()
    i = next(primes)
    factors = {}
    while i <= n:
        if n % i != 0:
            i = next(primes)
        else:
            n //= i
            update_dict(factors, i)
    if n > 1:
        update_dict(factors, i)

    return [(key, value) for key, value in factors.items()]


print(prime_factorization(8))
print(prime_factorization(10))  # This is 2^1 * 5^1
print(prime_factorization(14))
print(prime_factorization(356))
print(prime_factorization(89))  # 89 is a prime number
print(prime_factorization(1000))

print(prime_factorization(10) == [(2, 1), (5, 1)])  # This is 2^1 * 5^1
print(prime_factorization(14) == [(2, 1), (7, 1)])
print(prime_factorization(356) == [(2, 2), (89, 1)])
print(prime_factorization(89) == [(89, 1)])  # 89 is a prime number
print(prime_factorization(1000) == [(2, 3), (5, 3)])
