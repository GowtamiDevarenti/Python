#Part A — Conditions
#1. Create squares for numbers 1–20 using a normal loop, 
# then a list comprehension.
squares = []

for number in range(1, 21):
    squares.append(number ** 2)

print(squares)

#List Comprehension:

squares = [number ** 2 for number in range(1, 21)]

print(squares)


#2. Create a list containing only even numbers from 1–100.

even_numbers = []

for number in range(1, 101):
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

#3. Convert a list of names to stripped, title-cased names.

names = [" alice ", "BOB", " charlie ", "DAVID "]

clean_names = [name.strip().title() for name in names]

print(clean_names)

#4.Given scores, create a list containing only passing scores.

scores = [35, 72, 48, 90, 55, 41, 83]

passing_scores = [score for score in scores if score >= 50]

print(passing_scores)

#5.Create labels such as PASS/FAIL for every score using a 
# conditional expression in a comprehension.

scores = [35, 72, 48, 90, 55, 41, 83]

results = ["PASS" if score >= 50 else "FAIL" for score in scores]

print(results)

#6. Rewrite three earlier loop-based transformations from Lessons 2–4 as comprehensions.

#Example 1 — double numbers:

numbers = [1, 2, 3, 4, 5]

doubled = [number * 2 for number in numbers]

print(doubled)

#Example 2 — convert names to uppercase:

names = ["alice", "bob", "charlie"]

upper_names = [name.upper() for name in names]

print(upper_names)

#Example 3 — keep numbers greater than 10:

numbers = [5, 12, 8, 20, 15, 3]

large_numbers = [number for number in numbers if number > 10]

print(large_numbers)


#Part B — Dictionary and Set Comprehensions

#1. Create a dictionary mapping numbers 1–10 to their squares.

squares = {number: number ** 2 for number in range(1, 11)}

print(squares)

#2.Given a list of words, create a dictionary mapping each word to its length.

words = ["apple", "banana", "cat", "elephant"]

word_lengths = {word: len(word) for word in words}
                               
print(word_lengths)

#3. Given a list with duplicates, create a set comprehension containing lowercase normalized values

words = ["Apple", "APPLE", " banana ", "Banana", "ORANGE"]

clean_words = {word.strip().lower() for word in words}

print(clean_words)

#4.Create a dictionary of only products whose price is below a chosen threshold.

products = {
    "Laptop": 900,
    "Mouse": 25,
    "Keyboard": 60,
    "Monitor": 150
}

cheap_products = {
    name: price
    for name, price in products.items()
    if price < 100
}

print(cheap_products)

#5. Create a dictionary mapping student names to PASS/FAIL from a list of student dictionaries.

students = [
    {"name": "Alice", "score": 75},
    {"name": "Bob", "score": 42},
    {"name": "Charlie", "score": 88},
    {"name": "David", "score": 35}
]

results = {
    student["name"]: "PASS" if student["score"] >= 50 else "FAIL"
    for student in students
}

print(results)


#Part C — enumerate

#1. Print a playlist with numbering starting at 1 using enumerate.

playlist = ["Imagine", "Yesterday", "Halo", "Perfect"]

for number, song in enumerate(playlist, start=1):
    print(number, song)
    
#2. Given a list of tasks, print Task 1:, Task 2: etc.

tasks = ["Study Python", "Do homework", "Go shopping", "Clean room"]

for number, task in enumerate(tasks, start=1):
    print(f"Task {number}: {task}")
    
#3.Find and print indexes of all values above a threshold.

#I'll use 50 as the threshold.

scores = [35, 72, 48, 90, 55, 41, 83]

for index, score in enumerate(scores):
    if score > 50:
        print(index)
        
#4.Rewrite a range(len(...)) loop using enumerate and explain why the new version is clearer.

#Old Version:

names = ["Alice", "Bob", "Charlie"]

for i in range(len(names)):
    print(i, names[i])
    
    
#Using enumerate:

for index, name in enumerate(names):
    print(index, name)

#Part D — zip and Unpacking

#1. Combine separate name and score lists using zip and print each pair.
names = ["Alice", "Bob", "Charlie"]
scores = [85, 72, 91]

for name, score in zip(names, scores):
    print(name, score)

#2. Create a dictionary using dict(zip(keys, values)).
keys = ["name", "age", "city"]
values = ["Alice", 22, "Stockholm"]

person = dict(zip(keys, values))

