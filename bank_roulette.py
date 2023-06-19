#You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
#Important: You are not allowed to use the choice() function.

import random 

# Split string method
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")

print(names)

list_size = len(names)

choosen = random.randint(0, list_size - 1)

print(choosen)

print (f"{names[choosen]} is going to buy the meal today!")