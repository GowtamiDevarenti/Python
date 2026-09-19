# ==========================================
# Part A - Warm-up: Python basics
# ==========================================

# 1. Print personal details and study goal
print("Name: Gowtami Devarenti")
print("Course: Python Programming")
print("Today's study goal: Learn Python basics and data types")

# 2. Variables for person's details and their data types
name = "Gowtami Devarenti"
age = 33
height = 1.65
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)

print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))

# 3. Change variable data type
age = 33
print("Age before:", age)
print("Type before:", type(age))

# changing to string
age = "thirty-three"
print("Age after:", age)
print("Type after:", type(age))

# This shows Python is dynamically typed.
# A variable can change its data type at any time based on the new value.

# 4. Arithmetic calculations
a = 15
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Normal division:", a / b)
print("Floor division:", a // b)
print("Remainder:", a % b)
print("Exponentiation:", a ** b)

# 5. Three examples of explicit type conversion

# string to int
num_str = "25"
num_int = int(num_str)
print("String to int:", num_int + 5)

# int to float
count = 10
count_float = float(count)
print("Int to float:", count_float)

# number to string
score = 95
message = "Your score is " + str(score)
print("Number to string:", message)


# ==========================================
# Part B - User input and calculations
# ==========================================

# 1. Profile program: calculate approximate age
name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))

current_year = 2026
age = current_year - birth_year
print(f"Hello {name}, you are approximately {age} years old.")

# 2. Price and discount calculation
price = float(input("Enter the price: "))
discount_percent = float(input("Enter discount percentage: "))

discount = price * (discount_percent / 100)
final_price = price - discount
print(f"Final price: ${final_price:.2f}")

# 3. Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit:.2f} degrees F")

# 4. Room area and perimeter
length = float(input("Enter room length: "))
width = float(input("Enter room width: "))

area = length * width
perimeter = 2 * (length + width)

print(f"Room area: {area:.2f}")
print(f"Room perimeter: {perimeter:.2f}")

# 5. What happens if the user enters 'hello'?
# If the user enters 'hello' when a number is expected, Python gives a ValueError:
# ValueError: invalid literal for int() with base 10: 'hello'
# This happens because int() and float() only work with numbers, not words.
# The program crashes immediately at that line.


# ==========================================
# Part C - Strings
# ==========================================

# 1. Sentence length, upper, lower, and stripped
sentence = "   Python is powerful and versatile.   "

print("Length:", len(sentence))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Stripped:", sentence.strip())

# 2. Full name with f-string
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

full_name = f"{first_name} {last_name}"
print("Full name:", full_name)

# 3. Slicing 'python programming'
text = "python programming"

print("First character:", text[0])
print("Last character:", text[-1])
print("First six characters:", text[:6])
print("Last eleven characters:", text[-11:])
print("Reversed string:", text[::-1])

# 4. Username generator
first = input("Enter first name: ").strip().lower()
last = input("Enter last name: ").strip().lower()

username = first[:3] + last[:5]
print("Generated username:", username)

# 5. Email split
email = input("Enter email: ")
parts = email.split("@")

local_part = parts[0]
domain = parts[1]

print("Local part:", local_part)
print("Domain:", domain)

# 6. Replace Java with Python
sentence = "I like to code in Java."
new_sentence = sentence.replace("Java", "Python")

print("Original sentence:", sentence)
print("Changed sentence:", new_sentence)


# ==========================================
# Part E - Applied Challenge: Registration Summary
# ==========================================

# 1 & 2. Collect and normalize inputs
first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
city = input("Enter city: ").strip()
birth_year = int(input("Enter year of birth: ").strip())
fav_language = input("Enter favourite language: ").strip()

# 3. Create user ID: first 3 of last name + first of first name + last 2 of year
user_id = (last_name[:3] + first_name[:1] + str(birth_year)[-2:]).lower()

# 4. Multi-line summary using f-strings
print("\n--- Registration Summary ---")
print(f"Name               : {first_name.title()} {last_name.title()}")
print(f"User ID            : {user_id}")
print(f"City               : {city.title()}")
print(f"Year of Birth      : {birth_year}")
print(f"Favourite Language : {fav_language.capitalize()}")

# 5. Initials, name length (no spaces), reversed language
initials = f"{first_name[0].upper()}.{last_name[0].upper()}."
name_length = len(first_name) + len(last_name)
reversed_language = fav_language[::-1]

print(f"Initials           : {initials}")
print(f"Name Length        : {name_length} characters")
print(f"Reversed Language  : {reversed_language}")

# 6. Three extra pieces of derived info
age = 2026 - birth_year
student_email = f"{first_name.lower()}.{last_name.lower()}@techacademy.edu"
city_code = city[:3].upper()

print(f"Approximate Age    : {age} years old")
print(f"Student Email      : {student_email}")
print(f"City Code          : {city_code}")


# ==========================================
# Part F - Stretch Challenges: Python Foundation
# ==========================================

# 1. Seconds converter using // and %
total_seconds = int(input("\nEnter total seconds: "))

hours = total_seconds // 3600
leftover_seconds = total_seconds % 3600

minutes = leftover_seconds // 60
seconds = leftover_seconds % 60

print(f"{total_seconds} seconds = {hours} hour(s), {minutes} minute(s), and {seconds} second(s)")

# 2. Extract digits of 4-digit number without string conversion
num = int(input("Enter a 4-digit integer: "))

thousands = num // 1000
hundreds = (num // 100) % 10
tens = (num // 10) % 10
units = num % 10

print("Thousands:", thousands)
print("Hundreds :", hundreds)
print("Tens     :", tens)
print("Units    :", units)

# 3. Text masking: show first 2 and last 2 letters, middle with *
word = input("Enter a word: ").strip()

if len(word) <= 4:
    masked = word
else:
    middle = "*" * (len(word) - 4)
    masked = word[:2] + middle + word[-2:]

print("Masked word:", masked)

# 4. Five 'predict before running' examples

# Example 1: string concatenation + int conversion
val = "12"
print("Example 1:", int(val) + int(val + "3"))
# Prediction: 135
# Why: val + "3" gives "123". Then 12 + 123 = 135.

# Example 2: slicing with step
letters = "abcdefghijkl"
print("Example 2:", letters[1:9:3])
# Prediction: 'beh'
# Why: starts at index 1 ('b'), stops before 9 ('j'), takes every 3rd letter.

# Example 3: negative slice
text = "Developer"
print("Example 3:", text[-3::-2])
# Prediction: 'pedv'
# Why: starts at 'p' (index -3), steps backward by 2.

# Example 4: operator precedence
print("Example 4:", 17 // 3 + 17 % 3 * 5)
# Prediction: 15
# Why: 17 // 3 = 5, 17 % 3 = 2. Multiplication is first: 2 * 5 = 10. Then 5 + 10 = 15.

# Example 5: slice and int conversion
code = "987654"
print("Example 5:", int(code[:3]) - int(code[-2:]))
# Prediction: 933
# Why: code[:3] is "987" and code[-2:] is "54". 987 - 54 = 933.
