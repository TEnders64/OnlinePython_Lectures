print "Scores and Grades"
for i in range(0,10):
    user_input = raw_input("Enter A Score: ")
    if user_input < 60:
        print "Score: ",user_input,"; Your grade is an F"
    elif user_input <= 69:
        print "Score: ",user_input,"; Your Grade is a D"
    elif user_input <= 79:
        print "Score: ",user_input,"; Your grade is a C"
    elif user_input <= 89:
        print "Score: ",user_input,"; Your grade is a B"
    else:
        print "Score: ",user_input,"; Your grade is an A"
print "End of the program, Bye!"
