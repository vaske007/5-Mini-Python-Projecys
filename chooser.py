import random


time_to_code = ["30 min", "45 min", "1 hour", "1 hour 15 min", "1 hour 30 min", "1 hour 45 min", "2 hour"]

print("30 min = 0", "45 min = 1", "1 hour = 2", "1 hour 15 min = 3", "1 hour 30 min = 4", "1 hour 45 min = 5", "2 hour = 6")

how_much_time_do_you_have = input("How much time do you have? ")
how_much_time_do_you_have = int(how_much_time_do_you_have)

print(time_to_code[how_much_time_do_you_have])