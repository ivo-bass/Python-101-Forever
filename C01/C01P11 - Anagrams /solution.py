def char_histogram(string):
    dd = {}
    for char in string:
        dd[char] = dd.get(char, 0) + 1
    return dd


def anagrams(word1, word2):
    word1 = word1.replace(' ', '').lower()
    word2 = word2.replace(' ', '').lower()
    histogram1 = char_histogram(word1)
    histogram2 = char_histogram(word2)
    print(histogram1, histogram2)
    return histogram1 == histogram2


print(anagrams("listen", "silent") is True)
print(anagrams("LISTEN", "silent") is True)
print(anagrams("python", "ruby") is False)
print(anagrams("New York Times", "monkeys writing") is True)  # BUG HERE!
