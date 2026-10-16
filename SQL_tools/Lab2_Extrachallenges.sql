--Extra challenges: building tables
--Level 1
--Exercise 1
--Create a table suppliers with supplier_id (primary key), name (must have a value and must be
--unique), country (Sweden if nothing is given) and email.
--Expected: Runs without errors


CREATE TABLE suppliers (supplier_id INTEGER PRIMARY KEY,name TEXT NOT NULL UNIQUE,country TEXT DEFAULT 'Sweden',email TEXT);



--Add a supplier without giving a country. Then show all suppliers. What does the country column say?
--Expected: 1 row, country is Sweden

----
INSERT INTO suppliers (name, email)
VALUES ('Mayookha Textiles', 'info@mayookhatextiles.com');

SELECT * FROM suppliers;

--Try to add a second supplier with the same name, Nordic Textiles. What happens, and which rule stopped you?  Expected: An error

INSERT INTO suppliers (name, email)
VALUES ('Nordic Textiles', 'sales@nordictextiles.com');


--Create a table coupons where the code itself (for example 'SUMMER20') is the primary key.discount_percent must be between 1 and 90, and valid_until must have a value. Then try to add a
--coupon with 95 percent off.
--Expected: The table is created, the INSERT gives an error

CREATE TABLE coupons (
    code TEXT PRIMARY KEY,
    discount_percent INTEGER CHECK (discount_percent BETWEEN 1 AND 90),
    valid_until TEXT NOT NULL
);

INSERT INTO coupons (code, discount_percent, valid_until)
VALUES ('SUMMER95', 95, '2026-12-31');



--Level 2
--Use the SQLite documentation: sqlite.org/lang_createtable.html and sqlite.org/lang_altertable.html
--Add a supplier without giving a supplier_id. Which id does it get? Why?
--Look up: INTEGER PRIMARY KEY · Expected: 1 new row

INSERT INTO suppliers (name, country, email)
VALUES ('Stockholm Books', 'Sweden', 'info@stockholmbooks.com');

SELECT * FROM suppliers;

--Rename the column email in suppliers to contact_email.
--Look up: ALTER TABLE ... RENAME COLUMN · Expected: Runs without errors

ALTER TABLE suppliers
RENAME COLUMN email TO contact_email;


--Show the columns of the products table using SQL, not the Database Structure tab.
--Look up: PRAGMA table_info · Expected: 5 rows, one per column

PRAGMA table_info(products);


--A product can come from many suppliers, and a supplier can deliver many products. Create the
--middle table product_suppliers with a purchase price that must be more than 0. The same pair
--can only appear once. Then try to connect product 1 to supplier 99.
--Look up: PRIMARY KEY with two columns · Expected: The table is created, the INSERT gives
--an error

CREATE TABLE product_suppliers (
    product_id INTEGER,
    supplier_id INTEGER,
    purchase_price REAL CHECK (purchase_price > 0),
    PRIMARY KEY (product_id, supplier_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

--Try to connect product 1 to supplier 99
--First, turn on foreign key checking:

PRAGMA foreign_keys = ON;

INSERT INTO product_suppliers
    (product_id, supplier_id, purchase_price)
VALUES
    (1, 99, 10.50);
	
--Create a table campaigns with name, start_date and end_date. Add a rule that end_date can
--never be before start_date. Test it with a campaign that ends before it starts.
--Look up: CHECK that compares two columns · Expected: The table is created, the INSERT
--gives an error

CREATE TABLE campaigns (
    name TEXT,
    start_date TEXT,
    end_date TEXT,
    CHECK (end_date >= start_date)
);

--Test it with a campaign that ends before it starts

INSERT INTO campaigns (name, start_date, end_date)
VALUES ('Summer Sale', '2026-08-20', '2026-08-10');




--Level 3
--Create a table product_sizes with an own id, product_id (points to products), size (only S, M, L or
--XL) and stock (0 if nothing is given). The same product can't have the same size twice. Test it by
--adding size M for product 1 twice.
--Look up: UNIQUE on two columns · Expected: The first INSERT works, the second gives an
--error


CREATE TABLE product_sizes (
    id INTEGER PRIMARY KEY,
    product_id INTEGER,
    size TEXT CHECK (size IN ('S', 'M', 'L', 'XL')),
    stock INTEGER DEFAULT 0,
    UNIQUE (product_id, size),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

--2. Add size M for product 1 the first time

INSERT INTO product_sizes (product_id, size)
VALUES (1, 'M');

--3. Try adding size M for product 1 again

INSERT INTO product_sizes (product_id, size)
VALUES (1, 'M');


--Create a table employees where each employee can have a manager, who is also an employee in
--the same table. The boss has no manager. Add the boss and two employees who report to the
--boss.
--Look up: a foreign key that points to its own table · Expected: 3 rows


CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    manager_id INTEGER,
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);

--2. Add the boss and two employees

INSERT INTO employees (employee_id, name, manager_id)
VALUES (1, 'Amar', NULL);

INSERT INTO employees (employee_id, name, manager_id)
VALUES (2, 'Sahithi', 1);

INSERT INTO employees (employee_id, name, manager_id)
VALUES (3, 'Vevanth', 1);

--3. Show all employees

SELECT * FROM employees;



--Create two tables: teams and players, where a player belongs to a team. Make it so that when a
--team is deleted, its players are deleted automatically. Add one team with two players, delete the
--team, and check the players table.
--Look up: ON DELETE CASCADE · Expected: 0 rows left in player

CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY,
    team_name TEXT NOT NULL
);

CREATE TABLE players (
    player_id INTEGER PRIMARY KEY,
    player_name TEXT NOT NULL,
    team_id INTEGER,
    FOREIGN KEY (team_id)
        REFERENCES teams(team_id)
        ON DELETE CASCADE
);



















