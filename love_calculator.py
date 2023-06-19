#You are going to write a program that tests the compatibility between two people.
#To work out the love score between two people:
#Take both people's names and check for the number of times the letters in the word TRUE occurs. 
#Then check for the number of times the letters in the word LOVE occurs. 
#Then combine these numbers to make a 2 digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()

count_t_name1 = lower_name1.count("t")
count_r_name1 = lower_name1.count("r")
count_u_name1 = lower_name1.count("u")
count_e_name1 = lower_name1.count("e")

count_t_name2 = lower_name2.count("t")
count_r_name2 = lower_name2.count("r")
count_u_name2 = lower_name2.count("u")
count_e_name2 = lower_name2.count("e")


count_name1 = count_t_name1 + count_r_name1 + count_u_name1 + count_e_name1 +  count_t_name2 + count_r_name2 + count_u_name2 + count_e_name2

count_l_name1 = lower_name1.count("l")
count_o_name1 = lower_name1.count("o")
count_v_name1 = lower_name1.count("v")
count_e_name1 = lower_name1.count("e")

count_l_name2 = lower_name2.count("l")
count_o_name2 = lower_name2.count("o")
count_v_name2 = lower_name2.count("v")
count_e_name2 = lower_name2.count("e")

count_name2 = count_l_name1 + count_o_name1 + count_v_name1 + count_e_name1 + count_l_name2 + count_o_name2 + count_v_name2 + count_e_name2

str_name1 = str(count_name1)
str_name2 = str(count_name2)
str_final = str_name1 + str_name2

score = int(str_final)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


