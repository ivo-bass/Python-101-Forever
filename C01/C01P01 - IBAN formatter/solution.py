from time import time


def get_time(func):
    def wrapper(iban):
        start = time()
        result = func(iban)
        end = time()
        exec_time = end - start
        info = func.__name__
        return result, exec_time, info

    return wrapper


@get_time
def iban_formatter_string_concatenator(iban):
    iban = iban.replace(' ', '')
    formatted = ''

    for index, char in enumerate(iban):
        if index % 4 == 0 and index > 0:
            formatted += ' '
        formatted += char

    return formatted


@get_time
def iban_formatter_append_to_list(iban):
    iban = iban.replace(' ', '')
    ll = []

    for index, char in enumerate(iban):
        if index % 4 == 0 and index > 0:
            ll.append(' ')
        ll.append(char)

    return ''.join(ll)


@get_time
def iban_formatter_slicing_comprehension(iban):
    iban = iban.replace(' ', '')
    result = [iban[i:i + 4] for i in range(0, len(iban), 4)]
    return ' '.join(result)


@get_time
def iban_formatter_for_loop_slicing(iban):
    iban = iban.replace(' ', '')
    ll = []
    for i in range(0, len(iban), 4):
        ll.append(iban[i:i + 4])
    return ' '.join(ll)


formatters = (
    iban_formatter_string_concatenator,
    iban_formatter_append_to_list,
    iban_formatter_slicing_comprehension,
    iban_formatter_for_loop_slicing
)

tests = (
    ("BG91UNCR70001864961754", "BG91 UNCR 7000 1864 9617 54"),
    ("BG80 BNBG 9661 1020 3456 78", "BG80 BNBG 9661 1020 3456 78"),
    ("BG14TTBB94005362446381", "BG14 TTBB 9400 5362 4463 81"),
    ("BG80BNBG96611020345678", "BG80 BNBG 9661 1020 3456 78")
)

for func in formatters:
    for iban, expected in tests:
        result, exec_time, info = func(iban)
        print(info)
        print(f'{expected} == {result}')
        print(expected == result)
        print(exec_time)
        print()
