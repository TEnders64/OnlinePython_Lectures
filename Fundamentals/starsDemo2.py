x = [4, 6, 1, 3, 5, 7, 25]


# for idx in range(0, len(x)):
#     stars = ""
#     for num in range(0, x[idx]):
#         stars += "*"
#     print stars
#
# for idx in range(0, len(x)):
#     print x[idx] * "*"

y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
#
# for idx in range(0, len(y)):
#     if isinstance(y[idx], str):
#         strLen = len(y[idx])
#         print strLen * y[idx][0].lower()
#     else:
#         print y[idx] * "*"

# def drawStarsAndChars(someList):
#     for idx in range(0, len(someList)):
#         if isinstance(someList[idx], str):
#             char = someList[idx][0].lower()
#             charStr = ""
#             for charIdx in range(0, len(someList[idx])):
#                 charStr += char
#             print charStr
#         else:
#             starStr = ""
#             for starIdx in range(0, someList[idx]):
#                 starStr += "*"
#             print starStr
# 
# drawStarsAndChars(y)















class Queens:
    def __init__(self, n):
        self.n = n
        rangen = range(n)

        # Assign a unique int to each column and diagonal.
        # columns:  n of those, range(n).
        # NW-SE diagonals: 2n-1 of these, i-j unique and invariant along
        # each, smallest i-j is 0-(n-1) = 1-n, so add n-1 to shift to 0-
        # based.
        # NE-SW diagonals: 2n-1 of these, i+j unique and invariant along
        # each, smallest i+j is 0, largest is 2n-2.

        # For each square, compute a bit vector of the columns and
        # diagonals it covers, and for each row compute a function that
        # generates the possiblities for the columns in that row.
        self.rowgenerators = []
        for i in rangen:
            rowuses = [(1L << j) |                  # column ordinal
                       (1L << (n + i-j + n-1)) |    # NW-SE ordinal
                       (1L << (n + 2*n-1 + i+j))    # NE-SW ordinal
                            for j in rangen]

            def rowgen(rowuses=rowuses):
                for j in rangen:
                    uses = rowuses[j]
                    if uses & self.used == 0:
                        self.used |= uses
                        yield j
                        self.used &= ~uses

            self.rowgenerators.append(rowgen)

    # Generate solutions.
    def solve(self):
        self.used = 0
        for row2col in conjoin(self.rowgenerators):
            yield row2col

    def printsolution(self, row2col):
        n = self.n
        assert n == len(row2col)
        sep = "+" + "-+" * n
        print sep
        for i in range(n):
            squares = [" " for j in range(n)]
            squares[row2col[i]] = "Q"
            print "|" + "|".join(squares) + "|"
            print sep
