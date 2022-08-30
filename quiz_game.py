print("Welcome to my physics quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes": # If the user types in "yes" or "Yes" the game will continue, but if they type anything else, the code will stop. The "lower" part, converts everything that is beeing written by the user to lower case, while ".upper" converts it all to upper case.
    quit()

print("Great! Let's play :)")
score = 0

answer = input("Who is the first person to design models of flying machines? ").lower()
if answer == "leonardo da vinci":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("How long did it take Henry Ford to assemble a Model Tear after establishing the conveyer belt? ").lower()
if answer == "93 minutes":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")


answer = input("What is the unit of frequency? ").lower()
if answer == "hertz":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("Which sound is produced by the Galton whistle? ").lower()
if answer == "ultrasonic":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + " % correct!") # The number 4 is there because there are 4 questions. (score / amount of questions) * 100 = how big of a % you have guessed correctly.
