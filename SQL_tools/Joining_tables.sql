
-- Exercises: Joining Tables
-- Database: webshop.db
--
-- Before starting, check if the orders table contains 15 orders.
-- If the result is not 15, run webshop_reset.sql and press Ctrl+S.

SELECT COUNT(*) FROM orders;


-- Exercise 1
-- Show each order along with the customer's first name,
-- last name, and order status.
-- Expected: 15 rows

SELECT
    customers.first_name,
    customers.last_name,
    orders.status
FROM orders
INNER JOIN customers
    ON orders.customer_id = customers.customer_id;


-- Exercise 2
-- Find all orders placed by customers named Simon.
-- Expected: 3 rows

SELECT
    customers.first_name,
    customers.last_name,
    orders.order_id,
    orders.status
FROM orders
INNER JOIN customers
    ON orders.customer_id = customers.customer_id
WHERE LOWER(customers.first_name) = 'simon';


-- Exercise 3
-- Show all orders placed by customers living in Stockholm.
-- Display the newest orders first.
-- Expected: 3 rows

SELECT
    customers.customer_id,
    customers.first_name,
    customers.city,
    orders.order_id,
    orders.order_date
FROM orders
INNER JOIN customers
    ON orders.customer_id = customers.customer_id
WHERE LOWER(customers.city) = 'stockholm'
ORDER BY orders.order_date DESC;


-- Exercise 4
-- List every order item with its product name and category.
-- Expected: 23 rows

SELECT
    order_items.order_id,
    order_items.product_id,
    products.name,
    products.category
FROM order_items
INNER JOIN products
    ON order_items.product_id = products.product_id;


-- Exercise 5
-- Find all orders that included shoes.
-- Show the order ID, product ID, product name, and category.
-- Expected: 4 rows

SELECT
    order_items.order_id,
    order_items.product_id,
    products.name,
    products.category
FROM order_items
INNER JOIN products
    ON order_items.product_id = products.product_id
WHERE LOWER(products.category) = 'shoes';


-- Exercise 6
-- Show the complete receipt for order number 10.
-- Include the product name, quantity, unit price,
-- and total price for each item.
-- Expected: 2 rows

SELECT
    order_items.order_id,
    products.name,
    order_items.quantity,
    order_items.unit_price,
    order_items.quantity * order_items.unit_price AS line_total
FROM products
INNER JOIN order_items
    ON products.product_id = order_items.product_id
WHERE order_items.order_id = 10;


-- Exercise 7
-- Find customers who bought a black hoodie.
-- Show their first name, order date, and product name.
-- Expected: 3 rows

SELECT
    customers.first_name,
    orders.order_date,
    products.name
FROM customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id
INNER JOIN order_items
    ON order_items.order_id = orders.order_id
INNER JOIN products
    ON products.product_id = order_items.product_id
WHERE LOWER(products.name) = 'hoodie black';


-- Exercise 8
-- Show every customer and their orders.
-- Include customers who have not placed any orders.
-- Expected: 17 rows

SELECT
    customers.first_name,
    customers.last_name,
    orders.order_id,
    orders.status
FROM customers
LEFT JOIN orders
    ON customers.customer_id = orders.customer_id;


-- Exercise 9
-- Find products that have never been sold.
-- Show their product ID and name.
-- Expected: 2 rows

SELECT
    products.product_id,
    products.name
FROM products
LEFT JOIN order_items
    ON products.product_id = order_items.product_id
WHERE order_items.order_id IS NULL;


-- Exercise 10: Challenge
-- Find all products purchased by customers from Uppsala.
-- Show the customer's first name, product name, and quantity.
-- This query joins several tables to connect customers,
-- their orders, and the products they purchased.
-- Expected: 8 rows

SELECT
    customers.first_name,
    products.name,
    order_items.quantity
FROM customers
INNER JOIN orders
    ON customers.customer_id = orders.customer_id
INNER JOIN order_items
    ON orders.order_id = order_items.order_id
INNER JOIN products
    ON order_items.product_id = products.product_id
WHERE customers.city = 'Uppsala';
