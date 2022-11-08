

# Welcome the people to my quiz
def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {} ".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


statement_generator("Welcome To My Math Quiz!!", "*")


# Player enters their name
name = input("Enter A Name:")
print("Stored Name: {}".format(name))

# introducing them to what timetables they want to be tested on and what they want to go up to
time_table = int(input("What times table do you want to be quizzed on?"))
max_value = int(input("Enter the maximum value for your time table."))
score = 0

# Start of the timetable quiz
print("Here is the {} time table quiz ... Good luck".format(time_table))

# Timetables process
for x in range(1, max_value+1):
    answer = x * time_table
    guess = int(input("What is {} x {} = ".format(x, time_table)))
    if guess == answer:
        print("CORRECT")
        score += 1
    else:
        print("WRONG, {} x {} = {}".format(x, time_table, answer))


# Ask The user to play again
play_again = input("Press <Enter> To play Again.... ")
while play_again == "":
    play_again = "Press <Enter>"

# continues the quiz
else:
    play_again = input("Let's Continue With The Math Quiz. ")

# enter their name
    name = input("Enter A Name:")
print("Stored Name: {}".format(name))

# introducing them to what timetables they want to be tested on and what they want to go up to
time_table = int(input("What times table do you want to be quizzed on?"))
max_value = int(input("Enter the maximum value for your time table."))
score = 0

# Start of the timetable quiz
print("Here is the {} time table quiz ... Good luck".format(time_table))

# Timetables process
for x in range(1, max_value+1):
    answer = x * time_table
    guess = int(input("What is {} x {} = ".format(x, time_table)))
    if guess == answer:
        print("CORRECT")
        score += 1
    else:
        print("WRONG, {} x {} = {}".format(x, time_table, answer))

# player to quit the quizz
play_again = input("Type 'xxx' to quit playing the quiz. ")
while play_again == "":
    play_again = "xxx"


# telling the user thank you for playing and have an awesome day :)
else:
    play_again = input("Thank You For Playing My Quiz, Have An Awesome Day :) .")
