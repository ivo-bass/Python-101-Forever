def sum_of_digits(n):
    # return sum(int(ch) for ch in str(abs(n)))

    absolute_n = abs(n)
    string_n = str(absolute_n)

    result = 0
    for char in string_n:
        result += int(char)

    return result


print(sum_of_digits(1325132435356) == 43)
print(sum_of_digits(123) == 6)
print(sum_of_digits(6) == 6)
print(sum_of_digits(10) == 1)
