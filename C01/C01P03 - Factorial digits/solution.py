def fact_digits(n):
    # return sum(factorial(int(ch)) for ch in str(abs(n)))

    n = abs(n)

    result = 0
    while n != 0:
        digit = n % 10
        result += factorial(digit)
        n = n // 10

    return result


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


print(fact_digits(101) == 3)
print(fact_digits(111) == 3)
print(fact_digits(145) == 145)
print(fact_digits(999) == 1088640)
