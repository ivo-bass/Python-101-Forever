def sum_of_digits(n):
    return sum(int(s) for s in str(abs(n)))


print(sum_of_digits(1325132435356))
print(sum_of_digits(123))
print(sum_of_digits(6))
print(sum_of_digits(10))