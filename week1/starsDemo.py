def drawStars(numList):
    # [3,1,2]
    # ***
    # *
    # **
    for idx in range(0, len(numList)):
        starStr = ""
        for starIdx in range(0, numList[idx]):
            starStr += "*"
        print starStr

# drawStars([3,1,2])

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def drawStarsAndChars(someList):
    for idx in range(0, len(someList)):
        if isinstance(someList[idx], str):
            char = someList[idx][0].lower()
            charStr = ""
            for charIdx in range(0, len(someList[idx])):
                charStr += char
            print charStr
        else:
            starStr = ""
            for starIdx in range(0, someList[idx]):
                starStr += "*"
            print starStr

drawStarsAndChars(x)
