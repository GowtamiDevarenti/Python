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
