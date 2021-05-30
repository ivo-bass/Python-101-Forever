def char_histogram(string):
    dd = {}
    for char in string:
        dd[char] = dd.get(char, 0) + 1
    return dd


print(char_histogram("") == {})
print(char_histogram("    ") == {' ': 4})
print(char_histogram("Python!") == {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1})
print(char_histogram("AAAAaaa!!!") == {'A': 4, 'a': 3, '!': 3})
print(char_histogram("Some very long string here with different casing") ==
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
