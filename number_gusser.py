# randint does the same thing as randrange, execpt that it does include the last number you want in range
import random

top_of_range = input("Type a number: ") # Whatever the user types in, will be returned to us as a string(" "), which in python is not considered a number, integer... it's considered a string.

if top_of_range.isdigit(): # .isdigit checks wheter or not the string that the user types in is a number, digit, and if so it will activate the if function.
    top_of_range = int(top_of_range) # Here we are converting the string that we get from the user to a number. If the user types in "25", the int function will turn it into 25. int("25). But if the user types in text like "hello", the int will return error.

    if top_of_range <= 0:
        print("Please type a number larger than  0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range) 

