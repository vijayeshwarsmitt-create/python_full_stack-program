# 10. W3Schools SQL Practice Questions

This document contains a comprehensive set of practice questions based on the standard W3Schools Sample Database schema. These questions range from basic selection to complex multi-table joins.

---

## 1. Basic SELECT (20 Questions)
1.  Select all columns from the `Customers` table.
2.  Select only the `CustomerName` column from `Customers`.
3.  Select distinct `Country` from the `Customers` table.
4.  Select the `City` column from the `Customers` table.
5.  Select all `Products` where the `Price` is greater than 50.
6.  Select all `Orders` where the `OrderID` is exactly 10248.
7.  Select all `Customers` who live in 'Germany'.
8.  Select all `Employees` who were hired after the year 1993.
9.  Select all `Products` where the `CategoryID` is 1.
10. Select the top 5 `Customers`.
11. Select the first 10 `Products`.
12. Select unique `Cities` from the `Customers` table.
13. Select all `Orders` where the `ShipName` is 'United Packages'.
14. Select all `Customers` whose `CustomerID` starts with the letter 'A'.
15. Select all `Products` with a price between 10 and 20.
16. Select all `Orders` where the `OrderDate` is NULL.
17. Select all `Employees` whose `LastName` is 'Davolio'.
18. Select all `Products` that are NOT in category 2.
19. Select all `Customers` living in either 'Germany' or 'France'.
20. Select all `Customers` who are NOT from the 'UK'.

---

## 2. WHERE + Operators (20 Questions)
1.  Use `LIKE` to find all `Customers` whose names start with 'B'.
2.  Find all `Customers` whose names end with the letter 's'.
3.  Find all `Customers` whose names contain the string 'on'.
4.  Use `IN` to select customers from multiple countries (e.g., 'Germany', 'France', 'UK').
5.  Use `BETWEEN` to find products within a specific price range.
6.  Use `NOT BETWEEN` to find products outside a specific price range.
7.  Use the `AND` operator to combine two conditions.
8.  Use the `OR` operator to combine two conditions.
9.  Use the `NOT` operator to exclude a condition.
10. Use `IS NULL` to find records with missing values.
11. Use `IS NOT NULL` to find records that have values.
12. Use the `>=` (Greater than or equal to) operator to filter data.
13. Use the `<>` (Not equal) operator to filter data.
14. Find all `Orders` placed between two specific dates.
15. Find all `Products` where the price is > 100 AND `CategoryID` is 2.
16. Find all `Customers` from 'London' OR 'Paris'.
17. Find all `Employees` who are NOT from the 'USA'.
18. Find all `Orders` shipped after a specific date.
19. Find all `Products` where the price is NOT between 20 and 50.
20. Combine `LIKE` and `AND` in a single query to filter specific names and locations.

---

## 3. ORDER BY + LIMIT (10 Questions)
1.  Order all `Customers` by `Country` alphabetically.
2.  Order all `Products` by `Price` in descending order (DESC).
3.  Order a table result by multiple columns (e.g., `Country` then `City`).
4.  Order all `Employees` by their `BirthDate`.
5.  Order all `Orders` by `OrderDate` in descending order.
6.  Retrieve the top 3 most expensive products.
7.  Retrieve the 5 cheapest products.
8.  Order `Customers` by `City` in ascending order (ASC).
9.  Sort a list of `Suppliers` by `Country`, and then by `City` within each country.
10. Order a result-set by the length of a string column (e.g., length of `CustomerName`).

---

## 4. GROUP BY + Aggregates (20 Questions)
1.  Count the total number of records in the `Customers` table.
2.  Count the number of `Customers` per country.
3.  Count the total number of `Orders` placed by each customer.
4.  Find the average price of all products.
5.  Find the maximum price in the `Products` table.
6.  Find the minimum price in the `Products` table.
7.  Find the sum of all quantities in the `OrderDetails` table.
8.  Group products by `CategoryID` and show the count.
9.  Group customers by `Country` and show the count.
10. Group customers by `City` and show the count.
11. Find the total number of orders placed per year.
12. Find the total sales amount per product.
13. Find the total sales amount per customer.
14. Find the average salary of employees (if salary column exists).
15. Find the maximum salary among employees.
16. Count the number of employees in each city.
17. List customers who have placed more than 5 orders.
18. Use the `HAVING` clause with `COUNT` to filter groups.
19. Use the `HAVING` clause with `SUM` to filter summed values.
20. Use `GROUP BY` on multiple columns (e.g., `Category` and `Supplier`).

