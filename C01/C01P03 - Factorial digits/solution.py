def fact_digits(n):
    return sum(factorial(int(s)) for s in str(abs(n)))

def factorial(n):
    fact = 1
    for i in range(1, n+1): 
        fact *= i
    return fact


print(fact_digits(101))
print(fact_digits(111))
print(fact_digits(145))
print(fact_digits(999))
