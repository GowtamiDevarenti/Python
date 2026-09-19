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
num1 = 15
num2 = 4

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Normal division:", num1 / num2)
print("Floor division:", num1 // num2)
print("Remainder:", num1 % num2)
print("Exponentiation:", num1 ** num2)

# 5. Write three examples where explicit type conversion is necessary: String to int, int to float, Number to string.
# String to int
age_text = "25"
age_num = int(age_text)
print("String to int:", age_num + 5)

# int to float
count = 10
count_float = float(count)
print("Int to float:", count_float)

# Number to string
score = 95
score_text = "Your score is " + str(score)
print("Number to string:", score_text)


# ==========================================
# Part B – User Input and Calculations
# ==========================================

# 1. Profile program: asks for name and year of birth, then prints approximate age.
user_name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))
current_year = 2026
age = current_year - birth_year
print(f"Hello {user_name}, you are approximately {age} years old.")

# 2. Price and discount percentage. Round to two decimals.
price = float(input("Enter item price: "))
discount_percentage = float(input("Enter discount percentage: "))
discount_amount = price * (discount_percentage / 100)
final_price = price - discount_amount
print(f"Final price: ${final_price:.2f}")

# 3. Celsius to Fahrenheit conversion using F = C * 9/5 + 32.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"Temperature in Fahrenheit: {fahrenheit:.2f} degrees F")

# 4. Room length and width, calculate area and perimeter.
room_length = float(input("Enter room length: "))
room_width = float(input("Enter room width: "))
room_area = room_length * room_width
room_perimeter = 2 * (room_length + room_width)
print(f"Room area: {room_area:.2f}")
print(f"Room perimeter: {room_perimeter:.2f}")

# 5. Discussion on invalid numeric input in comments:
# What would happen today if the user entered 'hello' when asked for a numeric value?
# When int('hello') or float('hello') runs, Python cannot convert the word 'hello' into numbers.
# Python raises a ValueError: invalid literal for int() with base 10: 'hello'
# The program crashes immediately and stops running at that line.


# ==========================================
# Part C – Strings
# ==========================================

# 1. Sentence methods: length, uppercase, lowercase, stripped.
sentence = "   Python is powerful and versatile.   "
print("Length:", len(sentence))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Stripped:", sentence.strip())

# 2. Full name formatted with f-string.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = f"{first_name} {last_name}"
print("Full name:", full_name)

# 3. Indexing and slicing on 'python programming'.
text = "python programming"
print("First character:", text[0])
print("Last character:", text[-1])
print("First six characters:", text[:6])
print("Last eleven characters:", text[-11:])
print("Reversed string:", text[::-1])

# 4. Username generator.
first = input("Enter first name: ").strip().lower()
last = input("Enter last name: ").strip().lower()
username = first[:3] + last[:5]
print("Generated username:", username)

# 5. Email extraction: local part and domain.
email = input("Enter your email address: ")
local_part, domain = email.split("@")
print("Local part:", local_part)
print("Domain:", domain)

# 6. Replace 'Java' with 'Python'.
original_text = "I like to code in Java."
changed_text = original_text.replace("Java", "Python")
print("Original sentence:", original_text)
print("Changed sentence:", changed_text)


# ==========================================
# Part E – Applied Challenge: Registration Summary
# ==========================================

# 1 & 2. Collect and normalize inputs.
reg_first = input("Enter first name: ").strip()
reg_last = input("Enter last name: ").strip()
city = input("Enter city: ").strip()
reg_year = int(input("Enter year of birth: ").strip())
fav_language = input("Enter favourite programming language: ").strip()

# 3. Generated user ID: first 3 of last name + first of first name + last 2 digits of birth year.
user_id = (reg_last[:3] + reg_first[:1] + str(reg_year)[-2:]).lower()

# 4. Clean multi-line summary using f-strings.
print("\n--- Registration Summary ---")
print(f"Name               : {reg_first.title()} {reg_last.title()}")
print(f"User ID            : {user_id}")
print(f"City               : {city.title()}")
print(f"Year of Birth      : {reg_year}")
print(f"Favourite Language : {fav_language.capitalize()}")

# 5. Initials, name length (no spaces), reversed language.
initials = f"{reg_first[0].upper()}.{reg_last[0].upper()}."
name_length = len(reg_first) + len(reg_last)
reversed_language = fav_language[::-1]

print(f"Initials           : {initials}")
print(f"Name Length        : {name_length} characters")
print(f"Reversed Language  : {reversed_language}")

# 6. Three derived pieces of information.
approx_age = 2026 - reg_year
suggested_email = f"{reg_first.lower()}.{reg_last.lower()}@techacademy.edu"
city_code = city[:3].upper()

print(f"Approximate Age    : {approx_age} years old")
print(f"Suggested Email    : {suggested_email}")
print(f"City Code          : {city_code}")


# ==========================================
# Part F – Stretch Challenges: Python Foundation
# ==========================================

# 1. Simple seconds converter using // and %.
total_seconds = int(input("\nEnter total seconds: "))
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{total_seconds} seconds = {hours} hour(s), {minutes} minute(s), and {seconds} second(s)")

# 2. Extract digits of 4-digit number without converting to string.
number = int(input("Enter a 4-digit integer: "))
thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
units = number % 10

print(f"Thousands : {thousands}")
print(f"Hundreds  : {hundreds}")
print(f"Tens      : {tens}")
print(f"Units     : {units}")

# 3. Text masking program: first 2 and last 2 characters visible, middle with *.
word = input("Enter a word to mask: ").strip()
if len(word) <= 4:
    masked_word = word
else:
    mask = "*" * (len(word) - 4)
    masked_word = word[:2] + mask + word[-2:]

print("Masked word:", masked_word)

# 4. Five 'predict before running' examples.

# Example 1: Type conversion and string concatenation
val = "12"
print("Example 1 result:", int(val) + int(val + "3"))
# Prediction: 135
# Why: val + "3" produces "123". int("12") + int("123") evaluates to 12 + 123 = 135.

# Example 2: String slice with step
alpha = "abcdefghijkl"
print("Example 2 result:", alpha[1:9:3])
# Prediction: 'beh'
# Why: Starts at index 1 ('b'), stops before 9 ('j'), steps by 3 (indices 1, 4, 7).

# Example 3: Negative slice with step
msg = "Developer"
print("Example 3 result:", msg[-3::-2])
# Prediction: 'pedv'
# Why: Starts at index -3 ('p'), steps backward by 2 ('p', 'e', 'd', 'v').

# Example 4: Integer division and modulo precedence
print("Example 4 result:", 17 // 3 + 17 % 3 * 5)
# Prediction: 15
# Why: 17 // 3 = 5; 17 % 3 = 2; 2 * 5 = 10; 5 + 10 = 15.

# Example 5: Slicing and type conversion combined
code = "987654"
print("Example 5 result:", int(code[:3]) - int(code[-2:]))
# Prediction: 933
# Why: code[:3] is "987" (987) and code[-2:] is "54" (54). 987 - 54 = 933.