print(person)


#3. Combine three lists: product name, price and stock.
products = ["Laptop", "Mouse", "Keyboard"]
prices = [900, 25, 60]
stock = [5, 20, 15]

for name, price, amount in zip(products, prices, stock):
    print(name, price, amount)

#4. Investigate what happens when zipped lists have different lengths.
names = ["Alice", "Bob", "Charlie"]
scores = [80, 90]

for name, score in zip(names, scores):
    print(name, score)
    
#zip() stops when the shortest list runs out of values. So "Charlie" is not included.


#5. Use tuple unpacking directly in a for loop over zipped data.

names = ["Alice", "Bob", "Charlie"]
scores = [80, 90, 75]

for name, score in zip(names, scores):
    print(f"{name} got {score}")
    
#automatically unpack the tuple created by zip().

#6. Swap two variables without a temporary variable.

a = 10
b = 20

a, b = b, a

print(a)
print(b)

#Part E — sorted and lambda
#1. Sort a list of words by length using sorted(..., key=...).

words = ["apple", "cat", "elephant", "dog", "hi"]

sorted_words = sorted(words, key=len)

print(sorted_words)

#2. Sort a list of student dictionaries by score ascending and descending.
students = [
    {"name": "Aliya", "score": 85},
    {"name": "Boby", "score": 62},
    {"name": "Gowtami", "score": 91}
]

ascending = sorted(students,key =lambda student:student["score"])
print(ascending)

descending = sorted(
    students,
    key=lambda student: student["score"],
    reverse=True
)

print(descending)

#3. Sort products by price using a lambda.

products = [
    {"name": "Laptop", "price": 900},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 60}
]

sorted_products = sorted(
    products,
    key=lambda product: product["price"]
)

print(sorted_products)

#4. Sort people by last name when each item is a dictionary 
# containing first_name and last_name.

people = [
    {"first_name": "John", "last_name": "Smith"},
    {"first_name": "Alice", "last_name": "Brown"},
    {"first_name": "David", "last_name": "Andersson"}
]

sorted_people = sorted(
    people,
    key=lambda person: person["last_name"]
)

print(sorted_people)

#5. Write a normal named function for a sort key,
# then replace it with lambda. Compare when each is clearer.

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 62},
    {"name": "Charlie", "score": 91}
]

def get_score(student):
    return student["score"]

sorted_students = sorted(students, key=get_score)

print(sorted_students)

sorted_students = sorted(
    students,
    key=lambda student: student["score"]
)

print(sorted_students)

#For a small, one-time sorting operation, the lambda version is shorter. A named function can be clearer
# when the sorting rule is more complicated or will be reused.

#Part F — Applied Challenge: Data Cleanup
#1. Start with a list of at least twelve messy dictionaries representing 
#products: inconsistent name casing/spacing, category, price and stock.

products = [
    {"name": " laptop ", "category": " electronics ", "price": 9000, "stock": 5},
    {"name": "MOUSE", "category": "Electronics", "price": 250, "stock": 20},
    {"name": " keyboard ", "category": " ELECTRONICS", "price": 600, "stock": 15},
    {"name": "phone", "category": " electronics ", "price": 7000, "stock": 8},
    {"name": " HEADPHONES ", "category": "Electronics", "price": 800, "stock": 12},
    {"name": "desk ", "category": " furniture", "price": 1200, "stock": 4},
    {"name": " CHAIR", "category": "Furniture ", "price": 200, "stock": 10},
    {"name": "lamp", "category": " FURNITURE", "price": 450, "stock": 7},
    {"name": "notebook ", "category": " stationery", "price": 40, "stock": 30},
    {"name": " PEN", "category": "Stationery", "price": 30, "stock": 50},
    {"name": "BACKPACK ", "category": " stationery ", "price": 450, "stock": 0},
    {"name": " tablet", "category": "ELECTRONICS ", "price": 4000, "stock": 6}
]


#2.Create a cleaned list where names/categories are normalized. 
# Use comprehensions where readable.

cleaned_products = [
    {
        "name": product["name"].strip().title(),
        "category": product["category"].strip().title(),
        "price": product["price"],
        "stock": product["stock"]
    }
    for product in products
]

print(cleaned_products)

#3.Create a list of in-stock products.

in_stock = [
    product
    for product in cleaned_products
    if product["stock"] > 0
]

print(in_stock)

