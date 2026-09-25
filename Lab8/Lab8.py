"""Part A - Mutable default arguments
1. Create a BadTeam class with name and a default parameter members=[]. Add an add_member()
method.
2. Create two BadTeam objects without providing a members list. Add a member to only one team and
print both lists. Explain in a comment what happened.
3. Create a corrected Team class using None as the default value and create a new list inside __init__.
4. Repeat the test with two Team objects and show that each object now has its own list."""

# Part A - Mutable Default Arguments

# This class has a BAD default value.
class BadTeam:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add_member(self, member):
        self.members.append(member)


# We create two teams without giving them a members list.
team1 = BadTeam("Team A")
team2 = BadTeam("Team B")

# We only add a member to team1.
team1.add_member("Alice")

print(team1.members)
print(team2.members)

# What happened?
# Both teams show Alice!
# This is because the default list [] is created only once.
# team1 and team2 are therefore using the SAME list.

#Corrected version

# Correct way: use None as the default value.

class Team:
    def __init__(self, name, members=None):
        self.name = name

        # A new list is created for every object.
        if members is None:
            self.members = []
        else:
            self.members = members

    def add_member(self, member):
        self.members.append(member)


# Create two new teams.
team1 = Team("Team A")
team2 = Team("Team B")

# Add a member only to team1.
team1.add_member("Alice")

print(team1.members)
print(team2.members)

# Now team1 contains Alice, but team2 is empty.
# Each Team object has its own separate list.


"""Part B - Dictionary or class?
1. Represent a movie using a dictionary with title, director and rating.
2. Represent the same information using a Movie class.
3. Add a method to Movie that returns whether the movie is highly rated. Choose a sensible rating
threshold.
4. In comments, briefly explain one situation where you would choose a dictionary and one where you
would choose a class."""


#Using a dictionary

# Part B - Dictionary

# A dictionary is a simple way to store information about a movie.
movie_dict = {
    "title": "The Lion King",
    "director": "Roger Allers",
    "rating": 8.5
}

print(movie_dict)
print(movie_dict["title"])
print(movie_dict["rating"])

# A dictionary is useful when we mainly need to store simple data.
# For example, a dictionary is good for temporary data or simple records.


#Using a class

# The same movie can also be represented using a class.

class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def is_highly_rated(self):
        # We decide that 8.0 or higher is highly rated.
        return self.rating >= 8.0


movie = Movie("The Lion King", "Roger Allers", 8.5)

print(movie.title)
print(movie.director)
print(movie.rating)

print(movie.is_highly_rated())

# A class is useful when we have both data AND behaviour.
# For example, Movie has information about a movie,
# but it also has the is_highly_rated() method.

"""Part C - Inheritance fundamentals
1. Create a base class Account with owner and balance.
2. Create SavingsAccount(Account) with an additional interest_rate attribute.
3. Use super() so SavingsAccount reuses the initialization from Account.
4. Create at least two objects and print their attributes.
5. Write the "is-a" statement that explains why this inheritance relationship makes sense."""



# Part C - Inheritance Fundamentals

# This is the base class.
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


# SavingsAccount inherits from Account.
class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        # super() calls the __init__ method from Account.
        super().__init__(owner, balance)

        # This is extra information only for SavingsAccount.
        self.interest_rate = interest_rate


# Create two savings accounts.
account1 = SavingsAccount("Alice", 1000, 0.05)
account2 = SavingsAccount("Bob", 2000, 0.03)

print(account1.owner)
print(account1.balance)
print(account1.interest_rate)

print(account2.owner)
print(account2.balance)
print(account2.interest_rate)


# IS-A relationship:
# A SavingsAccount IS-A Account.
#
# This makes sense because a savings account is a type of account.


"""Part D - Inherited and subclass-specific behaviour
1. Create a base class Employee with name and a method get_information().
2. Create Developer(Employee) and add a method that only Developer has.
3. Create another Employee subclass of your choice and give it its own subclass-specific method.
4. Demonstrate that both subclasses can use inherited behaviour from Employee.
5. Demonstrate that an Employee object cannot automatically use a method that only exists in one of its
subclasses"""


# Part D - Inherited and Subclass-Specific Behaviour

