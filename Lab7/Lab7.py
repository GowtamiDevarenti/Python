


""" Part A - Classes and objects
1. Create a Book class with title, author and pages. Create at least four Book objects and print their
attributes."""




"""2. Create a Laptop class with brand, model, ram_gb and price. Create three separate objects and
change the price of one object.
3. Create two objects with the same attribute values. Use is to check whether they are the same object.
4. Add a default value to at least one __init__ parameter.
5. Create one object using keyword arguments. """

# Part A - Classes and objects

class Book:
    def __init__(self, title, author, pages=100):
        self.title = title
        self.author = author
        self.pages = pages


# Creating four Book objects
book1 = Book("Harry Potter", "J.K. Rowling", 350)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book3 = Book("1984", "George Orwell", 280)
book4 = Book("The Alchemist", "Paulo Coelho", 208)

print(book1.title, book1.author, book1.pages)
print(book2.title, book2.author, book2.pages)
print(book3.title, book3.author, book3.pages)
print(book4.title, book4.author, book4.pages)



# Laptop class
class Laptop:
    def __init__(self, brand, model, ram_gb, price):
        self.brand = brand
        self.model = model
        self.ram_gb = ram_gb
        self.price = price


laptop1 = Laptop("Dell", "Inspiron", 8, 700)
laptop2 = Laptop("HP", "Pavilion", 16, 900)
laptop3 = Laptop("Apple", "MacBook Air", 16, 1200)

# Changing the price of one laptop
laptop1.price = 650

print(laptop1.brand, laptop1.model, laptop1.price)
print(laptop2.brand, laptop2.model, laptop2.price)
print(laptop3.brand, laptop3.model, laptop3.price)


# Two objects with the same values
book5 = Book("1984", "George Orwell", 280)
book6 = Book("1984", "George Orwell", 280)

# They have the same values, but they are different objects
print(book5 is book6)   # False


# Using keyword arguments
book7 = Book(title="Dune", author="Frank Herbert", pages=412)

print(book7.title)
print(book7.author)
print(book7.pages)


"""Part B - Methods and state
1. Extend your Book class with an is_long() method that returns True if the book has more than 300
pages.
2. Create a BankAccount class with owner and balance. Add a deposit() method that changes the
balance.
3. Add a withdraw() method. Prevent withdrawals that would make the balance negative by raising a
ValueError.
4. Create a Task class with title and completed=False. Add complete() and reopen() methods.
5. Create at least two objects from one of your classes and show that changing the state of one object
does not change the other."""


# Part B - Methods and state

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        return self.pages > 300


book1 = Book("Harry Potter", "J.K. Rowling", 350)
book2 = Book("1984", "George Orwell", 280)

print(book1.is_long())   # True
print(book2.is_long())   # False


# BankAccount class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("You do not have enough money.")
        self.balance -= amount


account = BankAccount("John", 500)

account.deposit(200)
print(account.balance)

account.withdraw(100)
print(account.balance)

# This would cause a ValueError
# account.withdraw(1000)


# Task class
class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def complete(self):
        self.completed = True

    def reopen(self):
        self.completed = False


task1 = Task("Finish Python lab")
task2 = Task("Read chapter 5")

task1.complete()

print(task1.title, task1.completed)
print(task2.title, task2.completed)


# Changing one object does not change the other
task2.complete()

print(task1.completed)
print(task2.completed)


"""Part C - Instance and class attributes
1. Create a Product class with name and price as instance attributes.
2. Add a class attribute called tax_rate that is shared by all Product objects.
3. Add a price_with_tax() method that returns the price including tax.
4. Create at least three Product objects and print their prices with tax.
5. Change Product.tax_rate and show how it affects the Product objects.
6. Give one Product object its own tax_rate. Print the tax rate from that object, another Product object and
the Product class"""

# Part C - Instance and class attributes

class Product:
    # This is shared by all Product objects
    tax_rate = 0.20

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return self.price + (self.price * Product.tax_rate)


