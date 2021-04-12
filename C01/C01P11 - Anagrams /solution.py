def char_histogram(string):
    return {char: string.count(char) for char in set(string)}


def anagrams(word1, word2):
    word1 = word1.replace(' ', '').lower()
    word2 = word2.replace(' ', '').lower()
    histogram1 = char_histogram(word1)
    histogram2 = char_histogram(word2)
    return histogram1 == histogram2


print(anagrams("listen", "silent") is True)
print(anagrams("LISTEN", "silent") is True)
print(anagrams("python", "ruby") is False)
print(anagrams("New York Times", "monkeys writing") is True)  # BUG HERE!
