from collections import deque


def is_credit_card_valid_old_solution(number):
    digits = [int(s) for s in str(number)]
    result_digits = []
    counter = 1
    while digits:
        if counter == 2:
            num = digits.pop() * 2
            if num >= 10:
                num = sum([int(s) for s in str(num)])
            counter = 1
        else:
            num = digits.pop()
            counter += 1
        result_digits.append(num)
    return sum(result_digits) % 10 == 0


# ____NEW_SOLUTION____
def is_credit_card_valid(number):
    digits = deque(int(s) for s in str(number))
    for i in range(len(digits)):
        num = digits.pop()
        if not i % 2 == 0:
            num *= 2
            if num >= 10:
                num = sum([int(s) for s in str(num)])
        digits.appendleft(num)
    return sum(digits) % 10 == 0


print(is_credit_card_valid(79927398713) is True)
print(is_credit_card_valid(79927398715) is False)
print(is_credit_card_valid(4417123456789113) is True)
