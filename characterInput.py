#Asks a user their name and age and prints the year the user will turn 100 along with their name.
#Also asks for a random number that determins how many times the previous number is printed.
import datetime
#imports the datetime module to find the current year
username = input("Hello there! Please enter your name. ")
#enter your name
userage = input('Now would please enter your age. ')
#enter your age
printnumber = int(input('And could you please enter a random number. '))
#enter a random number
currentyear = datetime.date.today().year
#extracts the current year from datetime
whenage100 = ((100 - int(userage) + currentyear))
#variable that calculates the year the user will turn 100
print("You will turn 100 in " + str(whenage100) + ", " + username + '.')
#prints a personalized message telling the user what year they will turn 100
while printnumber > 0:
    print("You will turn 100 in " + str(whenage100) + ", " + username + '.')
    printnumber = int(printnumber) - 1
#prints the same message printnumber times