from collections import defaultdict, Counter


def char_histogram(string):
    """ RadoRado kaza 'NE!' :) """
    return {char: string.count(char) for char in set(string)}


def char_histogram2(string):
    dd = {}
    for char in string:
        if char not in dd:
            dd[char] = 0
        dd[char] += 1
    return dd


def char_histogram3(string):
    dd = defaultdict(int)
    for char in string:
        dd[char] += 1
    return dd


def char_histogram4(string):
    return Counter(string)


print(char_histogram3("") == {})
print(char_histogram3("    ") == {' ': 4})
print(char_histogram3("Python!") == {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1})
print(char_histogram3("AAAAaaa!!!") == {'A': 4, 'a': 3, '!': 3})
print(char_histogram3("Some very long string here with different casing") ==
      {
          'S': 1,
          'o': 2,
          'm': 1,
          'e': 6,
          ' ': 7,
          'v': 1,
          'r': 4,
          'y': 1,
          'l': 1,
          'n': 4,
          'g': 3,
          's': 2,
          't': 3,
          'i': 4,
          'h': 2,
          'w': 1,
          'd': 1,
          'f': 2,
          'c': 1,
          'a': 1
      })