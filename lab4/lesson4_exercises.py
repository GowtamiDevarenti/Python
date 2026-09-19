# Lab 4 - Functions in Python
# Name: Gowtami Devarenti
# Course: Python Fundamentals


# Part A - Function fundamentals


# 1. Write functions greet(), show_course_name() and print_separator(). Call each more than once.

def greet():
    print("Hello! Welcome to Python functions.")

def show_course_name():
    print("Course: Python Programming Fundamentals")

def print_separator():
    print("-" * 40)


# 2. Write greet_person(name) and introduce(name, city).

def greet_person(name):
    print(f"Hello, {name}!")

def introduce(name, city):
    print(f"My name is {name} and I live in {city}.")


# 3. Write add(a, b), subtract(a, b), multiply(a, b) and divide(a, b). Each must return a value.

def add(a: int, b: int) -> int:
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Check if b is 0 so the program doesn't crash with ZeroDivisionError
    if b == 0:
        print("Cannot divide by zero!")
        return None
    return a / b


# 4. Demonstrate parameter vs argument in comments using one of your functions.

# Difference between parameter and argument:
# - PARAMETER: The placeholder variables defined in the function header.
#   For example, in `def add(a, b):`, `a` and `b` are parameters.
# - ARGUMENT: The actual values we pass in when we call the function.
#   For example, in `add(10, 5)`, `10` and `5` are arguments.


# 5. Create calculate_area(width, height) and use its returned value in another calculation.

def calculate_area(width, height):
    return width * height



# Part B - Return values
 
 

# 1. Write returning True/False.

def is_even(number: int) -> bool:
    """Checks if a number is even."""
    return number % 2 == 0


# 2. Write get_larger(a, b) returning the larger value without max().

def get_larger(a, b):
    if a > b:
        return a
    else:
        return b


# 3. Write classify_score(score) returning PASS or FAIL.

def classify_score(score):
    if score >= 50:
        return "PASS"
    else:
        return "FAIL"


# 4. Write format_name(first_name, last_name) returning a formatted string.

def format_name(first_name, last_name):
    # strip removes accidental extra spaces, title capitalizes the first letter
    return f"{first_name.strip().title()} {last_name.strip().title()}"


# 5. Write apply_discount(price, percent) returning the discounted price.

def apply_discount(price, percent):
    discount_amount = price * (percent / 100)
    return price - discount_amount


# 6. Show with a small example why print(result) inside a function is not the same as return result.

def add_and_print(a, b):
    result = a + b
    print("Result printed inside function:", result)
    # Since there is no return statement, this function returns None

def add_and_return(a, b):
    result = a + b
    return result

# Explanation:
# print() only displays text on the screen for us to read. It gives nothing back to the code (it evaluates to None).
# return gives the actual value back to where the function was called. This lets us store the answer in a variable
# and use it in further calculations (like multiplying it or adding to it).



# Part C - Defaults and keyword arguments


# 1. Create greet(name, greeting='Hello'). Test positional and keyword arguments.

def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"


# 2. Create calculate_price(price, quantity=1, discount=0). Return the final total.

def calculate_price(price, quantity=1, discount=0):
    total = (price * quantity) - discount
    return total


# 3. Create create_user(name, city='Unknown', active=True) returning a dictionary.

def create_user(name, city="Unknown", active=True):
    return {
        "name": name,
        "city": city,
        "active": active
    }


# 4. Call one function using keyword arguments in a different order from parameter definition.
# Shown in the main section: create_user(active=False, city="Stockholm", name="Gowtami")


# 5. Write one invalid default-parameter ordering as a comment and explain why it is invalid.

# INVALID EXAMPLE:
# def calculate_total(quantity=1, price):
#     return price * quantity
#
# WHY IT IS INVALID:
# In Python, non-default arguments cannot follow default arguments.
# If we called calculate_total(5), Python wouldn't know if 5 is for quantity or for price.
# Mandatory arguments must always come first.


# Part D - Functions and collections



# 1. Write calculate_total(numbers) manually using a loop.