#4.Create a set of unique normalized categories.
categories = {
    product["category"]
    for product in cleaned_products
}

print(categories)

#5. Create 
# a dictionary mapping product name to inventory value (price * stock).
inventory_values = {
    product["name"]: product["price"] * product["stock"]
    for product in cleaned_products
}

print(inventory_values)

#6. Sort products by inventory value from highest to lowest.

sorted_products = sorted(
    cleaned_products,
    key=lambda product: product["price"] * product["stock"],
    reverse=True
)

print(sorted_products)

#7. Use enumerate to print a ranked report.

for rank, product in enumerate(sorted_products, start=1):
    value = product["price"] * product["stock"]

    print(
        f"{rank}. {product['name']} - "
        f"Inventory value: {value}"
    )
    
#8. Use zip to combine 
# at least one pair of separate derived lists in a meaningful way.


names = [product["name"] for product in sorted_products]

values = [
    product["price"] * product["stock"]
    for product in sorted_products
]

for name, value in zip(names, values):
    print(f"{name}: {value}")
    
#9. Write both a deliberately over-complicated comprehension and a clearer alternative. 
#Explain why the clearer version wins.

#Over-complicated:

result = [
    product["name"].strip().title()
    for product in products
    if product["stock"] > 0
    if product["price"] * product["stock"] > 100
    if product["category"].strip().lower() == "electronics"
]

#Clearer alternative:

electronics = [
    product
    for product in products
    if product["category"].strip().lower() == "electronics"
]

valuable_products = [
    product
    for product in electronics
    if product["stock"] > 0
    and product["price"] * product["stock"] > 100
]

names = [
    product["name"].strip().title()
    for product in valuable_products
]

print(names)

#The second version is easier to read and debug because each step has one clear purpose.

#Part G — Stretch Challenges
#1. Flatten a simple list of lists using a comprehension.

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [
    number
    for row in numbers
    for number in row
]

print(flattened)

#2. Create a multiplication table structure using a nested comprehension,
# then decide whether the result is readable enough.

table = [
    [row * column for column in range(1, 11)]
    for row in range(1, 11)
]

print(table)

#3. Given names and scores, 
# create only passing student dictionaries in one readable comprehension.

names = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 42, 91, 35]

passing_students = [
    {"name": name, "score": score}
    for name, score in zip(names, scores)
    if score >= 50
]

print(passing_students)

#4. Use any() and all() to answer useful questions about a score list, 
# after first solving them with loops.

scores = [65, 72, 81, 90]

#I opened the shared ChatGPT conversation, but its contents aren’t available to me through the shared-page view.

"""Please paste the relevant conversation here (or upload screenshots), and I can continue from exactly where it left off.

printnt all the qustionns in this limk Lab 6.pdf

Yes. I can print all the questions from Lab 6, but the SharePoint PDF link isn’t accessible from here—it returned an access/fetch error.

Please upload Lab 6.pdf directly in this chat. Once you upload it, I’ll extract and list every question exactly as it appears, in order, without solving them.

Lab 6.pdf
PDF
analyse tyhe pdf print all the questions and give humanised python code for each question


I analyzed the uploaded Lab 6.pdf. It is a 3-page scanned PDF, so the text layer itself is empty; I extracted the questions from the page images. The lab covers list/dictionary/set comprehensions, enumerate, zip, unpacking, sorted/lambda, data cleanup, and stretch challenges.

Below I’ve kept the original question order and wording, followed by simple, human-readable Python for each task.

Lab 6 — Questions + Humanized Python Solutions"""
Part A — List Comprehensions
1. Create squares for numbers 1–20 using a normal loop, then a list comprehension.

Normal loop:

squares = []

for number in range(1, 21):
    squares.append(number ** 2)

print(squares)

List comprehension:

squares = [number ** 2 for number in range(1, 21)]

print(squares)
2. Create a list containing only even numbers from 1–100.
even_numbers = []

for number in range(1, 101):
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

Using comprehension:

even_numbers = [number for number in range(1, 101) if number % 2 == 0]

print(even_numbers)
3. Convert a list of names to stripped, title-cased names.
names = [" alice ", "BOB", " charlie ", "DAVID "]

clean_names = [name.strip().title() for name in names]

print(clean_names)

Output:

['Alice', 'Bob', 'Charlie', 'David']
4. Given scores, create a list containing only passing scores.

I'll use 50 as the passing score.

