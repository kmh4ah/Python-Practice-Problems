
#Print out a message to the user to tell them the year that they will turn 100 years old
print("***This program can tell in which year you will turn 100 years old***")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
present_year = int(input("Enter current year: "))
predict_year = str((present_year - age) + 100)
print(name + " will turn 100 years old in " + predict_year)
