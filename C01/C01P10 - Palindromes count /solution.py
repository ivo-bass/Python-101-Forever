def palindromes_count(n):
    count = 0
    for number in range(10, n+1):
        num_list = [s for s in str(number)]
        reversed_list = list(reversed(num_list))
        if num_list == reversed_list:
            count += 1
    return count


print(palindromes_count(10) == 0)
print(palindromes_count(20) == 1)  # only 11
print(palindromes_count(101) == 10)  # 11, 22, 33, 44, 55, 66, 77, 88, 99, 101
print(palindromes_count(92009) == 1009)
print(palindromes_count(99999) == 1089)