scores = [35, 72, 48, 90, 55, 41, 83]

passing_scores = [score for score in scores if score >= 50]

print(passing_scores)
5. Create labels such as PASS/FAIL for every score using a conditional expression in a comprehension.
scores = [35, 72, 48, 90, 55, 41, 83]

results = ["PASS" if score >= 50 else "FAIL" for score in scores]

print(results)

Output:

['FAIL', 'PASS', 'FAIL', 'PASS', 'PASS', 'FAIL', 'PASS']
6. Rewrite three earlier loop-based transformations from Lessons 2–4 as comprehensions.

Here are three simple examples.

Example 1 — double numbers:

numbers = [1, 2, 3, 4, 5]

doubled = [number * 2 for number in numbers]

print(doubled)

Example 2 — convert names to uppercase:

names = ["alice", "bob", "charlie"]

upper_names = [name.upper() for name in names]

print(upper_names)

Example 3 — keep numbers greater than 10:

numbers = [5, 12, 8, 20, 15, 3]

large_numbers = [number for number in numbers if number > 10]

print(large_numbers)
Part B — Dictionary and Set Comprehensions
1. Create a dictionary mapping numbers 1–10 to their squares.
squares = {number: number ** 2 for number in range(1, 11)}

print(squares)

The result starts like:

{1: 1, 2: 4, 3: 9, 4: 16, ...}
2. Given a list of words, create a dictionary mapping each word to its length.
words = ["apple", "banana", "cat", "elephant"]

word_lengths = {word: len(word) for word in words}

print(word_lengths)

Output:

{'apple': 5, 'banana': 6, 'cat': 3, 'elephant': 8}
3. Given a list with duplicates, create a set comprehension containing lowercase normalized values.
words = ["Apple", "APPLE", " banana ", "Banana", "ORANGE"]

clean_words = {word.strip().lower() for word in words}

print(clean_words)

This removes duplicates because a set only keeps unique values.

4. Create a dictionary of only products whose price is below a chosen threshold.

I'll choose 100 as the threshold.

products = {
    "Laptop": 900,
    "Mouse": 25,
    "Keyboard": 60,
    "Monitor": 150
}

cheap_products = {
    name: price
    for name, price in products.items()
    if price < 100
}

print(cheap_products)
5. Create a dictionary mapping student names to PASS/FAIL from a list of student dictionaries.
students = [
    {"name": "Alice", "score": 75},
    {"name": "Bob", "score": 42},
    {"name": "Charlie", "score": 88},
    {"name": "David", "score": 35}
]

results = {
    student["name"]: "PASS" if student["score"] >= 50 else "FAIL"
    for student in students
}

print(results)
Part C — enumerate
1. Print a playlist with numbering starting at 1 using enumerate.
playlist = ["Imagine", "Yesterday", "Halo", "Perfect"]

for number, song in enumerate(playlist, start=1):
    print(number, song)

Output:

1 Imagine
2 Yesterday
3 Halo
4 Perfect
2. Given a list of tasks, print Task 1:, Task 2: etc.
tasks = ["Study Python", "Do homework", "Go shopping", "Clean room"]

for number, task in enumerate(tasks, start=1):
    print(f"Task {number}: {task}")
3. Find and print indexes of all values above a threshold.

I'll use 50 as the threshold.

scores = [35, 72, 48, 90, 55, 41, 83]

for index, score in enumerate(scores):
    if score > 50:
        print(index)

If you want to print both the index and score:

for index, score in enumerate(scores):
    if score > 50:
        print(f"Index {index}: {score}")
4. Rewrite a range(len(...)) loop using enumerate and explain why the new version is clearer.

Old version:

names = ["Alice", "Bob", "Charlie"]

for i in range(len(names)):
    print(i, names[i])

Using enumerate:

for index, name in enumerate(names):
    print(index, name)

enumerate() is clearer because we directly receive both the index and the value. We don't need to manually use names[i].

Part D — zip and Unpacking
1. Combine separate name and score lists using zip and print each pair.
names = ["Alice", "Bob", "Charlie"]
scores = [85, 72, 91]

for name, score in zip(names, scores):
    print(name, score)
2. Create a dictionary using dict(zip(keys, values)).
keys = ["name", "age", "city"]
values = ["Alice", 22, "Stockholm"]

person = dict(zip(keys, values))

print(person)

Output:

