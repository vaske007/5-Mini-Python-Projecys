# randint does the same thing as randrange, execpt that it does include the last number you want in range
import random

top_of_range = input("Type a number: ") # Whatever the user types in, will be returned to us as a string(" "), which in python is not considered a number, integer... it's considered a string.

if top_of_range.isdigit(): # .isdigit checks wheter or not the string that the user types in is a number, digit, and if so it will activate the if function.
    top_of_range = int(top_of_range) # Here we are converting the string that we get from the user to a number. If the user types in "25", the int function will turn it into 25. int("25). But if the user types in text like "hello", the int will return error.

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range) 
guesses = 0

while True: # This loop will run while the code indented into it is True. You do not have to use True or False as the condition for the while loop
    guesses += 1
    user_guess = input("Make a guess: ") 
    if user_guess.isdigit(): # .isdigit checks wheter or not the string that the user types in is a number, digit, and if so it will activate the if function.
        user_guess = int(user_guess) # Here we are converting the string that we get from the user to a number. If the user types in "25", the int function will turn it into 25. int("25). But if the user types in text like "hello", the int will return error.
    else:
        print("Please type a number next time.")
        continue # Continue sends you back to the top of the loop

    # If the user guesses correct the loop will break, else it will contiune running till the user gets it correct.
    if user_guess == random_number:
        print("You got it!")
        break # Will stop the loop once the line has been run   
    elif user_guess > random_number: # If the number that the user types in is not equal to the random number, the code will check if the number that the user types in is greater than the random number, they will be told so. And if the number that the user types in is below the random number, they will be told so.
        print ("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses.")
    
    
    
    
    
    
    
