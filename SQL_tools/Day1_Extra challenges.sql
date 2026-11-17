--Extra challenges: SELECT
--Level 1
--Exercise 1
--Show products that are not Accessories, are in stock, and have a space in their name. Sort by
--category, then by price from highest to lowest.
--Expected: 6 row
select * from products where category!='Accessories' and stock>0 and name like '% %' order by category, price desc;

--Exercise 2
--Show customers who live in a city starting with S or M, plus customers with no city at all.
--Expected: 5 rows
select * from customers where (city like 'S%' or city like 'M%') or city is null;


--Exercise 3
--Which Shoes product is the second most expensive? Show only that one.
--Expected: 1 row

select * from products where category='Shoes' order by price desc limit 1 offset 1; 

--Exercise 4
--Of the customers who joined in 2024 or 2025, show the 3 who joined most recently. Solve it
--without BETWEEN and without >=.
--Expected: 3 rows


SELECT *
FROM customers
WHERE YEAR(joined_date) IN (2024, 2025)
ORDER BY joined_date DESC
LIMIT 3;


--Level 2
--Use the SQLite documentation: sqlite.org/lang_corefunc.html
--Exercise 5
--Show each customer's full name in one column called full_name (like "Anna Lindqvist"), sorted by
--last name.
--Look up: ||   ·   Expected: 10 rows

SELECT first_name || ' ' || last_name AS full_name
FROM customers
ORDER BY last_name;

--Exercise 6
--Give every product a price level: budget under 200 kr, mid from 200 to 799 kr, premium from 800
--kr.
--Look up: CASE WHEN   ·   Expected: 12 rows: 4 budget, 5 mid, 3 premium

SELECT *,
       CASE
           WHEN price < 200 THEN 'budget'
           WHEN price < 800 THEN 'mid'
           ELSE 'premium'
       END AS price_level
FROM products;

--Exercise 7
--Show every customer's first name and city, but write Unknown instead of NULL.
--Look up: COALESCE   ·   Expected: 10 rows


SELECT first_name,
       COALESCE(city, 'Unknown') AS city
FROM customers;

--Exercise 8
--Which customers joined in the first half of a year (January to June), whatever the year?
--Look up: strftime   ·   Expected: 6 rows 

SELECT *
FROM customers
WHERE strftime('%m', joined_date) BETWEEN '01' AND '06';

--Exercise 9
--Which product has the longest name?
--Look up: LENGTH   ·   Expected: 1 row


SELECT *
FROM products
ORDER BY LENGTH(name) DESC
LIMIT 1;

--Exercise 10
--Show each customer's email username: the part before the @.
--Look up: substr and instr   ·   Expected: 10 rows

SELECT first_name,
       substr(email, 1, instr(email, '@') - 1) AS username
FROM customers;


--Level 3
--Exercise 11
--Which products cost more than the average price? Don't type the average yourself: let SQL
--calculate it inside the query.
--Expected: 5 rows

SELECT *
FROM products
WHERE price > (SELECT AVG(price) FROM products);


--Exercise 12
--Make a price list with one column that says, for example, "Socks 3-pack costs 129 kr". Only
--products in stock, cheapest first. Watch out: does it say 129 or 129.0? Fix it.
--Expected: 10 rows

SELECT name || ' costs ' ||
       CAST(price AS INTEGER) || ' kr' AS price_list
FROM products
WHERE stock > 0
ORDER BY price ASC;


--Exercise 13
--How many customers live in each city? Biggest city first.
--Look up: GROUP BY   ·   Expected: 6 rows

SELECT city, COUNT(*) AS customer_count
FROM customers
GROUP BY city
ORDER BY customer_count DESC;