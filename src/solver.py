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

def getAnagrams(str):
    dictionary = getDictionary()
    anagrams = []

    sorted = sortLetters(str)

    for anagram in dictionary[sorted]:
        anagrams.append(anagram.strip().lower())

    return anagrams

while True:
    print("Input a string (Enter to quit): ")
    str = input().lower()

    if str == "":
        break

    else:
        anagrams = getAnagrams(str)
        print('\n')

        for anagram in anagrams:
            print(anagram)
            print('\n')
