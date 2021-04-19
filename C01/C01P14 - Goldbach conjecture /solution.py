"""
Implement a function, called goldbach which takes an integer n, and returns a list of tuples, that is the goldbach conjecture for the given number.

The Goldbach conjecture states:

Every even integer greater than 2 can be expressed as the sum of two primes.

Keep in mind that there can be more than one combination of two primes, that sums up to the given number.

In case an odd integer is given, return None.

The result should be sorted by the first item in the tuple.

For example:

4 = 2 + 2
6 = 3 + 3
8 = 3 + 5
10 = 3 + 7 = 5 + 5
100 = 3 + 97 = 11 + 89 = 17 + 83 = 29 + 71 = 41 + 59 = 47 + 53
"""


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num // 2 + 1):
        if (num % i) == 0:
            return False
    return True


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


def goldbach(n):
    if n % 2 == 1:
        return None
    pairs = []
    primes = prime_numbers_generator()
    prime_1 = next(primes)
    while prime_1 * 2 <= n:
        prime_2 = n - prime_1
        if is_prime(prime_2):
            pairs.append((prime_1, prime_2))
        prime_1 = next(primes)
    return pairs


print(goldbach(4) == [(2, 2)])
print(goldbach(6) == [(3, 3)])
print(goldbach(8) == [(3, 5)])
print(goldbach(10) == [(3, 7), (5, 5)])
print(goldbach(100) == [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)])
print(goldbach(5) is None)
print(goldbach(-1) is None)