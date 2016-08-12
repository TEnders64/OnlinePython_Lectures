print "Scores and Grades"
for num in range(0,2):
    score = input("Enter a score: ")
    if score <= 69:
        grade = "D"
    elif score <= 79:
        grade = "C"
    elif score <= 89:
        grade = "B"
    else:
        grade = "A"
    # print "Score: {}; Your grade is {}".format(score, grade)
    print "Score: "+str(score)+"; Your grade is "+grade
print "Goodbye"
