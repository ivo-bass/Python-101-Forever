def is_palindrome(number):
    num_list = [s for s in str(number)]
    reversed_list = list(reversed(num_list))
    return num_list == reversed_list


def build_cache():
    dd = {}
    for number in range(11, 100000):
        dd[number] = is_palindrome(number)
    return dd


CACHE = build_cache()


def palindromes_count(n):
    count = 0
    for number in range(11, n+1):
        if CACHE[number]:
            count += 1
    return count


print(palindromes_count(10) == 0)
print(palindromes_count(20) == 1)  # only 11
print(palindromes_count(101) == 10)  # 11, 22, 33, 44, 55, 66, 77, 88, 99, 101
print(palindromes_count(359) == 35)
print(palindromes_count(1698) == 106)
print(palindromes_count(5098) == 140)
print(palindromes_count(10001) == 190)
print(palindromes_count(92009) == 1009)
print(palindromes_count(99999) == 1089)
