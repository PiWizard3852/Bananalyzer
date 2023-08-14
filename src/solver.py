from collections import defaultdict
from functools import lru_cache


def sortLetters(str):
    return ''.join(sorted(str.strip().lower()))


@lru_cache
def getDictionary():
    dictionary = defaultdict(set)

    with open("dictionary.txt", "r") as words:
        for word in words:
            sorted = sortLetters(word)
            dictionary[sorted].add(word.strip().lower())

    return dictionary


def getPlayableWords(letters):
    dictionary = getDictionary()
    words = []

    for key in dictionary:
        if letters.issuperset(key):
            for word in dictionary[key]:
                words.append(word)

    return sorted(words, key=len, reverse=True)


while True:
    print("Input a string (Enter to quit): ")
    str = input().lower()

    if str == "":
        break

    else:
        anagrams = getPlayableWords(set(str))
        print('\n')

        for anagram in anagrams:
            print(anagram)

        print('\n')