# Base class
class Employee:
    def __init__(self, name):
        self.name = name

    def get_information(self):
        return f"Employee name: {self.name}"


# Developer inherits from Employee.
class Developer(Employee):

    def write_code(self):
        return f"{self.name} is writing code."


# Another Employee subclass.
class Designer(Employee):

    def design(self):
        return f"{self.name} is designing a website."


# Create objects.
developer = Developer("Alice")
designer = Designer("Bob")

# Both objects can use get_information()
# because they inherited it from Employee.
print(developer.get_information())
print(designer.get_information())

# These methods only belong to their own subclasses.
print(developer.write_code())
print(designer.design())


# An Employee object can use get_information().
employee = Employee("Charlie")

print(employee.get_information())

# But Employee does NOT automatically have write_code().
# The write_code() method belongs only to Developer.
#
# So this would cause an error:
# employee.write_code()
#
# An Employee is not automatically a Developer.


"""Part E - super() and shared initialization
1. Create a base class Device with brand and year.
2. Add useful shared initialization logic inside Device, for example validation that year cannot be negative
and an attribute such as is_active=True.
3. Create Laptop(Device) with one additional attribute such as ram_gb. Use super().
4. Create another Device subclass with its own additional attribute and use super() again.
5. Demonstrate that both subclasses receive the shared initialization logic from Device without duplicating
it."""

# Part E - super() and Shared Initialization

# Base class
class Device:
    def __init__(self, brand, year):
        # Check that the year is not negative.
        if year < 0:
            raise ValueError("Year cannot be negative.")

        self.brand = brand
        self.year = year

        # Every device starts as active.
        self.is_active = True


# Laptop inherits from Device.
class Laptop(Device):
    def __init__(self, brand, year, ram_gb):
        # Reuse the initialization from Device.
        super().__init__(brand, year)

        # Extra information for laptops.
        self.ram_gb = ram_gb


# Phone also inherits from Device.
class Phone(Device):
    def __init__(self, brand, year, storage_gb):
        # Reuse the initialization from Device.
        super().__init__(brand, year)

        # Extra information for phones.
        self.storage_gb = storage_gb


# Create a laptop.
laptop = Laptop("Dell", 2024, 16)

# Create a phone.
phone = Phone("Samsung", 2025, 256)

print(laptop.brand)
print(laptop.year)
print(laptop.ram_gb)
print(laptop.is_active)

print(phone.brand)
print(phone.year)
print(phone.storage_gb)
print(phone.is_active)


# Both Laptop and Phone get brand, year and is_active
# from Device.
#
# We do not have to write the same code twice.
# super() allows both subclasses to reuse Device's __init__ method.

"""Part F - Method overriding
1. Create a base class Notification with a method send() that returns a general message.
2. Create EmailNotification(Notification) and SMSNotification(Notification).
3. Override send() in both subclasses so each returns a different message.
4. Create one object from each class and call send() on all of them.
5. Explain in a comment which method is used when send() is called on each object"""

# Part F - Method Overriding

# Base class
class Notification:
    def send(self):
        return "Sending a general notification."


# EmailNotification changes the send() method.
class EmailNotification(Notification):
    def send(self):
        return "Sending an email notification."


# SMSNotification also changes the send() method.
class SMSNotification(Notification):
    def send(self):
        return "Sending an SMS notification."


# Create objects.
general = Notification()
email = EmailNotification()
sms = SMSNotification()

print(general.send())
print(email.send())
print(sms.send())


# When general.send() is called:
# Python uses the send() method from Notification.
#
# When email.send() is called:
# Python uses the overridden send() method from EmailNotification.
#
# When sms.send() is called:
# Python uses the overridden send() method from SMSNotification.


"""Part G - Override and still use the base method
1. Create a base class Report with a method get_summary() that returns a general report summary.
2. Create SalesReport(Report) and override get_summary().
3. Inside the overridden method, call the base implementation using super() and add SalesReport-specific
information.
4. Create a SalesReport object and print the final result."""

# Part G - Override and still use the base method

# Base class
class Report:
    def get_summary(self):
        return "This is a general report."


# SalesReport inherits from Report.
class SalesReport(Report):

    # We override get_summary().
    def get_summary(self):
        # First, get the message from the parent class.
        general_summary = super().get_summary()

        # Then add information specific to sales.
        return general_summary + " This report contains sales information."


