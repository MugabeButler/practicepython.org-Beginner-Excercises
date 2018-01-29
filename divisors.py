#Asks for a number and prints all divisors of that number
yournumber = int(input("Please enter your number "))

print("Your number is divisible by: ")
for divisor in range(1, yournumber + 1):
#starts loop for a range of numbers starting at 1 and ending at the inputted number + 1
    if yournumber % divisor == 0:
    #if the inputted number divides evenly into the number in the range
        print(divisor)
        #prints the number in the range