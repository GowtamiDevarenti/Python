--Day 2: Exercises
--Exercise 1


--Create a table books with: book_id (primary key), title (must have a value), author, year (whole
--number)


CREATE TABLE books (book_id INTEGER PRIMARY KEY,title TEXT NOT NULL,author TEXT,year INTEGER);


--Add a rule to books so year must be greater than 1400. (Hint: DROP and CREATE again.

DROP TABLE books;


CREATE TABLE books (book_id INTEGER PRIMARY KEY,title TEXT NOT NULL,author TEXT, year INTEGER CHECK(year > 1400 ));



--Add a column isbn to books. It should be TEXT.

ALTER TABLE books ADD COLUMN isbn TEXT ;


--Delete the books table.


DROP TABLE books;

--Create a table reviews: review_id, product_id (points to products), rating (1 to 5), comment.

CREATE TABLE reviews (review_id INTEGER PRIMARY KEY,product_id INTEGER,rating INTEGER CHECK (rating BETWEEN 1 AND 5),comment TEXT,FOREIGN KEY (product_id) REFERENCES products(product_id));

--Test reviews: try to add a review with rating 6. What happens?

INSERT INTO reviews (review_id, product_id, rating, comment)
VALUES (1, 1, 6, 'Good product');


--Test reviews: try to add a review for product 50. What happens?

--SQLite gives an error if product 50 does not exist in the products table and foreign key enforcement is enabled.
