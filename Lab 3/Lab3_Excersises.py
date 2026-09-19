#Part A — Conditions
#1. Write a program that classifies a number as positive, negative or zero.

number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")    
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
    
    
    
 #2.Ask for an age and classify it into at least four age groups using if/elif/else.
age = int(input("Enter an age: "))
if age < 0:
    print("Invalid age.")
elif age < 13:
    print("The person is a child.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is a senior citizen.")    
    
#3. Create a login check using a stored username and password. Both must match.                                
stored_username = "Gowtami"
stored_password = "python92"

username = input("Enter username: ")
password = input("Enter password: ")

if username == stored_username and password == stored_password:
    print("Login successful.")
else:
    print("Invalid username or password.")

#4. Given a score from 0-100, print a grade using at least five ranges. Think carefully about condition order.


score = int(input("Enter your score from 0 to 100: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
    
    
#5. Create a shipping rule based on order total and whether the customer is a member. Use and/or.

order_total = float(input("Enter the order total: "))
is_member = input("Are you a member? (yes/no): ").lower() == "yes"

if order_total > 100 and is_member:
    print("Free shipping!")
elif order_total > 50 and is_member:
    print("Shipping cost: 20sek")
else:
    print("Shipping cost: 40sek")


#6. Write five expressions using ==, !=, >, <, >= and <= and predict each boolean result before running.

print(5 == 5)  # Predict: True
print(5 != 5)  # Predict: False
print(5 > 3)   # Predict: True
print(5 < 3)   # Predict: False
print(5 >= 5)  # Predict: True
print(5 <= 3)  # Predict: False

#Part B — Truthy, False and Membership
#1. Create examples with empty string, non-empty string, zero, non-zero integer, empty list and non-empty list.
# Test each directly in an if statement.

empty_string = ""
non_empty_string = "Hello"
zero_integer = 0
non_zero_integer = 5
empty_list = []
non_empty_list = [1, 2, 3]

if empty_string:
    print("Empty string is truthy.")
else:
    print("Empty string is falsy.")

if non_empty_string:
    print("Non-empty string is truthy.")
else:
    print("Non-empty string is falsy.")

if zero_integer:
    print("Zero integer is truthy.")
else:
    print("Zero integer is falsy.")

if non_zero_integer:
    print("Non-zero integer is truthy.")
else:
    print("Non-zero integer is falsy.")

if empty_list:
    print("Empty list is truthy.")
else:
    print("Empty list is falsy.")

if non_empty_list:
    print("Non-empty list is truthy.")
else:
    print("Non-empty list is falsy.")
    
    
#2. Ask for a language and check whether it exists in a predefined list of supported languages.
supported_languages = ["Python", "Java", "C++", "JavaScript"]

language = input("Enter a programming language: ")

if language in supported_languages:
    print(f"{language} is a supported language.")
else:
    print(f"{language} is not a supported language.")
    
#3. Create a list of blocked usernames and reject a supplied username if it appears in the list.

blocked_usernames = ["admin", "moderator", "user123"]

username = input("Enter your username: ")

if username in blocked_usernames:
    print(f"Username '{username}' is blocked.")
else:
    print(f"Username '{username}' is allowed.")
    
#4. Use not to express at least two conditions in a readable way.

password = input("Enter your password: ")

if not password:
    print("You did not enter a password.")
else:
    print("Password entered successfully.")


age = int(input("Enter your age: "))

if not age >= 18:
    print("You are under 18.")
else:
    print("You are 18 or older.")
    
#Part C — For Loops
#1. Loop over a list of names and print a numbered greeting for each.

names = ["Alice", "Bob", "Charlie"]
for i, name in enumerate(names, start=1):
    print(f"{i}. Hello, {name}!")
    
#2. Loop over numbers 1-50 and print only even numbers.

for number in range(1, 51):
    if number % 2 == 0:
        print(number)
        
#3. Calculate the sum of a list manually using a loop rather than sum().

numbers = [1, 2, 3, 4, 5]
total = 0

for number in numbers:
    total += number                         
    
print(f"The sum of the list is: {total}")

#4.Find the largest number in a list manually without max().

numbers = [1, 2, 3, 4, 5]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(f"The largest number in the list is: {largest}")

#5.5. Count how many words in a list have more than five characters.

words = ["apple", "banana", "cherry", "date", "elderberry"]
count = 0           

for word in words:
    if len(word) > 5:
        count += 1

print(f"Number of words with more than five characters: {count}")

#6. Given a list of scores, count passes and failures using a threshold of 70.

scores = [85, 42, 77, 90, 65, 58, 73]
pass_count = 0  
fail_count = 0

for score in scores:
    if score >= 70:
        pass_count += 1
    else:
        fail_count += 1
        

print(f"Number of passes: {pass_count}")
print(f"Number of failures: {fail_count}")

#7. Loop over a dictionary using keys, values and .items() in three separate examples.

student_grades = {"Alice": 85, "Bob": 42, "Charlie": 77}

# Using keys()
for name in student_grades:
    print(f"{name}: {student_grades[name]}")

# Using values()
for grade in student_grades.values():
    print(grade)

# Using .items()
for name, grade in student_grades.items():
    print(f"{name}: {grade}")   

#Part D — Range, Enumerate and Nested Loops
#1. Use range to print 10 down to 1.

for number in range(10, 0, -1):
    print(number)
    
#2. Generate the multiplication table for a number supplied by the user.

number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


#3. Use enumerate to print a playlist with track numbers starting at 1.

playlist = ("Perfect", "Believer", "Shape of You","Blinding Lights", "Someone Like You", "Rolling in the Deep")

for track_number, song in enumerate(playlist, start=1):
    print(track_number, "-", song)


#4. Use nested loops to print coordinate pairs for x=1..3 and y=1..4.

for x in range(1, 4):
    for y in range(1, 5):
        print("(", x, ",", y, ")")
        
        
#5. Create a simple 5x5 text grid using nested loops.

for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()  # Move to the next line after each row 
    
#Part E — While Loops
#1. Create a countdown from 10 to 0.

countdown = 10
while countdown >= 0:
    print(countdown)
    countdown -= 1      
print("Countdown complete!")

#2. Ask repeatedly for a password until the correct password is entered.

correct_password = "Gowtami123"

password = input("Enter the password: ")

while password != correct_password:
    print("Wrong password. Try again.")
    password = input("Enter the password: ")

print("Correct password! Welcome.")


#3. Create a menu that repeats until the user chooses 'quit'. The menu can simply print which option was selected.

choice = ""

while choice != "quit":
    print("\n--- Menu ---")
    print("1. Start")
    print("2. Settings")
    print("3. Help")
    print("Type 'quit' to exit.")

    choice = input("Choose an option: ")

    if choice == "1":
        print("You selected Start.")
    elif choice == "2":
        print("You selected Settings.")
    elif choice == "3":
        print("You selected Help.")
    elif choice == "quit":
        print("Goodbye!")
    else:
        print("That is not a valid option.")
        
#4. Ask the user for numbers until they enter 0. Keep a running total.

total = 0

number = int(input("Enter a number (0 to stop): "))

while number != 0:
    total += number
    number = int(input("Enter another number (0 to stop): "))

print("The total is:", total)

#5.Create a guessing loop with a fixed secret number. Tell the user whether each guess is too high or too low.

secret_number = 25

guess = int(input("Guess the secret number: "))

while guess != secret_number:

    if guess > secret_number:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")

    guess = int(input("Try again: "))

print("Congratulations! You guessed the correct number.")


#Part F – break and continue

#1. Loop through numbers 1–100 and stop when you reach the first number divisible by both 7 and 9.

for number in range(1, 101):
    if number % 7 == 0 and number % 9 == 0:
        print("First number divisible by both 7 and 9:", number)
        break
    
#2. Loop through a list of strings and skip empty strings using continue.

strings = ["Hello", "", "Python", "", "World", "Programming"]

for text in strings:
    if text == "":
        continue

    print(text)
    
#3. Search a list for a target name. Print "found" and break when it appears; otherwise
# explain how you know it was not found.

names = ["Alice", "Bob", "Charlie", "David", "Emma"]
target = "Charlie"

for name in names:
    if name == target:
        print("found")
        break
else:
    print("The name was not found because the loop finished without finding it.")
    
#4. Process a list of numeric values where negative values 
# should be skipped and processing stops completely when the value 999 appears.

numbers = [10, -5, 20, -3, 30, 999, 40, 50]

for number in numbers:
    if number == 999:
        print("999 found. Stopping processing.")
        break

    if number < 0:
        continue

    print("Processing:", number)
    
#Part G – Applied Challenge: Console Study Tracker


#1. Create a list of dictionaries representing at least ten study sessions with subject and minutes.

sessions = [
    {"subject": "Python", "minutes": 60},
    {"subject": "Math", "minutes": 45},
    {"subject": "English", "minutes": 30},
    {"subject": "Physics", "minutes": 50},
    {"subject": "Python", "minutes": 40},
    {"subject": "Math", "minutes": 70},
    {"subject": "History", "minutes": 35},
    {"subject": "English", "minutes": 55},
    {"subject": "Physics", "minutes": 65},
    {"subject": "Python", "minutes": 80}
]

#2. Loop through the sessions and calculate total minutes.

total_minutes = 0

for session in sessions:
    total_minutes += session["minutes"]

print("Total study time:", total_minutes, "minutes")


#3. Calculate total minutes per subject using a dictionary that starts empty and is updated inside the loop.

minutes_per_subject = {}

for session in sessions:
    subject = session["subject"]
    minutes = session["minutes"]

    if subject not in minutes_per_subject:
        minutes_per_subject[subject] = 0

    minutes_per_subject[subject] += minutes

print(minutes_per_subject)

#4. Identify the longest study session without max(..., key=...).

longest_session = sessions[0]

for session in sessions:
    if session["minutes"] > longest_session["minutes"]:
        longest_session = session

print("Longest study session:")
print(longest_session)

#5. Print only sessions longer than 45 minutes.

print("Sessions longer than 45 minutes:")

for session in sessions:
    if session["minutes"] > 45:
        print(session["subject"], "-", session["minutes"], "minutes")
    
#6.Create a repeated menu that lets a user view all sessions, view total time, filter by subject, or quit.
sessions = [
    {"subject": "Python", "minutes": 60},
    {"subject": "Math", "minutes": 45},
    {"subject": "English", "minutes": 30},
    {"subject": "Physics", "minutes": 50},
    {"subject": "Python", "minutes": 40},
    {"subject": "Math", "minutes": 70},
    {"subject": "History", "minutes": 35},
    {"subject": "English", "minutes": 55},
    {"subject": "Physics", "minutes": 65},
    {"subject": "Python", "minutes": 80}
]

while True:
    print("\n--- Study Tracker Menu ---")
    print("1. View all sessions")
    print("2. View total study time")
    print("3. Filter by subject")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAll study sessions:")

        for session in sessions:
            print(
                session["subject"],
                "-",
                session["minutes"],
                "minutes"
            )

    elif choice == "2":
        total = 0

        for session in sessions:
            total += session["minutes"]

        print("Total study time:", total, "minutes")

    elif choice == "3":
        subject = input("Enter subject: ")

        found = False

        for session in sessions:
            if session["subject"].lower() == subject.lower():
                print(
                    session["subject"],
                    "-",
                    session["minutes"],
                    "minutes"
                )
                found = True

        if not found:
            print("No sessions found for that subject.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
        
        
 #7. Use break/continue where they genuinely improve the flow.
 
    for session in sessions:

    # Skip sessions that have 0 minutes
      if session["minutes"] == 0:
        continue

    # Stop processing if a session reaches 100 minutes
    if session["minutes"] >= 100:
        break

    print(session["subject"], "-", session["minutes"], "minutes")
    
    
  #Part H – Stretch Challenges
#1. Print FizzBuzz from 1 to 100: multiples of 3 → Fizz, 5 → Buzz, both → FizzBuzz. 

for number in range(1, 101):

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)

#2.Given a sentence, count vowels without using .count() repeatedly.

sentence = input("Enter a sentence: ")

vowels = "aeiou"
vowel_count = 0

for character in sentence.lower():
    if character in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)

#3. Find all duplicate values in a list using loops and collections.

from collections import Counter

numbers = [1, 2, 3, 2, 4, 5, 3, 6, 7, 5, 8]

counts = Counter(numbers)

duplicates = []

for number in counts:
    if counts[number] > 1:
        duplicates.append(number)

print("Duplicate values:", duplicates)

#4. Build a simple text histogram: for each number in [3, 5, 2], print that many * characters.

numbers = [3, 5, 2]

for number in numbers:
    print("*" * number)
    

