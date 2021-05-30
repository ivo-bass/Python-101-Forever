SPACE = ' '


def iban_formatter(iban):
    result = []
    counter = 0

    for char in iban:

        if char == SPACE:
            continue

        if counter == 4:
            result.append(SPACE)
            counter = 0

        result.append(char)
        counter += 1

    return ''.join(result)



def test():
    tests = (
        ("BG91UNCR70001864961754", "BG91 UNCR 7000 1864 9617 54"),
        ("BG80 BNBG 9661 1020 3456 78", "BG80 BNBG 9661 1020 3456 78"),
        ("BG14TTBB94005362446381", "BG14 TTBB 9400 5362 4463 81"),
        ("BG80BNBG96611020345678", "BG80 BNBG 9661 1020 3456 78")
    )

    for iban, expected in tests:
        result = iban_formatter(iban)
        print(f'{expected} ==? {result}')
        print(expected == result)
        print()


test()