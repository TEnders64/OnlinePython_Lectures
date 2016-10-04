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
