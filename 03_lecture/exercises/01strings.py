"""
Write a program which asks the user for a string and an amount.
The program then prints out the string as many times as specified by the amount.
The printout should all be on one line, with no extra spaces or symbols added.

Example:
    Please type in a string: >> hey
    Please type in an amount: >> 4
    heyheyheyhey
"""
# Write your solution here
#enter = input("Please type in a string: ")
#n = int(input("Please type in an amount: "))
#print(enter * n)


""""

Write a program which asks the user for two strings and then prints out whichever is the longer of the two - 
that is, whichever has the more characters. If the strings are of equal length, the program 
should print out "The strings are equally long".

Examples:

    Please type in string 1: >> hello
    Please type in string 2: >> world
    The strings are equally long
    
    Please type in string 1: >> hey
    Please type in string 2: >> world
    world is longer
"""

# Write your solution here
#string_1 = input("Enter one string: ")
#string_2 = input("Enter another string: ")
#if len(string_1) < len(string_2):
#    print(f"{string_2} has more characters than {string_1}.")
#elif len(string_1) > len(string_2):
#    print(f"{string_1} has more characters than {string_2}.")
#else:
#    print("Both strings are equally long.")

"""
Write a program which asks the user for a string. The program then prints out the input string in reversed order, 
from end to beginning. Each character should be on a separate line.
Try to solve this example in 2 ways:
    * once using positive indeces
    * once using negative indeces
"""
str = input("String here: ")
for i in range(-1, -len(str) - 1, -1):
    print(str[i])

for i in range(len(str) - 1, -1, -1):
    print(str[i])

# Write your solution here

# def reverse_string_negative_index(string):
#     reversed_string = string[::-1]
#     for i in range(-1, -len(reversed_string) - 1, -1):
#         print(reversed_string[i])

# user_input = input("Enter a string: ")
# reverse_string_negative_index(user_input)

# input_string = input("Please type in a string: ")
# index = -1
# while abs(index) <= len(input_string):
#     print(input_string[index])
#     index -= 1

"""
Write a program which asks the user for a string. 
The program then prints out a message based on whether the second character and the second to last character 
are the same or not. See the examples below.

Examples:
    Please type in a string: >> python
    The second and the second to last characters are different
    
    Please type in a string: >> pascal
    The second and the second to last characters are a
"""
# Write your solution here

#input_string = input("Please type in a string: ")
#if input_string[1] == input_string[-2]:
#    print(f"The second and the second last characters are {input_string[1]}")
#    print(input_string)
#else:
#    print("The second and the second to last characters are different.")


"""
Write a program which prints out a line of hash characters, the width of which is chosen by the user.

Examples:
    Width: >> 8
    ########
    
    Width: >> 2
    ##
"""
# Write your solution here
#symbol = "#"
#width = int(input("Enter a width: "))
#print(symbol * width)



"""
Modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.

Example:
    Width: >> 10
    Height: >> 3
    ##########
    ##########
    ##########
"""
# Write your solution here
#symbol = "#"
#height = int(input("Enter a height: "))
#width = int(input("Enter a width: "))
#i = 0
#while i < height:
#    print(symbol * width)
#    i += 1


"""
Write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed. 
If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.

You may assume the input string is at most 20 characters long.

Examples:
    Please type in a string:hello
    ***************hello
    
    Please type in a string:helloworld
    **********helloworld 
"""
# Write your solution here

# string = input("Input a string: ")
# star = 20 - len(string)
# if len(string) == 20:
#     print(string)
# elif len(string) > 20:
#     print("The string is too long.")
# else:
#     print("*" * int(star) + string)

"""
Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. 
The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.

Examples:
    Word: >> testing
    
    ******************************
    *          testing           *
    ******************************

    Word: >> python
    
    ******************************
    *           python           *
    ******************************
"""
# Write your solution here

# stars = 30 * "*"
# string = input("Please input a string: ")
# spaces = (28 - len(string)) // 2
# print(stars)
# if len(string) % 2 == 0:
#     print("*" + spaces * " " + string + spaces * " " + "*")
# elif len(string) % 2 == 1:
#     print("*" + (spaces + 1) * " " + string + spaces * " " + "*")
# print(stars)

"""
Write a program which asks the user to type in a string. 
The program then prints out all the substrings which begin with the first character, 
from the shortest to the longest. Have a look at the example below.

Example:
    Please type in a string: >> test
    t
    te
    tes
    test
"""
# Write your solution here

#string = input("Please type in a string: ")
#index = 0
#i = 0
#all_strings = ""
#while i < len(string):
#    print(all_strings + string[index])
#    all_strings += string[index]
#    index += 1
#    i += 1


"""
Write a program which asks the user to type in a string. 
The program then prints out all the substrings which end with the last character, from the shortest to the longest. 
Have a look at the example below.

Example:
    Please type in a string: >> test
    t
    st
    est
    test
"""
# Write your solution here

string = input("Please type in a string: ")
index = -1
i = 0
all_strings = ""
while i < len(string):
    print(all_strings + string[index])
    all_strings += string[index]
    index -= 1
    i += 1

"""
Write a program which asks the user to input a string. The program then prints out different messages if the string 
contains any of the vowels a, e or o.

You may assume the input will be in lowercase entirely. Have a look at the examples below.

    Please type in a string: >> hello there
    a not found
    e found
    o found
    
    Please type in a string: >> hiya
    a found
    e not found
    o not found
"""
# Write your solution here



"""
Write a program which asks the user to type in a string and a single character. The program then 
prints the first three character slice which begins with the character specified by the user. 
You may assume the input string is at least three characters long. The program must print out three characters, 
or else nothing.

Pay special attention to when there are less than two characters left in the string after the first occurrence of 
the character looked for. In that case nothing should be printed out, and there should not be any indexing errors 
when executing the program.

Examples:

    Please type in a word: >> mammoth
    Please type in a character: >> m
    mam
    
    Please type in a word: >> banana
    Please type in a character: >> n
    nan
    
    Please type in a word: >> python
    Please type in a character: >> n
"""
# Write your solution here

"""
Write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, 
the program should print out a message accordingly.

In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the 
substring aa is at index 2.

Examples:

    Please type in a string: >> abcabc
    Please type in a substring: >> ab
    The second occurrence of the substring is at index 3.
    
    Please type in a string: >> methodology
    Please type in a substring: >> o
    The second occurrence of the substring is at index 6.
    
    Please type in a string: >> aybabtu
    Please type in a substring: >> ba
    The substring does not occur twice in the string.
"""
# Write your solution here