# Creating three products
product1 = Product("Laptop", 1000)
product2 = Product("Phone", 700)
product3 = Product("Headphones", 100)

print(product1.price_with_tax())
print(product2.price_with_tax())
print(product3.price_with_tax())


# Changing the shared tax rate
Product.tax_rate = 0.25

print(product1.price_with_tax())
print(product2.price_with_tax())
print(product3.price_with_tax())


# Give only product1 its own tax rate
product1.tax_rate = 0.10

print("Product 1 tax:", product1.tax_rate)
print("Product 2 tax:", product2.tax_rate)
print("Class tax:", Product.tax_rate)


"""Part D - Collections of objects
1. Create at least six Student objects with name and score.
2. Store all Student objects in a list.
3. Loop through the list and print each student's name and score.
4. Add a get_status() method that returns "PASS" or "FAIL" based on the score.
5. Loop through the students again and print each student's name and status.
6. Use a list comprehension to create a new list containing only students with a score of 70 or higher.
"""

# Part D - Collections of objects

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        if self.score >= 70:
            return "PASS"
        else:
            return "FAIL"


# Creating six students
student1 = Student("Alice", 85)
student2 = Student("Bob", 65)
student3 = Student("Charlie", 72)
student4 = Student("David", 55)
student5 = Student("Emma", 91)
student6 = Student("Frank", 68)


# Put all students into a list
students = [
    student1,
    student2,
    student3,
    student4,
    student5,
    student6
]


# Print each student's name and score
for student in students:
    print(student.name, student.score)


print("\nStudent results:")

# Print each student's name and status
for student in students:
    print(student.name, student.get_status())


# List comprehension
passed_students = [
    student for student in students
    if student.score >= 70
]

print("\nStudents who scored 70 or higher:")

for student in passed_students:
    print(student.name)
    

#The list comprehension:

passed_students = [
    student for student in students
    if student.score >= 70
]



"""Part E - Objects inside objects
1. Create a Teacher class with a name.
2. Create a Course class with a course name and a teacher. The teacher should be a Teacher object.
3. Create a Teacher object and use it when creating a Course object.
4. Print the course name and the teacher's name through the Course object.
5. Extend Course so that it also contains an initially empty list of Student objects.
6. Add an add_student() method and use it to add at least three Student objects to the course.
7. Loop through course.students and print the name of every student"""

# Part E - Objects inside objects

class Teacher:
    def __init__(self, name):
        self.name = name


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)


# Create a teacher
teacher1 = Teacher("Mr. Smith")

# Use the Teacher object when creating the course
course1 = Course("Python Programming", teacher1)

print("Course:", course1.name)
print("Teacher:", course1.teacher.name)


# Create students
student1 = Student("Alice", 85)
student2 = Student("Bob", 72)
student3 = Student("Charlie", 90)


# Add students to the course
course1.add_student(student1)
course1.add_student(student2)
course1.add_student(student3)


# Print all students in the course
print("\nStudents in the course:")

for student in course1.students:
    print(student.name)
    
#The important part is:

#course1.teacher.name' - course1 contains a Teacher object, so we can access the teacher's name through the course.


"""Part F - Applied challenge: Course manager
1. Build a small course management program using Student, Teacher and Course classes.
2. Student should contain at least name and score.
3. Student should have a method that returns "PASS" or "FAIL".
4. Teacher should contain at least a name.
5. Course should contain a name, a Teacher object and a list of Student objects.
6. Add methods for adding a student and showing how many students are currently in the course.
7. Add a method that returns a list containing only the students who passed.
8. Add validation somewhere in your program using ValueError. Choose a validation that makes sense.
9. Create at least five Student objects, one Teacher object and one Course object. Demonstrate that your
methods work.
10. Print a simple course summary containing the course name, teacher name, number of students and
the names of the students who passed"""


# Part F - Course Manager


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        if self.score >= 70:
            return "PASS"
        else:
            return "FAIL"


