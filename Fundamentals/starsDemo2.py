x = [4, 6, 1, 3, 5, 7, 25]

# for idx in range(0, len(x)):
#     stars = ""
#     for num in range(0, x[idx]):
#         stars += "*"
#     print stars

for idx in range(0, len(x)):
    print x[idx] * "*!"

y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

for idx in range(0, len(y)):
    if isinstance(y[idx], str):
        strLen = len(y[idx])
        print strLen * y[idx][0].lower() 
    else:
        print y[idx] * "*"
