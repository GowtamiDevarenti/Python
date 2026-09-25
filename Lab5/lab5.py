
#Part A – Scope
#1.Create a global variable course_name and a function that creates
# a local variable with the same name. 
# Print both and explain the result.

course_name = "Python Programming"   # Global variable


def show_course():
    course_name = "System Developer"          # Local variable
    print("Inside the function:", course_name)


show_course()

print("Outside the function:", course_name)


#2.Create a function with a local counter and show that it does not remain available outside the function.

def count_students():
    counter = 10
    print("Number of students:", counter)


count_students()

# This would give an error because counter only exists inside the function.
#print(counter)

#3.Create a function that attempts to modify a global numeric variable without global. Observe/describe the problem,
# then rewrite the design to return the new value instead.

score = 10


def increase_score(current_score):
    new_score = current_score + 5
    return new_score


score = increase_score(score)

print("New score:", score)

score = 10


def increase_score(current_score):
    new_score = current_score + 5
    return new_score


score = increase_score(score)

print("New score:", score)

#4.Create a nested function and demonstrate a simple enclosing-scope lookup.

def outer_function():
    message = "Hello from the outer function"

    def inner_function():
        print(message)

    inner_function()


outer_function()

#5.Create examples that avoid shadowing built-ins such as list, str, sum and max.

# Good variable names

numbers = [10, 20, 30, 40]

total = sum(numbers)
largest_number = max(numbers)

names = list(("Anna", "John", "Peter"))

text = str(123)

print("Total:", total)
print("Largest:", largest_number)
print("Names:", names)
print("Text:", text)


#Part B – *args

#1.Write add_all(*numbers) returning the sum without sum().