---

## 5. JOINS (60 Questions)

### INNER JOIN (15 Questions)
1.  Join `Customers` and `Orders` to show which customer placed which order.
2.  Join `Orders` and `OrderDetails` to see item details for each order.
3.  Join `Products` and `Categories` to see which product belongs to which category.
4.  Join `Orders`, `Customers`, and `Employees` to see a full order report.
5.  Join `Products` and `Suppliers` to see who supplies which product.
6.  Retrieve `CustomerName` along with their corresponding `OrderID`.
7.  Retrieve `ProductName` along with the quantity sold in an order.
8.  List all `Orders` along with the name of the `Employee` who handled them.
9.  List all `Orders` along with the `Shipper` name.
10. List all `Products` with their full category names.
11. Show the number of orders per customer using a Join and Group By.
12. Show total sales per product by joining `Products` and `OrderDetails`.
13. List all `Employees` along with the total number of orders they have processed.
14. Show `OrderID` along with the price of each product in that order.
15. Calculate the total amount for each order by joining tables.

### LEFT JOIN (10 Questions)
1.  Show all `Customers` and their orders (even if they haven't placed any).
2.  Identify `Customers` who have placed zero orders.
3.  Show all `Products` and their order details (even if never ordered).
4.  Find `Products` that have never been ordered.
5.  List all `Employees` and the orders they handled (include employees with no orders).
6.  Show all `Categories` and the products within them.
7.  Identify `Categories` that currently have no products linked to them.
8.  List all `Suppliers` and the products they supply (include suppliers with no products).
9.  Find `Suppliers` who do not supply any products.
10. Show all `Customers` with their total order count (even if count is zero).

### RIGHT JOIN (10 Questions)
1.  Show all `Orders` and their customers (include orders with no valid customer).
2.  Show all `Categories` and their products (include categories with no products).
3.  Show all `Products` and their order details (from the perspective of order details).
4.  Show all `Employees` and the orders they processed (from the perspective of orders).
5.  Show all `Suppliers` and their products (from the perspective of products).
6.  List all `Categories` and the products associated with them.
7.  List all `Shippers` and the orders they have shipped.
8.  List all `Orders` and the `Employees` who handled them (perspective of orders).
9.  List all `Shippers` and all the `Orders` they have handled.
10. Show all `Orders` and the corresponding `Customers`.

### CROSS JOIN (10 Questions)
1.  Combine every `Customer` with every `Product`.
2.  Create a combination of all `Employees` and all `Shippers`.
3.  Generate all possible combinations of `Categories` and `Suppliers`.
4.  Match every `Customer` with every `Employee`.
5.  Match every `Product` with every `Employee`.
6.  Generate combinations of all `Orders` and all `Shippers`.
7.  Combine all `Categories` with all `Customers`.
8.  Combine all `Suppliers` with all `Employees`.
9.  Create combinations of all `Countries` and all `Products`.
10. Create combinations of all `Cities` and all `Employees`.

### SELF JOIN (15 Questions)
1.  Find employees who report to the same manager.
2.  Display each employee's name along with their manager's name.
3.  Find employees who live in the same city.
4.  Find customers who are from the same country.
5.  Find products that belong to the same category.
6.  List employees who were born in the same year.
7.  Identify customers located in the same city.
8.  Find orders that were placed on the same exact date.
9.  List employees who were hired in the same year.
10. Find products that have the exact same price.
11. Find employees who hold the same job title.
12. Identify customers who share the same postal code.
13. Find products that come from the same supplier.
14. Find orders that used the same shipping company.
15. List all employees who share the same manager.
