#Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. 

year = int(input("Which year do you want to check? "))

#This is how you work out whether if a particular year is a leap year.
if year % 4 == 0:
#on every year that is evenly divisible by 4 
    if year % 100 == 0:
    #except every year that is evenly divisible by 100 
        if year % 400 == 0:
        #unless the year is also evenly divisible by 400
            print ("Leap year.")
        else:
            print ("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