def add_all(*numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


answer = add_all(10, 20, 30, 40)

print("Total:", answer)

#2.Write average(*numbers). Decide what should happen when no numbers are supplied.

def average(*numbers):

    if len(numbers) == 0:
        return None

    total = 0

    for number in numbers:
        total = total + number

    return total / len(numbers)


print("Average:", average(10, 20, 30, 40))

print("Average:", average())


#3.Write longest_word(*words) returning the longest word.

def longest_word(*words):

    if len(words) == 0:
        return None

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


answer = longest_word("cat", "elephant", "dog", "computer")

print("Longest word:", answer)

#4.Write build_sentence(separator, *words) returning one joined string.

def build_sentence(separator, *words):
    sentence = separator.join(words)
    return sentence


result = build_sentence(" ", "Python", "is", "easy", "to", "learn")

print(result)

#5.Write describe_scores(student_name, *scores) returning name, number of scores and average.

def describe_scores(student_name, *scores):

    if len(scores) == 0:
        average = 0
    else:
        total = 0

        for score in scores:
            total = total + score

        average = total / len(scores)

    return student_name, len(scores), average


name, number_of_scores, average_score = describe_scores(
    "Anna", 80, 90, 85, 95
)

print("Student:", name)
print("Number of scores:", number_of_scores)
print("Average:", average_score)


#Part C – Positional Unpacking

#1.Create a list [10, 20, 30] and unpack it into a function expecting three positional parameters.

def show_numbers(first, second, third):
    print("First:", first)
    print("Second:", second)
    print("Third:", third)


numbers = [10, 20, 30]

show_numbers(*numbers)

#2.Create a tuple containing first_name, last_name, city and call a function using *tuple.

def introduce(first_name, last_name, city):
    print(
        f"My name is {first_name} {last_name} "
        f"and I live in {city}."
    )


person = ("Gowtami", "Devarenti", "Gothenburg")

introduce(*person)


#3.Use starred assignment: first, *middle, last = values. Test with several list lengths.

values = [10, 20, 30, 40, 50]

first, *middle, last = values

print("First:", first)
print("Middle:", middle)
print("Last:", last)

#4.Explain in comments the difference between * in a function definition and * in a function call.

# * in a function definition collects multiple arguments.


def show_numbers(a, b, c):
    print(a, b, c)


numbers = [10, 20, 30]

show_numbers(*numbers)


#Part D – **kwargs

#Write show_profile(**info) and iterate over all key/value pairs.

def show_profile(**info):

    for key, value in info.items():
        print(key, ":", value)


show_profile(
    name="Gowtami",
    age=33,
    city="Gothenburg",
    course="Python"
)

#info collects named arguments into a dictionary.
#Then .items() gives us the key and value.

show_profile(name="Anna", age=22)
{
    "name": "Anna",
    "age": 22
}

#2.Write create_user(username, **details) returning one dictionary containing username plus all supplied details.

def create_user(username, **details):

    user = {
        "username": username
    }

    user.update(details)

    return user


user = create_user(
    "anna123",
    age=22,
    city="Stockholm",
    course="Python"
)

print(user)


#3.Write build_product(name, price, **metadata) returning a dictionary.

def build_product(name, price, **metadata):

    product = {
        "name": name,
        "price": price
    }

    product.update(metadata)

    return product


product = build_product(
    "Laptop",
    9000,
    brand="Dell",
    color="Silver",
    storage="512GB"
)

print(product)

#4.Write a function that accepts **settings and returns only settings whose value is not None.


def useful_settings(**settings):

    result = {}

    for key, value in settings.items():

        if value is not None:
            result[key] = value

    return result


settings = useful_settings(
    theme="dark",
    language="English",
    notifications=None,
    font_size=14
)

print(settings)


#5.Call a normal named-parameter function using ** dictionary unpacking. Ensure dictionary keys match parameter names.

def introduce(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")


person = {
    "name": "Gowtami",
    "age": 30,
    "city": "Gothenburg"
}

introduce(**person)

#Part E – Combining Parameters

#1.Create log_event(event_type, *messages, **metadata) returning a structured dictionary.

def log_event(event_type, *messages, **metadata):

    event = {
        "event_type": event_type,
        "messages": messages,
        "metadata": metadata
    }

    return event


result = log_event(
    "login",
    "User opened the website",
    "User entered password",
    username="anna123",
    device="Laptop"
)

print(result)

#2.Create calculate_order(customer, *prices, **options). Support an optional discount and shipping fee in options.

def calculate_order(customer, *prices, **options):

    total = 0

    # Add all product prices
    for price in prices:
        total = total + price

    # Get discount, or use 0 if no discount was given
    discount = options.get("discount", 0)

    # Get shipping fee, or use 0 if no shipping fee was given
    shipping = options.get("shipping", 0)

    discount_amount = total * discount / 100

    final_total = total - discount_amount + shipping

    return {
        "customer": customer,
        "original_total": total,
        "discount": discount,
        "shipping": shipping,
        "final_total": final_total
    }


order = calculate_order(
    "Anna",
    50,
    30,
    20,
    discount=10,
    shipping=5
)

print(order)

#3.Create a function where explicit named parameters would be clearer than **kwargs.
# Write both versions and compare readability in comments.

#Version 1 – using **kwargs

def create_student(**details):

    return details


student = create_student(
    name="Anna",
    age=22,
    course="Python"
)

print(student)


#Version 2 – explicit parameters

def create_student(name, age, course):

    return {
        "name": name,
        "age": age,
        "course": course
    }


student = create_student(
    "Anna",
    22,
    "Python"
)

print(student)

#So **kwargs is useful when the number or names of extra options can vary, 
# while explicit parameters are useful when the required information is known.

#4.Create at least three calls to the same flexible function with substantially different numbers of arguments

def add_all(*numbers):

    total = 0

    for number in numbers:
        total = total + number

    return total


# First call - 2 numbers
print(add_all(10, 20))

# Second call - 4 numbers
print(add_all(5, 10, 15, 20))

# Third call - 6 numbers
print(add_all(1, 2, 3, 4, 5, 6))


#Part F – Applied Challenge: Report Builder
#1. Build a flexible report system without files. create_report(title, *sections, **metadata)
# should return a dictionary.

def create_report(title, *sections, **metadata):
    report = {
        "title": title,
        "sections": sections,
        "metadata": metadata
    }

    return report


#2. Each section can be a string or a small dictionary; choose and document your design.

def create_report(title, *sections, **metadata):
    return {
        "title": title,
        "sections": sections,
        "metadata": metadata
    }


report = create_report(
    "My First Report",
    "This is the introduction.",
    {"heading": "Results", "text": "The results look good."},
    author="John",
    department="IT"
)

print(report)

#3.Metadata may include author, department, version, confidential and date.

report = create_report(
    "Annual Report",
    "This is the report introduction.",
    author="John",
    department="Finance",
    version="1.0",
    confidential=True,
    date="2026-09-18"
)

print(report)

#4. Write summarize_report(report) that returns a readable multi-line string.

def summarize_report(report):
    lines = []

    lines.append(f"Report: {report['title']}")
    lines.append("-" * 30)

    for number, section in enumerate(report["sections"], start=1):
        if isinstance(section, str):
            lines.append(f"Section {number}: {section}")

        elif isinstance(section, dict):
            heading = section.get("heading", f"Section {number}")
            text = section.get("text", "")
            lines.append(f"{heading}: {text}")

    if report["metadata"]:
        lines.append("")
        lines.append("Metadata:")

        for key, value in report["metadata"].items():
            lines.append(f"{key}: {value}")

    return "\n".join(lines)

report = create_report(
    "Sales Report",
    "Sales increased this year.",
    {"heading": "Conclusion", "text": "The company performed well."},
    author="John",
    version="1.0"
)

print(summarize_report(report))

#5.Write count_words(*sections) that counts words across all supplied textual sections.

def count_words(*sections):
    total_words = 0

    for section in sections:
        if isinstance(section, str):
            total_words += len(section.split())

        elif isinstance(section, dict):
            text = section.get("text", "")
            if isinstance(text, str):
                total_words += len(text.split())

    return total_words

section1 = "Python is easy to learn."
section2 = {"heading": "Results", "text": "The project was completed successfully."}

print(count_words(section1, section2))


#6.Use dictionary unpacking to create at least two reports from predefined metadata dictionaries.

metadata1 = {
    "author": "John",
    "department": "IT",
    "version": "1.0",
    "date": "2026-09-18"
}

metadata2 = {
    "author": "Sarah",
    "department": "Finance",
    "version": "2.0",
    "date": "2026-09-18",
    "confidential": True
}

report1 = create_report(
    "IT Report",
    "The IT department completed the project.",
    **metadata1
)

report2 = create_report(
    "Finance Report",
    "The finance department reviewed the budget.",
    **metadata2
)

print(summarize_report(report1))
print()
print(summarize_report(report2))

#7.Demonstrate at least one case where your function deliberately ignores or handles a missing optional metadata field.

def create_report(title, *sections, **metadata):
    return {
        "title": title,
        "sections": sections,
        "metadata": metadata
    }


report = create_report(
    "Simple Report",
    "This report does not have a confidentiality setting.",
    author="John",
    version="1.0"
)

print(report)

#Part G – Stretch Challenges
#1. Write merge_settings(defaults, **overrides) returning a new dictionary without modifying defaults.

def merge_settings(defaults, **overrides):
    settings = defaults.copy()
    settings.update(overrides)

    return settings


defaults = {
    "theme": "light",
    "font_size": 12,
    "language": "English"
}

new_settings = merge_settings(
    defaults,
    theme="dark",
    font_size=14
)

print("Default settings:", defaults)
print("New settings:", new_settings)

#2.Write call_summary(function_name, *args, **kwargs) returning a string describing what would be called.

def call_summary(function_name, *args, **kwargs):
    parts = []

    for arg in args:
        parts.append(repr(arg))

    for key, value in kwargs.items():
        parts.append(f"{key}={value!r}")

    arguments = ", ".join(parts)

    return f"Would call {function_name}({arguments})"


result = call_summary(
    "create_report",
    "Sales Report",
    "Sales increased.",
    author="John",
    version="1.0"
)

print(result)

#3.Write a flexible statistics function that returns count, total, average, min and max for *numbers. 
# Implement the calculations manually where reasonable

def statistics(*numbers):
    if len(numbers) == 0:
        return {
            "count": 0,
            "total": 0,
            "average": None,
            "min": None,
            "max": None
        }

    count = len(numbers)

    total = 0
    for number in numbers:
        total += number

    average = total / count

    smallest = numbers[0]
    largest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

        if number > largest:
            largest = number

    return {
        "count": count,
        "total": total,
        "average": average,
        "min": smallest,
        "max": largest
    }


print(statistics(10, 20, 30, 40, 50))

#4.Create five "predict the output" questions and verify your predictions.

#example1:

def add_numbers(*numbers):
    return sum(numbers)

print(add_numbers(2, 4, 6))


#example2:

def show_info(name, **details):
    print(name)
    print(details)

show_info("John", age=25, city="Stockholm")

#example3:

def merge_settings(defaults, **overrides):
    settings = defaults.copy()
    settings.update(overrides)
    return settings

defaults = {"mode": "normal", "size": 10}

print(merge_settings(defaults, size=20))
print(defaults)

#example4:

def count_words(*sections):
    total = 0

    for section in sections:
        total += len(section.split())

    return total

print(count_words("Python is fun", "I like coding"))

#example5:

metadata = {
    "author": "John",
    "version": "1.0"
}

def create_report(title, **metadata):
    return {
        "title": title,
        "metadata": metadata
    }

report = create_report("Python Report", **metadata)

print(report["title"])
print(report["metadata"]["author"])












