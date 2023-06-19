#You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
import random

randomint = random.randint(1, 2)

if randomint == 1:
    print("Heads")
else:
    print("Tails")