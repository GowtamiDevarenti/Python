--Level 1
--Use webshop.db.
--Exercise 1
--Show products in Clothing or Accessories that cost between 150 and 500 kr. Most expensive first.
--Expected: 4 rows
----
SELECT *
FROM product
WHERE category IN ('Clothing', 'Accessories')
  AND price BETWEEN 150 AND 500
ORDER BY price DESC;

--Exercise 2
--Which orders were placed in February 2026 and are not cancelled?
--Expected: 4 rows
SELECT *
FROM Orders
WHERE OrderDate >= '2026-02-01'
  AND OrderDate < '2026-03-01'
  AND Status != 'Cancelled';


--Exercise 3
--Show every order line with the order_id, product name, quantity and line total (quantity times unit
--price). Only show lines where the line total is more than 500 kr. Biggest first.
--Expected: 11 rows

SELECT
    order_id,
    product_name,
    quantity,
    quantity * unit_price AS line_total
FROM OrderItems
JOIN Products
    ON OrderItems.product_id = Products.product_id
WHERE quantity * unit_price > 500
ORDER BY line_total DESC;
