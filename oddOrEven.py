#determines if an input is odd, even, or divisible by 4 and prints a message depeding on the result
#also asks for two inputs and decides if one input divides evenly into the other input
try:
    oddoreven = int(input("What number are you thinking of right now ? "))
    #asks for a number
    num = int(input("Any other number on your mind? " ))
    #asks for a number
    check = int(input("Give me on more number, I know you've got it in you. " ))
    #ask for a number
    if oddoreven % 2 == 0 and oddoreven % 4 != 0:
        print("Your first number, " + str(oddoreven) + ", is even stevens. ")
    #prints a message if the number given was even
    elif oddoreven % 4 == 0:
        print("Your first number, " + str(oddoreven) + ", is dvisible by four, so ..... open your door !")
    #prints a message if the number given was divisible by 4
    else:
        print("Your first number, " + str(oddoreven) + ", is odd as a dog. ")
    #prints a message in all other cases
    if num % check == 0:
        print("Those are some smooth numbers. " + "Your second number, " + str(num) + ", divides evenly into your third number, " + str(check) + " !")
    #prints a message if the second input divides evenly into the third input
    else:
        print("Your second number, " + str(num) + ", does not divide evenly into your third number, " +str(check) + ". ")    
    #prints a message  in all other cases
except ValueError:
    print("Enter a number please !")
#tells user to print a number