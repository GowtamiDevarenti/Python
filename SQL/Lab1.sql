--Exercise 1: SQL Queries
-- Question 1
SELECT first_name, email
FROM customers;


-- Question 2
SELECT *FROM products
WHERE category = 'Shoes';


-- Question 3
SELECT *FROM customers
WHERE city = 'Uppsala';


-- Question 4
SELECT *FROM products
WHERE price = 199;


-- Question 5
SELECT *FROM products
ORDER BY name ASC;


-- Question 6

SELECT *FROM customers

ORDER BY join_date ASC;

-- Question 7
SELECT *FROM products
WHERE stock = 0;


-- Question 8
SELECT *FROM customers

ORDER BY join_date DESC

LIMIT 3;

-- Question 9
SELECT *FROM customers
WHERE city IN ('Stockholm', 'Göteborg');


-- Question 10
SELECT name AS product, price AS price_sek
FROM products;

--Bonus 1 — Clothing or Shoes AND price &gt; 1000
SELECT *
FROM products
WHERE (category = 'Clothing' OR category = 'Shoes')
  AND price &gt; 1000;
  
 --Bonus 2 — Calculate total stock value

 
SELECT name,

       price,

       stock,

       price * stock AS stock_value

FROM products

WHERE stock &gt; 0

ORDER BY stock_value DESC;
	 

--Bonus 3. Customers whose first name has exactly 4 letters (4 rows)



SELECT *

FROM customers

WHERE first_name LIKE '____';



--Bonus 4. Products ranked 6 to 10 by price, cheapest first (5 rows)



SELECT *

FROM products

ORDER BY price ASC

LIMIT 5 OFFSET 5;



--Bonus 5. Customers who joined before 2025 and don't live in Uppsala (4 rows)



SELECT *

FROM customers

WHERE join_date &lt; '2025-01-01'

  AND city &lt;&gt; 'Uppsala'


ORDER BY city ASC, last_name ASC;








