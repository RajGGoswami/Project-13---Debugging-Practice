# Day 13 – Debugging Practice
# Part of my 100 Days of Code journey
#
# Learning goals for this project:
# - Understanding common programming bugs
# - Practicing systematic debugging techniques
# - Learning how to reason about code before running it
# - Using print statements, logic checks, and error handling
#
# This file contains multiple small debugging exercises
# focused on identifying, reproducing, and fixing bugs.


import random
import math


# --------------------------------------------------
# 1. DESCRIBE THE PROBLEM
# --------------------------------------------------
# Bug: The loop never reaches 20 because range(1, 20)
# stops at 19. Therefore the condition i == 20 is never true.

# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it!")
#
# my_function()

# Fix: Extend the range to include 20

# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it!")
#
# my_function()


# --------------------------------------------------
# 2. REPRODUCE THE BUG
# --------------------------------------------------
# Bug: randint was used without importing it from random

# dice_list = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(0, 5)
# print(dice_list[dice_num])

# Fix: Use random.randint or import randint explicitly


# --------------------------------------------------
# 3. PLAY COMPUTER (LOGIC ERROR)
# --------------------------------------------------
# Bug: Edge cases were not fully handled

# year = int(input("What's your year of birth? "))
#
# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year >= 1994:
#     print("You are Gen Z.")


# --------------------------------------------------
# 4. FIX ERRORS (EXCEPTION HANDLING)
# --------------------------------------------------
# Bug: Program crashes if non-numeric input is entered

# try:
#     age = int(input("How old are you? "))
# except ValueError:
#     print("You have typed in an invalid number. Please try again.")
#     age = int(input("How old are you? "))
#
# if age > 18:
#     print(f"You can drive at age {age}")


# --------------------------------------------------
# 5. PRINT IS YOUR FRIEND
# --------------------------------------------------
# Bug: Incorrect or missing variable assignment

# pages = int(input("Number of pages: "))
# words_per_page = int(input("Number of words per page: "))
# total_words = pages * words_per_page
# print(total_words)


# --------------------------------------------------
# 6. USE A DEBUGGER (COMPLEX LOGIC)
# --------------------------------------------------
# Practicing step-by-step inspection of variable changes

# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1, 3)
#         new_item += item
#         b_list.append(new_item)
#     print(b_list)
#
# mutate([1, 2, 3, 5, 8, 13])


# --------------------------------------------------
# FINAL DEBUGGING PRINCIPLES
# --------------------------------------------------
# 7. Take a Break
# 8. Ask a Friend
# 9. Run the Code Often
# 10. Ask StackOverflow


# --------------------------------------------------
# DEBUGGING PRACTICE – SOLVED EXAMPLES
# --------------------------------------------------

# 1. Odd or Even

# def odd_or_even(number):
#     if number % 2 == 0:
#         return "This is an even number."
#     else:
#         return "This is an odd number."


# 2. Leap Year Checker

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False


# 3. FizzBuzz

# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         if number % 3 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#         elif number % 3 == 0:
#             print("Fizz")
#         elif number % 5 == 0:
#             print("Buzz")
#         else:
#             print(number)
