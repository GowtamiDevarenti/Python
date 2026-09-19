# ==================================================
# TASK 1
# ==================================================

products = [
    {"name": "Laptop", "price": 12000, "stock": 4},
    {"name": "Mouse", "price": 350, "stock": 0},
    {"name": "Keyboard", "price": 800, "stock": 6},
    {"name": "Monitor", "price": 3200, "stock": 3},
    {"name": "Headset", "price": 950, "stock": 0},
    {"name": "Webcam", "price": 1100, "stock": 5}
]

# 1. Loop through the products.
# 2. Print the name of every product that is in stock.
# 3. Calculate the total value of all products in stock.
#    The value of a product is price * stock.
# 4. Print the total value.
# 5. Keep track of which in-stock product has the highest price
#    without using max(), and print its name.


# Write your solution below:

# 1. Loop through the products.

for product in products:
   print(product)
   
#2. Print the name of every product that is in stock.

for product in products:
   if product["stock"] > 0:
       print(f"In stock: {product['name']}")

# 3. Calculate the total value of all products in stock.
#    The value of a product is price * stock.
# 4. Print the total value.

total= 0

for product in products:
    if product["stock"] > 0:
        total = total + (product["price"] * product["stock"])

print(f"Total value of in-stock products: {total}")


# 5. Keep track of which in-stock product has the highest price
#    without using max(), and print its name.

highest_price = 0
highest_product = ""

for product in products:
    if product["stock"] > 0 and product["price"] > highest_price:
        highest_price = product["price"]
        highest_product = product["name"]
print(f"Highest priced in-stock product: {highest_product} at {highest_price}")




# ==================================================
# TASK 2
# ==================================================

scores = [78, 92, 55, 81, 67, 95, 73]

# Create a function called calculate_average that:
# - receives a list of scores
# - calculates and returns the average score
#
# Create another function called create_result that:
# - receives a list of scores
# - uses calculate_average()
# - returns "PASS" if the average is 70 or higher
# - otherwise returns "FAIL"
#
# Call create_result() using the scores above.
# Print both the average score and the final result.


# Write your solution below:

# Create a function called calculate_average that:
# - receives a list of scores
# - calculates and returns the average score

def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

print(f"Average score: {calculate_average(scores)}")

 #Create another function called create_result that:
# - receives a list of scores
# - uses calculate_average()
# - returns "PASS" if the average is 70 or higher
# - otherwise returns "FAIL"


def create_result(scores):
    average = calculate_average(scores)
    if average >= 70:
        return "PASS"
    else:
        return "FAIL"

result = create_result(scores)
print(f"Result: {result}")

# Call create_result() using the scores above.
# Print both the average score and the final result.

def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)
    return average
def create_result(scores):
    average = calculate_average(scores)
    if average >= 70:
        return "PASS"
    else:
        return "FAIL"
    
average_score = calculate_average(scores)
result = create_result(scores)
print(f"Average score: {average_score}")
print(f"Result: {result}")



# ==================================================
# TASK 3
# ==================================================

product_prices = [250, 400, 150, 700]

order_settings = {
    "discount": 10,
    "shipping": 49,
    "priority": True
}

# Create a function called calculate_order that:
# - receives a customer name as a normal parameter
# - receives any number of product prices using *args
# - receives optional settings using **kwargs
# - calculates the subtotal of all product prices
# - applies the discount percentage if "discount" exists
# - adds shipping if "shipping" exists
# - returns a dictionary containing:
#       customer
#       subtotal
#       final_total
#       settings
#
# Call the function using:
# - customer name "Anna"
# - the values from product_prices using unpacking
# - the values from order_settings using dictionary unpacking
#
# Print the returned dictionary.


# Write your solution below:

def calculate_order(customer, *args, **kwargs):
    subtotal = sum(args)


    if "discount" in kwargs:
        discount_amount = subtotal * kwargs["discount"] / 100
        subtotal = subtotal - discount_amount

    if "shipping" in kwargs:
        subtotal = subtotal + kwargs["shipping"]
        
    order = {
        "customer": customer,
        "subtotal": subtotal,
        "final_total": subtotal,
        "settings": kwargs
    }

    return  order
product_prices = [250, 400, 150, 700]
order_settings = {
    "discount": 10,
    "shipping": 49,
    "priority": True
}

order = calculate_order("Anna", *product_prices, **order_settings)
print(order)


# ==================================================
# TASK 4
# ==================================================

players = [
    {"name": "  anna", "score": 85, "active": True},
    {"name": "DAVID ", "score": 72, "active": False},
    {"name": " sara ", "score": 94, "active": True},
    {"name": "LEO", "score": 67, "active": True},
    {"name": " emma", "score": 88, "active": True},
    {"name": "OSCAR ", "score": 76, "active": False}
]

# 1. Create a new list containing normalized player names.
#    Remove unnecessary whitespace and use consistent capitalization.
#    Use a list comprehension.
#
# 2. Create a new list containing only the active players
#    with a score of 80 or higher.
#    Use a list comprehension.
#
# 3. Sort the original players by score from highest to lowest.
#    Use sorted() with a lambda.
#
# 4. Print the ranking in the following format:
#
#    1. Sara - 94
#    2. Emma - 88
#    ...
#
#    Generate the ranking numbers using enumerate().
#
# 5. Create a separate list containing the player names and
#    another list containing their scores.
#    Combine them using zip() and print each name together
#    with its score.


# Write your solution below:

# 1. Create a new list containing normalized player names.
#    Remove unnecessary whitespace and use consistent capitalization.
#    Use a list comprehension.

names_normalized = [player["name"].strip().capitalize() for player in players]
print("Normalized names:", names_normalized)

# 2. Create a new list containing only the active players
#    with a score of 80 or higher.
#    Use a list comprehension.

active_high_scorers = [player for player in players if player["active"] and player["score"] >= 80]
print("Active high scorers:", active_high_scorers)


# 3. Sort the original players by score from highest to lowest.
#    Use sorted() with a lambda.

sorted_players = sorted(players, key=lambda x: x["score"], reverse=True)
print("Sorted players by score:", sorted_players)


# 4. Print the ranking in the following format:
#
#    1. Sara - 94
#    2. Emma - 88
#    ...
#
#    Generate the ranking numbers using enumerate().


for i, player in enumerate(sorted_players, start=1):
    print(f"{i}. {player['name'].strip().capitalize()} - {player['score']}")
    
    
# 5. Create a separate list containing the player names and
#    another list containing their scores.
#    Combine them using zip() and print each name together
#    with its score.

name_list = [player["name"].strip().capitalize() for player in players]
score_list = [player["score"] for player in players]

for name, score in zip(name_list, score_list):
    print(f"{name} - {score}")
    