def calculate_total(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# 2. Write count_even(numbers).

def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count


# 3. Write get_long_words(words, minimum_length) returning a new list.

def get_long_words(words, minimum_length):
    long_words = []
    for word in words:
        if len(word) >= minimum_length:
            long_words.append(word)
    return long_words


# 4. Write find_student(students, name) where students is a list of dictionaries. Return the matching dictionary or None.

def find_student(students, name):
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None


# 5. Write average_score(students) for a list of dictionaries containing score values.

def average_score(students):
    if len(students) == 0:
        return 0
    total = 0
    for student in students:
        total += student["score"]
    return total / len(students)


# 6. Write get_active_users(users) returning only dictionaries where active is True.

def get_active_users(users):
    active_users = []
    for user in users:
        if user["active"] is True:
            active_users.append(user)
    return active_users



# Part E - Decomposition


# 1. Build a temperature report using separate functions for Celsius-to-Fahrenheit conversion, classification ('cold/warm/hot') and formatting.

def to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def classify_temp(celsius):
    if celsius < 15:
        return "cold"
    elif celsius <= 25:
        return "warm"
    else:
        return "hot"

def format_temp_report(celsius):
    f = to_fahrenheit(celsius)
    category = classify_temp(celsius)
    return f"{celsius} deg C ({f:.1f} deg F) is {category}."


# 2. Build a small order calculation using separate functions for subtotal, discount and final total.

def get_subtotal(price, quantity):
    return price * quantity

def get_discount(subtotal, discount_percent):
    return subtotal * (discount_percent / 100)

def get_final_total(price, quantity, discount_percent=0):
    subtotal = get_subtotal(price, quantity)
    discount = get_discount(subtotal, discount_percent)
    return subtotal - discount


# 3. Refactor one earlier exercise that contains repeated code into at least three functions.
# Refactored: Student report generator split into 3 small, focused functions

def check_valid_student(student):
    return "name" in student and "score" in student

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"

def generate_student_summary(student):
    if not check_valid_student(student):
        return "Invalid student record"
    grade = get_letter_grade(student["score"])
    status = "Passed" if student["score"] >= 50 else "Failed"
    return f"{student['name'].title()}: Score {student['score']} -> Grade {grade} ({status})"



# Part E.4 - Main-like section calling functions in a clear sequence

def greet_user(name):
    print("Hello,", name)


def calculate_sum(a, b):
    return a + b


def show_result(result):
    print("The result is:", result)


# Main-like section
if __name__ == "__main__":
    greet_user("Alice")

    result = calculate_sum(10, 20)

    show_result(result)




# Part G - Stretch challenges


# 1. Write a function that returns both minimum and maximum from a list without min()/max(). Return two values.

def find_min_max(numbers: list) -> tuple:
    """Finds the minimum and maximum values from a list without using min() or max()."""
    if not numbers:
        return None, None
    smallest = numbers[0]
    largest = numbers[0]
    for num in numbers[1:]:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return smallest, largest


# 2. Write a function that checks whether a word is a palindrome.

def is_palindrome(word: str) -> bool:
    """Checks if a word reads the same forwards and backwards."""
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


# 3. Write a function that counts character frequencies and returns a dictionary.

def count_characters(text: str) -> dict:
    """Counts how many times each character appears in a string."""
    frequencies = {}
    for char in text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies


# 4. Write a function that receives a list of numbers and returns a new dictionary with keys positive, negative and zero containing counts.

def count_numbers_by_sign(numbers: list) -> dict:
    """Counts how many numbers in a list are positive, negative, or zero."""
    counts = {"positive": 0, "negative": 0, "zero": 0}
    for n in numbers:
        if n > 0:
            counts["positive"] += 1
        elif n < 0:
            counts["negative"] += 1
        else:
            counts["zero"] += 1
    return counts


# 5. Add light type hints and a short docstring to at least five functions.

# (Added above to: add, is_even, find_min_max, is_palindrome, count_characters, and count_numbers_by_sign)