{'name': 'Alice', 'age': 22, 'city': 'Stockholm'}
3. Combine three lists: product name, price and stock.
products = ["Laptop", "Mouse", "Keyboard"]
prices = [900, 25, 60]
stock = [5, 20, 15]

for name, price, amount in zip(products, prices, stock):
    print(name, price, amount)
4. Investigate what happens when zipped lists have different lengths.
names = ["Alice", "Bob", "Charlie"]
scores = [80, 90]

for name, score in zip(names, scores):
    print(name, score)

Output:

Alice 80
Bob 90

zip() stops when the shortest list runs out of values. So "Charlie" is not included.

5. Use tuple unpacking directly in a for loop over zipped data.
names = ["Alice", "Bob", "Charlie"]
scores = [80, 90, 75]

for name, score in zip(names, scores):
    print(f"{name} got {score}")

Here:

name, score

automatically unpack the tuple created by zip().

6. Swap two variables without a temporary variable.
a = 10
b = 20

a, b = b, a

print(a)
print(b)

Output:

20
10
Part E — sorted and lambda
1. Sort a list of words by length using sorted(..., key=...).
words = ["apple", "cat", "elephant", "dog", "hi"]

sorted_words = sorted(words, key=len)

print(sorted_words)

Output:

['hi', 'cat', 'dog', 'apple', 'elephant']
2. Sort a list of student dictionaries by score ascending and descending.
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 62},
    {"name": "Charlie", "score": 91}
]

Ascending:

ascending = sorted(students, key=lambda student: student["score"])

print(ascending)

Descending:

descending = sorted(
    students,
    key=lambda student: student["score"],
    reverse=True
)

print(descending)
3. Sort products by price using a lambda.
products = [
    {"name": "Laptop", "price": 900},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 60}
]

sorted_products = sorted(
    products,
    key=lambda product: product["price"]
)

print(sorted_products)
4. Sort people by last name when each item is a dictionary containing first_name and last_name.
people = [
    {"first_name": "John", "last_name": "Smith"},
    {"first_name": "Alice", "last_name": "Brown"},
    {"first_name": "David", "last_name": "Andersson"}
]

sorted_people = sorted(
    people,
    key=lambda person: person["last_name"]
)

print(sorted_people)
5. Write a normal named function for a sort key, then replace it with lambda. Compare when each is clearer.

Normal function:

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 62},
    {"name": "Charlie", "score": 91}
]

def get_score(student):
    return student["score"]

sorted_students = sorted(students, key=get_score)

print(sorted_students)

Using lambda:

sorted_students = sorted(
    students,
    key=lambda student: student["score"]
)

print(sorted_students)

For a small, one-time sorting operation, the lambda version is shorter. A named function can be clearer when the sorting rule is more complicated or will be reused.

Part F — Applied Challenge: Data Cleanup
1. Start with a list of at least twelve messy dictionaries representing products: inconsistent name casing/spacing, category, price and stock.
products = [
    {"name": " laptop ", "category": " electronics ", "price": 900, "stock": 5},
    {"name": "MOUSE", "category": "Electronics", "price": 25, "stock": 20},
    {"name": " keyboard ", "category": " ELECTRONICS", "price": 60, "stock": 15},
    {"name": "phone", "category": " electronics ", "price": 700, "stock": 8},
    {"name": " HEADPHONES ", "category": "Electronics", "price": 80, "stock": 12},
    {"name": "desk ", "category": " furniture", "price": 200, "stock": 4},
    {"name": " CHAIR", "category": "Furniture ", "price": 120, "stock": 10},
    {"name": "lamp", "category": " FURNITURE", "price": 45, "stock": 7},
    {"name": "notebook ", "category": " stationery", "price": 8, "stock": 30},
    {"name": " PEN", "category": "Stationery", "price": 3, "stock": 50},
    {"name": "BACKPACK ", "category": " stationery ", "price": 40, "stock": 0},
    {"name": " tablet", "category": "ELECTRONICS ", "price": 400, "stock": 6}
]
2. Create a cleaned list where names/categories are normalized. Use comprehensions where readable.
cleaned_products = [
    {
        "name": product["name"].strip().title(),
        "category": product["category"].strip().title(),
        "price": product["price"],
        "stock": product["stock"]
    }
    for product in products
]

print(cleaned_products)
3. Create a list of in-stock products.
in_stock = [
    product
    for product in cleaned_products
    if product["stock"] > 0
]

