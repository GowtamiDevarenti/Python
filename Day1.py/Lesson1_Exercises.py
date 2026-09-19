# Lab 1: Python Foundation Exercises
# File: lesson1_exercises.py
# ==========================================
# Part A – Warm-up: Python Basics
# ==========================================
# 1. Create a new file called lesson1_exercises.py. Print your name, the course name and today's study goal on separate lines.
print("Name: Gowtami Devarenti")
print("Course: Python Programming")
print("Today's study goal: Learn basic Python syntax and data types")
# 2. Create variables for a person's name, age, height in meters and whether they are currently a student. Print both the values and their types.
name = "Gowtami Devarenti"
age = 33
height = 1.65
is_student = True
print("Name:", name)
print("Type of name:", type(name))
print("Age:", age)
print("Type of age:", type(age))
print("Height:", height)
print("Type of height:", type(height))
print("Is student:", is_student)
print("Type of is_student:", type(is_student))
# 3. Change the value stored in one variable to a different data type. Print its type before and after the change. Explain in a comment what this demonstrates about Python.
test_var = 10
print("Before change:", test_var)
print("Type before:", type(test_var))
# Change to string
test_var = "ten"
print("After change:", test_var)
print("Type after:", type(test_var))
# This demonstrates that Python is dynamically typed.
# A variable does not have a fixed type; Python updates its type
# automatically based on the value assigned to it.
# 4. Create two numeric variables and calculate: Addition, Subtraction, Multiplication, Normal division, Floor division, Remainder, Exponentiation.

num1 = 20
num2 = 5

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Normal division:", num1 / num2)
print("Floor division:", num1 // num2)
print("Remainder:", num1 % num2)
print("Exponentiation:", num1 ** num2)
