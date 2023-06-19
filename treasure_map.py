#You are going to write a program that will mark a spot with an X.
#In the starting code, you will find a variable called map.
#This map contains a nested list. 
#Your job is to write a program that allows you to mark a square on the map using a two-digit system. 
#The first digit in the input will specify the column (the position on the horizontal axis).
#The second digit in the input will specify the row number (the position on the vertical axis). 

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\n")

position_split = list(position)
line = position_split[0][0]
column = position_split[1][0]

int_line = int(line)

if column == '1':
    row1 [int_line - 1] = 'X'
elif column == '2':
    row2 [int_line - 1] = 'X'
elif column == '3':
    row3 [int_line - 1] = 'X'
else:
    print("something went wrong")

print(f"{row1}\n{row2}\n{row3}")