print(in_stock)
4. Create a set of unique normalized categories.
categories = {
    product["category"]
    for product in cleaned_products
}

print(categories)

You should get categories such as:

{'Electronics', 'Furniture', 'Stationery'}
5. Create a dictionary mapping product name to inventory value (price * stock).
inventory_values = {
    product["name"]: product["price"] * product["stock"]
    for product in cleaned_products
}

print(inventory_values)
6. Sort products by inventory value from highest to lowest.
sorted_products = sorted(
    cleaned_products,
    key=lambda product: product["price"] * product["stock"],
    reverse=True
)

print(sorted_products)
7. Use enumerate to print a ranked report.
for rank, product in enumerate(sorted_products, start=1):
    value = product["price"] * product["stock"]

    print(
        f"{rank}. {product['name']} - "
        f"Inventory value: {value}"
    )
8. Use zip to combine at least one pair of separate derived lists in a meaningful way.

For example, combine product names with their inventory values:

names = [product["name"] for product in sorted_products]

values = [
    product["price"] * product["stock"]
    for product in sorted_products
]

for name, value in zip(names, values):
    print(f"{name}: {value}")
9. Write both a deliberately over-complicated comprehension and a clearer alternative. Explain why the clearer version wins.

Over-complicated:

result = [
    product["name"].strip().title()
    for product in products
    if product["stock"] > 0
    if product["price"] * product["stock"] > 100
    if product["category"].strip().lower() == "electronics"
]

This works, but it is starting to do too many things at once.

Clearer alternative:

electronics = [
    product
    for product in products
    if product["category"].strip().lower() == "electronics"
]

valuable_products = [
    product
    for product in electronics
    if product["stock"] > 0
    and product["price"] * product["stock"] > 100
]

names = [
    product["name"].strip().title()
    for product in valuable_products
]

print(names)

The second version is easier to read and debug because each step has one clear purpose.

Part G — Stretch Challenges
1. Flatten a simple list of lists using a comprehension.
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [
    number
    for row in numbers
    for number in row
]

print(flattened)

Output:

[1, 2, 3, 4, 5, 6, 7, 8, 9]
2. Create a multiplication table structure using a nested comprehension, then decide whether the result is readable enough.
table = [
    [row * column for column in range(1, 11)]
    for row in range(1, 11)
]

print(table)

For example, the first row is:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

The second row is:

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

The nested comprehension is compact, but for beginners, a normal nested loop may be easier to understand.

3. Given names and scores, create only passing student dictionaries in one readable comprehension.
names = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 42, 91, 35]

passing_students = [
    {"name": name, "score": score}
    for name, score in zip(names, scores)
    if score >= 50
]

print(passing_students)
4. Use any() and all() to answer useful questions about a score list, after first solving them with loops.
scores = [65, 72, 81, 90]

#First, using a loop — does anyone fail?

has_failed = False

for score in scores:
    if score < 50:
        has_failed = True

print(has_failed)

#Using any():

has_failed = any(score < 50 for score in scores)

print(has_failed)

#Using a loop — did everyone pass?

everyone_passed = True

for score in scores:
    if score < 50:
        everyone_passed = False

print(everyone_passed)


#Using all():

everyone_passed = all(score >= 50 for score in scores)

print(everyone_passed)

#5. Create five examples where Pythonic syntax reduces boilerplate without reducing clarity.
#Example 1 — List comprehension
#Instead of:

numbers = []

for number in range(1, 6):
    numbers.append(number * 2)
    
#Use:
numbers = [number * 2 for number in range(1, 6)]

#Example 2 — enumerate

#Instead of:

names = ["Alice", "Bob", "Charlie"]

for i in range(len(names)):
    print(i, names[i])

#Use:

for i, name in enumerate(names):
    print(i, name)

#Example 3 — zip

#Instead of manually accessing two lists:

names = ["Alice", "Bob"]
scores = [80, 90]

for i in range(len(names)):
    print(names[i], scores[i])

#Use:

for name, score in zip(names, scores):
    print(name, score)
    
Example 4 — Dictionary comprehension
numbers = [1, 2, 3, 4, 5]

squares = {number: number ** 2 for number in numbers}

print(squares)

#Example 5 — Swapping variables

#Instead of using a temporary variable:

a = 10
b = 20

a, b = b, a

print(a, b)

#This uses Python's tuple unpacking to make the operation short and readable.