# Create a SalesReport object.
report = SalesReport()

print(report.get_summary())


# super().get_summary() allows us to use the original
# method from Report instead of completely replacing it.


"""Part H - Applied challenge: User accounts
1. Build a small user account system using inheritance.
2. Create a base class User with at least username and email.
3. Add a useful method to User that all user types should inherit.
4. Create AdminUser(User) and PremiumUser(User). Give each subclass at least one additional
attribute and one subclass-specific method.
5. Use super() in both subclasses instead of duplicating User's initialization.
6. Add one method to User and override it differently in AdminUser and PremiumUser.
7. In one overridden method, use super() to reuse the base implementation and then extend it.
8. Create several objects and demonstrate inherited methods, subclass-specific methods and overridden
methods.
9. Add at least one sensible validation using ValueError.
10. In comments, explain why AdminUser and PremiumUser have an "is-a" relationship with User"""



# Part H - User Account System

# --------------------------------------------------
# Base User class
# --------------------------------------------------

class User:
    def __init__(self, username, email):
        # Simple validation.
        if username == "":
            raise ValueError("Username cannot be empty.")

        if "@" not in email:
            raise ValueError("Email must contain @.")

        self.username = username
        self.email = email

    # This method can be used by all types of users.
    def get_information(self):
        return f"Username: {self.username}, Email: {self.email}"

    # This method can be changed by subclasses.
    def describe_account(self):
        return f"{self.username} has a normal user account."


# --------------------------------------------------
# AdminUser class
# --------------------------------------------------

class AdminUser(User):

    def __init__(self, username, email, admin_level):
        # Use User's initialization.
        super().__init__(username, email)

        # Extra information for an admin.
        self.admin_level = admin_level

    # Method only AdminUser has.
    def manage_users(self):
        return f"{self.username} can manage other users."

    # Override the method from User.
    def describe_account(self):
        # Use the original User method first.
        basic_description = super().describe_account()

        # Add extra admin information.
        return basic_description + f" {self.username} is also an admin."


# --------------------------------------------------
# PremiumUser class
# --------------------------------------------------

class PremiumUser(User):

    def __init__(self, username, email, subscription):
        # Use User's initialization.
        super().__init__(username, email)

        # Extra information for premium users.
        self.subscription = subscription

    # Method only PremiumUser has.
    def use_premium_feature(self):
        return f"{self.username} is using a premium feature."

    # Override the method from User.
    def describe_account(self):
        return f"{self.username} has a premium {self.subscription} subscription."


# --------------------------------------------------
# Create some users
# --------------------------------------------------

normal_user = User("Charlie", "charlie@example.com")

admin = AdminUser(
    "Alice",
    "alice@example.com",
    "High"
)

premium = PremiumUser(
    "Bob",
    "bob@example.com",
    "Monthly"
)


# --------------------------------------------------
# Inherited method
# --------------------------------------------------

print(normal_user.get_information())
print(admin.get_information())
print(premium.get_information())

# All three objects can use get_information()
# because it comes from the User class.


# --------------------------------------------------
# Subclass-specific methods
# --------------------------------------------------

print(admin.manage_users())

print(premium.use_premium_feature())

# manage_users() only belongs to AdminUser.
# use_premium_feature() only belongs to PremiumUser.


# --------------------------------------------------
# Overridden methods
# --------------------------------------------------

print(normal_user.describe_account())
print(admin.describe_account())
print(premium.describe_account())

# The normal User uses User's version.
# AdminUser uses its own overridden version.
# PremiumUser uses its own overridden version.


# --------------------------------------------------
# Validation example
# --------------------------------------------------

# The following would cause a ValueError because
# the username is empty:
#
# bad_user = User("", "test@example.com")


# This would also cause a ValueError because
# the email does not contain @:
#
# bad_user = User("David", "wrongemail")


# --------------------------------------------------
# IS-A relationships
# --------------------------------------------------

# AdminUser IS-A User.
# An admin is a type of user, so it makes sense
# for AdminUser to inherit from User.
#
# PremiumUser IS-A User.
# A premium user is also a type of user, so it makes sense
# for PremiumUser to inherit from User.




