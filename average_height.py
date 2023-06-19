# You are going to write a program that calculates the average student height from a List of heights.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

count = 0
for x in student_heights:
    count += 1

total_height = 0
for y in student_heights: 
    total_height = total_height + y

average = total_height / count
round_average = round(average)
print(round_average)



