# Day 5 I was learnt how to use loops in python
fruits = ["Apple", "Peach", "Pear"]

"""for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)"""

# Write a program that calculates the average student height
"""student_heights = input().split(" ")
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])

sum_height = 0
for height in student_heights:
    sum_height += height
avg_height = round(1.0 * sum_height / len(student_heights), 0)

print(f"Total height = {sum_height}")
print(f"Number of students = {len(student_heights)}")
print(f"Average height = {avg_height}")"""

# Write a program that calculates the highest score from a list of scores
"""student_scores = input().split(" ")
for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in class is: {highest_score}")"""

# Write a program that calculates the sum of all the even numbers from 1 to X.
# If X is 100 then the first even number would be 2 and the last one is 100.
"""target = int(input())
sum_even_number = 0
for num in range(2, target + 1, 2):
    sum_even_number += num
print(sum_even_number)"""

"""You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
    Your program should print each number from 1 to 100 in turn and include number 100.
    When the number is divisible by 3 then instead of printing the number it should print "Fizz".
    When the number is divisible by 5, then instead of printing the number it should print "Buzz
    And if the number is divisible by both 3 and 5 eg. 15 then instead of the number it should print "FizzBuzz" """
"""for num in range(1, 101):
    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    else:
        print(num)"""