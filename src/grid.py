from functools import lru_cache


@lru_cache
def getGridDimensions():
    longest = ""

    with open("dictionary.txt", "r") as words:
        for word in words:
            if len(word) > len(longest):
                longest = word

    return len(longest)


class Grid:
    def __init__(self):
        length = getGridDimensions()

        self.grid = [["" for i in range(length)] for n in range(length)]
        self.words = []

    def getCopy(self):
        copy = Grid()

        copy.grid = self.grid
        copy.words = self.words

        return copy

    def insertWord(self, word, x, y, horizontal):
        self.words.append([word, x, y, horizontal])

        for i in range(len(word)):
            if horizontal:
                self.grid[y][x + i] = word[i]
            else:
                self.grid[y + i][x] = word[i]

    def removeWord(self, word, x, y, horizontal):
        self.words.remove([word, x, y, horizontal])
        newGrid = Grid()

        for word in self.words:
            newGrid.insertWord(word[0], word[1], word[2], word[3])

        self.grid = newGrid.grid
