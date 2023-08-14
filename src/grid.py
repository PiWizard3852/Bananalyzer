def getGridDimensions():
    longest = ""

    with open("dictionary.txt", "r") as words:
        for word in words:
            if len(word) > len(longest):
                longest = word

    return len(longest)


def initGrid():
    gridLength = getGridDimensions()
    return [[0]*gridLength]*gridLength
