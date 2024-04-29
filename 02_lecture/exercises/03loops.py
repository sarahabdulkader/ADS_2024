"""
Write a program that prints out the message "hello world!" and then asks "shall we continue?"
until the user inputs "no". Then the program should print out "okay then" and finish.

Example:
    hello world!
    shall we continue? >> yes
    hello world!
    shall we continue? >> oui
    hello world!
    shall we continue? >> jawohl
    hello world!
    shall we continue? >> no
    okay then
"""
# Write your solution here
# print("Hello world!")
# while True:
#  code = input("Shall we continue? ")
#  if code != "no":
#    continue
#  else:
#   break
# print("Okay then.")


"""
Write a program which asks the user for integer numbers.

- If the number is below zero, the program should print out the message "invalid number".
- If the number is above zero, the program should print out the square root of the number using the Python sqrt function
- In either case, the program should then ask for another number.
- If the user inputs the number zero, the program should stop asking for numbers and exit the loop.

To use the `sqrt` function in python add the following to the top of your file: 
    from math import sqrt
Then use it like:
    print(sqrt(9))
    
Example:
    Please type in a number: >> 16
    4.0
    Please type in a number: >> 4
    2.0
    Please type in a number: >> -3
    invalid number
    Please type in a number: >> 1
    1.0
    Please type in a number: >> 0
    Exiting...
"""
# Write your solution here
# from math import sqrt

# while True:
#  number = int(input("Please type in a number: "))
#  if number == 0:
#    break
#  elif number < 0:
#    print("Invalid number.")
#    continue
#  elif number > 0:
#    print(sqrt(number))
#    continue
#  else:
#    continue



"""
This program should print out a countdown. However, the program doesn't quite work. Please fix it.
Hint: you can use the debugger of PyCharm to see how the program is executing.
"""
# Fix the code
# print("Countdown!")
# number = 5
# while True:
#  print(number)
#  number = number - 1
#  if number == 0:
#    break
# print("Now!")

"""
Write a program which asks the user for a year, and prints out the next leap year.
If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year.

Examples:
    Year: >> 2023
    The next leap year after 2023 is 2024
    
    Year: >> 2024
    The next leap year after 2024 is 2028
"""
# Write your solution here

# year = int(input("Year: "))
# while True:
#  if year % 4 == 0:
#    print(f"The next leap year after {year} is {year + 4}")
#    break
#  elif year % 4 == 1:
#    print(f"The next leap year after {year} is {year + 3}")
#    break
#  elif year % 4 == 2:
#    print(f"The next leap year after {year} is {year + 2}")
#    break
#  elif year % 4 == 3:
#    print(f"The next leap year after {year} is {year + 1}")
#    break




"""
Please write a program which keeps asking the user for words. 
If the user types in end, the program should print out the story the words formed, and finish.

Example:
  Please type in a word: >> Once
  Please type in a word: >> upon
  Please type in a word: >> a
  Please type in a word: >> time
  Please type in a word: >> there
  Please type in a word: >> was
  Please type in a word: >> a
  Please type in a word: >> girl
  Please type in a word: >> end
  Once upon a time there was a girl
"""

# all_strings = ""
# while True:
#  story = input("Enter a word: ('end' to finish):")
#  if story.lower() == "end":
#    print(all_strings)
#    break
#  else:
#    all_strings += story + " "

"""
Change the program above so that the loop ends also if the user types in the same word twice in a row.
"""
# Write your solution here

# prev_string = None
# all_strings = ""
# while True:
#  story = input("Enter a word: ")
#  story = prev_string
#  if story == prev_string:
#    print(all_strings)
#    break
#  elif story.lower() == "end":
#    print(all_strings)
#    break
#  else:
#    all_strings += story + " "

"""
Please write a program which asks the user for integer numbers. 
The program should keep asking for numbers until the user types in 0.

After reading the numbers the program should 
  - print out how many numbers were typed in
  - the sum of numbers entered
  - the mean of numbers entered
  - the number of positive and negative numbers entered
  
Example output
  Numbers typed in 4
  The sum of the numbers is 34
  The mean of the numbers is 8.5
  Positive numbers 3
  Negative numbers 1
"""
# Write your solution here


#positive_number = int(0)
#negative_number = int(0)
#typed_in = -1
#all_numbers = int(0)
#sum = 0
#while True:
#    number = int(input("Please type in a number: "))
#    typed_in += 1
#    sum += number
#    if number == 0:
#      print(f"Numbers typed in: {typed_in}.")
#      print(f"The sum of the numbers is {sum}.")
#      if typed_in != 0:
#         mean = sum / typed_in
#      else:
#         mean = 0
#      print(f"The mean of the numbers is {mean}")
#      print(f"Positive numbers {positive_number}")
#      print(f"Negative numbers {negative_number}")
#      break
#    elif number > 0:
#        positive_number += 1
#    elif number < 0:
#        negative_number += 1