class Teacher:
    def __init__(self, name):
        self.name = name


class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        # Make sure the score is valid
        if student.score < 0 or student.score > 100:
            raise ValueError("Score must be between 0 and 100.")

        self.students.append(student)

    def number_of_students(self):
        return len(self.students)

    def get_passed_students(self):
        return [
            student for student in self.students
            if student.get_status() == "PASS"
        ]

    def show_students_above(self, score):
        return [
            student for student in self.students
            if student.score > score
        ]


# Create a teacher
teacher1 = Teacher("Mr. Smith")


# Create a course
course1 = Course("Python Programming", teacher1)


# Create five students
student1 = Student("Alice", 85)
student2 = Student("Bob", 65)
student3 = Student("Charlie", 92)
student4 = Student("David", 58)
student5 = Student("Emma", 76)


# Add students to the course
course1.add_student(student1)
course1.add_student(student2)
course1.add_student(student3)
course1.add_student(student4)
course1.add_student(student5)


# Number of students
print("Number of students:", course1.number_of_students())


# Find students who passed
passed_students = course1.get_passed_students()

print("\nStudents who passed:")

for student in passed_students:
    print(student.name)


# Find students above a certain score
print("\nStudents with score above 80:")

high_scores = course1.show_students_above(80)

for student in high_scores:
    print(student.name, student.score)


# Simple course summary
print("\n--- Course Summary ---")
print("Course:", course1.name)
print("Teacher:", course1.teacher.name)
print("Number of students:", course1.number_of_students())

print("Passed students:")

for student in course1.get_passed_students():
    print("-", student.name)
    

"""Part G - Stretch challenges
1. Add a method that updates a student's score with validation.
2. Add a method to Course that finds students above a score threshold.
3. Create another Course object and show that its student list is separate from the first course.
4. Add one useful class attribute to Student, Teacher or Course and explain in a comment why it belongs
to the class rather than an individual object"""


# Part G - Stretch challenges


class Student:

    # This belongs to the whole Student class,
    # because the pass mark is the same for every student.
    PASS_MARK = 70

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        if self.score >= Student.PASS_MARK:
            return "PASS"
        else:
            return "FAIL"

    def update_score(self, new_score):
        # Score must be between 0 and 100
        if new_score < 0 or new_score > 100:
            raise ValueError("Score must be between 0 and 100.")

        self.score = new_score


class Teacher:
    def __init__(self, name):
        self.name = name


class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

        # Each course gets its own empty student list
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def number_of_students(self):
        return len(self.students)

    def get_passed_students(self):
        return [
            student for student in self.students
            if student.get_status() == "PASS"
        ]

    def find_students_above(self, threshold):
        return [
            student for student in self.students
            if student.score > threshold
        ]


# Create a teacher
teacher1 = Teacher("Mr. Smith")

# Create the first course
course1 = Course("Python Programming", teacher1)


# Create students
student1 = Student("Alice", 65)
student2 = Student("Bob", 80)
student3 = Student("Charlie", 92)
student4 = Student("David", 55)
student5 = Student("Emma", 75)


# Add students to first course
course1.add_student(student1)
course1.add_student(student2)
course1.add_student(student3)
course1.add_student(student4)
course1.add_student(student5)


# Update a student's score
student1.update_score(72)

print(student1.name, student1.score, student1.get_status())


# Find students above 80
print("\nStudents above 80:")

students_above_80 = course1.find_students_above(80)

for student in students_above_80:
    print(student.name, student.score)


# Create another course
teacher2 = Teacher("Mrs. Brown")
course2 = Course("Web Development", teacher2)

student6 = Student("Frank", 88)

course2.add_student(student6)


# Show that the two courses have separate student lists
print("\nCourse 1 students:", course1.number_of_students())
print("Course 2 students:", course2.number_of_students())


# Show passed students
print("\nStudents who passed Python Programming:")

for student in course1.get_passed_students():
    print(student.name)