def is_number_balanced(number):
    numbers_list = [int(n) for n in str(number)]
    mid_index = len(numbers_list) // 2
    left = sum(numbers_list[:mid_index])
    if not len(numbers_list) % 2 == 0:
        mid_index += 1
    right = sum(numbers_list[mid_index:])
    return left == right


print(is_number_balanced(9) is True)
print(is_number_balanced(4518) is True)
print(is_number_balanced(28471) is False)
print(is_number_balanced(1238033) is True)