"""
Largest Number

Write a program in Python 3 which asks the user for float numbers.
The program should keep asking for numbers until the user types in 0 or a negative number.
The program should then print the largest number.
If the first number entered is less than or equals to 0, the program should quit and print "no number entered".

DO NOT USE LISTS TO SOLVE THIS EXERCISE!

Examples:
  Number 1: >> 3
  Number 2: >> 4.67
  Number 3: >> 120.5
  Number 4: >> 70
  Number 5: >> 0
  The largest number is 120.5
  
  Number 1: >> -1.11
  No number entered.
"""
# Write your solution here

# all_strings = ""
# while True:
#  story = input("Enter a word: ('end' to finish):")
#  if story.lower() == "end":
#    print(all_strings)
#    break
#  else:
#    all_strings += story + " "


# largest_num = None
# all_numbers = ""

# first_num = float(input("Enter a first number: "))
# if first_num <= 0:
#    print("No number entered.")
# else:
#     largest_num = first_num
#     all_numbers += str(first_num) + " "
#     while True:
#         number = float(input("Enter another number: "))
#         if number <= 0:
#             break
#         all_numbers += str(number) + " "
#         if number > largest_num:
#             largest_num = number
# if largest_num is not None:
#     print(f"All numbers entered:\n{all_numbers}\n")
#     print(f"The largest number is {largest_num}.")






"""
Write a program that reads in an integer number (number of lines) and generates the subsequent output using 
two loops on the console (see below). 
If the input of numbers is smaller or equal to 0 an error message should be printed.

Examples:
  n: >> 4
  1
  2 3
  4 5 6
  7 8 9 10
  
  n: >> -1
  Invalid number!
"""
# Write your solution here
#while True:
#    n = int(input("Enter a number of rows: "))
#    if n <= 0:
#        print("Invalid number of rows!")
#        break
#    else:
#        count = 1
#        i = 1
#        while i <= n:
#            print(count, end=" ")
#            count += 1
#            i += 1

while True:
    n = int(input("Enter the number of lines: "))

    if n <= 0:
        print("Invalid number!")
    else:
        break

count = 1
for i in range(1, n + 1):
    for j in range(i):
        print(count, end=" ")
        count += 1
    print()

#i = 1
#while i <= rows:
#    j = 1
#    while j <= i:
#        print("*", end=" ")
#        j += 1
#    print()
#    i += 1

"""
Write a program that uses loops to create a pyramid of stars '*' on the console. 
The pyramid should have exactly 6 rows.
Example:
       *
      ***
     *****
    *******
   *********
  ***********
"""
# Write your solution here
""""
rows = 6
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end=" ")
        for j in range(2*i + 1):
            print("*", end=" ")
        print()
        n = 5

"""
# Pyramide wie oben angegeben

row = "*"

while n > 0:
    print(" " * n + row)
    row += "**"
    n -= 1


# Pyramide links

rows = 6
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

#Pyramide wie oben angegeben

rows = 6
i = 1
while i <= rows:
    print(" " * (rows - i) + "*" * (2 * i - 1))
    i += 1

#upside down pyramid

rows = 6
i = 6
while i >= 1:
    print(" " * (rows - i) + "*" * (2 * i - 1))
    i -= 1

"""
Write a program to calculate the average grade. The console reads in grades between 1 and 5 
until the number 0 is entered. If an invalid grade is entered, an error message is displayed, 
the grade is not counted and the prompt progresses. It is assumed that only integers are entered. 
At the end of the input, the grade average and the number of negatives (grade = 5) are output.

Example:
  Mark 1: >> 5
  Mark 2: >> 3
  Mark 3: >> 10
  Invalid mark!
  Mark 3: >> 1
  Mark 4: >> 5
  Mark 5: >> 0
  Average: 3.50
  Negative marks: 2
"""
# Write your solution here
""""
typed_grade = 0
sum = 0
negative_mark = 0
while True:
    grade = int(input("Type in the grade: "))
    if grade == 0:
        break
    elif grade > 5:
        print("Invalid mark!")
        continue
    elif grade == 5:
        negative_mark += 1
    else:
        typed_grade += 1
        sum += grade
print(f"Average: {sum / typed_grade}")
print(f"Negative marks: {negative_mark}")

"""




