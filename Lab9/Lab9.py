#Part A - Polymorphism
#1.Create three classes: EmailNotification, 
# SMSNotification and PushNotification

class EmailNotification:
    pass

class SMSNotification:
    pass

class PushNotification:
    pass

#A class is like a blueprint. Here we make three blueprints. p
# pass just means "nothing inside yet". We will add the send() method in the next step.


#2. Give all three classes a method called send(), but make each method return a different message. 

class EmailNotification:
    def send(self):
        return "Sending an Email notification"

class SMSNotification:
    def send(self):
        return "Sending an SMS notification"

class PushNotification:
    def send(self):
        return "Sending a Push notification"
    
#All three classes have a method with the same name, send(), but each one returns a different message.
# self refers to the object that calls the method.

#3: Create one object from each class and store them in a list
email = EmailNotification()
sms = SMSNotification()
push = PushNotification()

notifications = [email, sms, push]

#We build one object from each class, then put all three into a single list called notifications. Python lists can hold objects of different classes together.

#4: Loop through the list and call send()
for notification in notifications:
    print(notification.send())
    
#5. In a comment, explain why the loop does not need to know the exact class of each object
# The loop does not need to know the exact class of each object because
# every object in the list has a method called send(). Python only cares
# that the method exists, not which class the object comes from. Each object
# runs its own version of send(), so we get a different message each time.
# This idea is called polymorphism ("many forms").

#Part B - Polymorphism with inheritance

#1. Create a base class Document with a title attribute and a method describe()

class Document:
    def __init__(self, title):
        self.title = title

    def describe(self):
        return "This is a generic document."
    

#2. Create PDFDocument(Document) and TextDocument(Document).

class PDFDocument(Document):
    pass

class TextDocument(Document):
    pass

# 3. Override describe() in both subclasses so they return different descriptions.

class PDFDocument(Document):
    def describe(self):
        return "A PDF file with fixed layout, ideal for sharing and printing."

class TextDocument(Document):
    def describe(self):
        return "A plain text file containing simple, unformatted content."
    
#4. Create several PDFDocument and TextDocument objects and store them in one list.

documents = [
    PDFDocument("Annual Report"),
    TextDocument("Meeting Notes"),
    PDFDocument("Invoice #1042"),
    TextDocument("Shopping List"),
]


#5.Loop through the list and print each document's title and the result of describe().

for doc in documents:
    print(f"{doc.title}: {doc.describe()}")
    
    
#Part C - Duck typing
#1. Create two unrelated classes, for example Printer and Screen. Do not use inheritance between them.
class Printer:
    def __init__(self, name):
        self.name = name


class Screen:
    def __init__(self, name):
        self.name = name

#2. Give both classes a method called display_status().

class Printer:
    def __init__(self, name):
        self.name = name

    def display_status(self):
        print(f"Printer '{self.name}': online, paper tray full, ready to print.")


class Screen:
    def __init__(self, name):
        self.name = name

    def display_status(self):
        print(f"Screen '{self.name}': powered on, brightness 80%, resolution 1920x1080.")

#3. Create objects from both classes and store them in the same list.

devices = [
    Printer("Office Laser"),
    Screen("Main Monitor"),
    Printer("Photo Printer"),
    Screen("Reception Display"),
]

#4. Loop through the list and call display_status() on each object.

for device in devices:
    device.display_status()
    
#5. In a comment, explain why this works even though the classes do not share a base class. 

# This works because Python uses duck typing: it cares about what an object
# can DO, not what class it belongs to. "If it walks like a duck and quacks
# like a duck, it's a duck." Both Printer and Screen have a method named
# display_status(), so the call device.display_status() succeeds for either
# one. Python looks up the method on the object at runtime, so no shared base
# class or interface is needed.


#Part D: isinstance()
#1. Create a base class User and a subclass AdminUser(User).

class User:
    def __init__(self, name):
        self.name = name


class AdminUser(User):
    pass

#2. Create an AdminUser object.
admin = AdminUser("Sara")

#3.se isinstance() to check whether the object is an AdminUser, a User and a string.

is_admin = isinstance(admin, AdminUser)
is_user = isinstance(admin, User)
is_string = isinstance(admin, str)

#4. Print all three results.
print("Is AdminUser?", is_admin)
print("Is User?", is_user)
print("Is string?", is_string)

#5. In a comment, explain why the AdminUser object is also considered an instance of User.
#    Inheritance models an IS-A relationship: every AdminUser IS-A User,
#    so isinstance() returns True for the subclass and for its parent class.

#Part E: __str__

#1. Create a Product class with name and price.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price:.2f}"
    
#2. Create one Product object and print it before defining __str__. Observe the result.

product = Product("Laptop", 999.99)
print(product)

#3.Add __str__ so printing the Product gives a useful human-readable description.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"
    
#4. Create at least three Product objects and print them.
product1 = Product("Laptop", 999.99)
product2 = Product("Mouse", 29.99)
product3 = Product("Keyboard", 79.99)

print(product1)
print(product2)
print(product3)                                                                         

#5. Use str() on one Product object, store the result in a variable and print its type.
product_str = str(product1) 
print(product_str)
print(type(product_str))  # This will show that product_str is of type 'str'

#Part F: __str__ with inheritance
#1. Create a base class Account with owner and balance. & 2. Add __str__ to Account.
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner}, balance: ${self.balance:.2f}"
    
    #3.3. Create SavingsAccount(Account) with an additional interest_rate attribute.
    # Use super() in __init__.
    
class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    #4. Override __str__ in SavingsAccount to include the interest rate.
    def __str__(self):
        return f"Savings Account owner: {self.owner}, balance: ${self.balance:.2f}, interest rate: {self.interest_rate}%"
    
    #5.Create and print both an Account and a SavingsAccount object
    
    
normal = Account("Amar", 1200)
savings = SavingsAccount("Gowtami", 5000, 2.5)

print(normal)
print(savings)