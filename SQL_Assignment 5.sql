/*Challenge 1: Retrieve customer data
Adventure Works Cycles sells directly to retailers, who then sell products to consumers. Each retailer that is an Adventure Works customer has provided a named contact for all communication from Adventure Works. The sales manager at Adventure Works has asked you to generate some reports containing details of the company’s customers to support a direct sales campaign.*/

/*1. Retrieve Customer Details
To retrieve all columns for all customers from the SalesLT.Customer table:*/


SELECT * FROM SalesLT.Customer;

/*2. Retrieve Customer Name Data
To create a list of all customer contact names including title, first name, middle name (if any), last name, and suffix (if any):*/

SELECT 
    Title, 
    FirstName, 
    MiddleName, 
    LastName, 
    Suffix 
FROM 
    SalesLT.Customer;

/*3. Retrieve Customer Names and Phone Numbers
To create a call sheet that lists the salesperson, a column named CustomerName that displays how the customer contact should be greeted, and the customer’s phone number:*/

SELECT 
    SalesPerson, 
    CONCAT(Title, ' ', LastName) AS CustomerName, 
    Phone 
FROM 
    SalesLT.Customer;



/*Challenge 2: Retrieve data for transportation reports
The logistics manager at Adventure Works has asked you to generate some reports containing details of the company’s customers to help to reduce transportation costs.*/

/*1. Retrieve a List of Cities
To produce a list of all customer locations, querying the SalesLT.Address table and retrieving the values for City and StateProvince, removing duplicates and sorting in ascending order of city:
*/

SELECT DISTINCT 
    City, 
    StateProvince 
FROM 
    SalesLT.Address 
ORDER BY 
    City ASC;


/*2. Retrieve the Heaviest Products
To identify the heaviest products, retrieving the names of the top ten percent of products by weight:*/


SELECT 
    Name 
FROM 
    SalesLT.Product 
WHERE 
    Weight IS NOT NULL 
ORDER BY 
    Weight DESC 
OFFSET 0 ROWS 
FETCH NEXT (SELECT CAST(COUNT(*) * 0.1 AS INT) FROM SalesLT.Product) ROWS ONLY;



/*Challenge 3: Retrieve product data
The Production Manager at Adventure Works would like you to create some reports listing details of the products that you sell.*/

/*1. Retrieve Product Details for Product Model 1
To find the names, colors, and sizes of the products with a product model ID of 1:*/


SELECT 
    Name, 
    Color, 
    Size 
FROM 
    SalesLT.Product 
WHERE 
    ProductModelID = 1;


/*2. Filter Products by Color and Size
To retrieve the product number and name of the products that have a color of black, red, or white and a size of S or M:*/


SELECT 
    ProductNumber, 
    Name 
FROM 
    SalesLT.Product 
WHERE 
    Color IN ('Black', 'Red', 'White') 
    AND Size IN ('S', 'M');


/*3. Filter Products by Product Number
To retrieve the product number, name, and list price of products whose product number begins with BK-:*/


SELECT 
    ProductNumber, 
    Name, 
    ListPrice 
FROM 
    SalesLT.Product 
WHERE 
    ProductNumber LIKE 'BK-%';


/*4. Retrieve Specific Products by Product Number
To modify the previous query to retrieve the product number, name, and list price of products whose product number begins with BK-, followed by any character other than R, and ends with a - followed by any two numerals:*/


SELECT 
    ProductNumber, 
    Name, 
    ListPrice 
FROM 
    SalesLT.Product 
WHERE 
    ProductNumber LIKE 'BK-[^R]%-__';


/*Challenge 4: Generate invoice reports
Adventure Works Cycles sells directly to retailers, who must be invoiced for their orders. You have been tasked with writing a query to generate a list of invoices to be sent to customers.*/


/*1. Retrieve Customer Orders
To return the company name from the SalesLT.Customer table, and the sales order ID and total due from the SalesLT.SalesOrderHeader table:*/


SELECT 
    C.CompanyName, 
    SOH.SalesOrderID, 
    SOH.TotalDue 
FROM 
    SalesLT.Customer AS C
JOIN 
    SalesLT.SalesOrderHeader AS SOH 
ON 
    C.CustomerID = SOH.CustomerID;


/*2. Retrieve Customer Orders with Addresses
To extend the customer orders query to include the Main Office address for each customer:*/


SELECT 
    C.CompanyName, 
    SOH.SalesOrderID, 
    SOH.TotalDue, 
    A.AddressLine1, 
    A.AddressLine2, 
    A.City, 
    A.StateProvince, 
    A.PostalCode, 
    A.CountryRegion 
FROM 
    SalesLT.Customer AS C
JOIN 
    SalesLT.SalesOrderHeader AS SOH 
ON 
    C.CustomerID = SOH.CustomerID
JOIN 
    SalesLT.CustomerAddress AS CA 
ON 
    C.CustomerID = CA.CustomerID
JOIN 
    SalesLT.Address AS A 
ON 
    CA.AddressID = A.AddressID
WHERE 
    CA.AddressType = 'Main Office';


/*Challenge 5: Retrieve customer data
As you continue to work with the Adventure Works customer and sales data, you must create queries for reports that have been requested by the sales team.*/


/*1. Retrieve a List of All Customers and Their Orders
To list all customer companies and their contacts, showing the sales order ID and total due for each order, including customers with no orders:*/


SELECT 
    C.CompanyName, 
    C.FirstName, 
    C.LastName, 
    SOH.SalesOrderID, 
    SOH.TotalDue 
FROM 
    SalesLT.Customer AS C
LEFT JOIN 
    SalesLT.SalesOrderHeader AS SOH 
ON 
    C.CustomerID = SOH.CustomerID
ORDER BY 
    CASE WHEN SOH.SalesOrderID IS NULL THEN 1 ELSE 0 END, 
    C.CompanyName;


/*2. Retrieve a List of Customers with No Address
To return a list of customer IDs, company names, contact names, and phone numbers for customers with no address stored in the database:*/


SELECT 
    C.CustomerID, 
    C.CompanyName, 
    C.FirstName, 
    C.LastName, 
    C.Phone 
FROM 
    SalesLT.Customer AS C
LEFT JOIN 
    SalesLT.CustomerAddress AS CA 
ON 
    C.CustomerID = CA.CustomerID
WHERE 
    CA.AddressID IS NULL;


/*Challenge 6: Retrieve order shipping information
The operations manager wants reports about order shipping based on data in the SalesLT.SalesOrderHeader table.
1.	Retrieve the order ID and freight cost of each order.
o	Write a query to return the order ID for each order, together with the the Freight value rounded to two decimal places in a column named FreightCost.
2.	Add the shipping method.
o	Extend your query to include a column named ShippingMethod that contains the ShipMethod field, formatted in lower case.
3.	Add shipping date details.
o	Extend your query to include columns named ShipYear, ShipMonth, and ShipDay that contain the year, month, and day of the ShipDate. The ShipMonth value should be displayed as the month name (for example, June)*/



/*1. Retrieve the Order ID and Freight Cost of Each Order
To return the order ID for each order, together with the Freight value rounded to two decimal places in a column named FreightCost:*/


SELECT 
    SalesOrderID, 
    ROUND(Freight, 2) AS FreightCost 
FROM 
    SalesLT.SalesOrderHeader;


/*2. Add the Shipping Method
To extend the query to include a column named ShippingMethod that contains the ShipMethod field, formatted in lower case:*/


SELECT 
    SalesOrderID, 
    ROUND(Freight, 2) AS FreightCost, 
    LOWER(ShipMethod) AS ShippingMethod 
FROM 
    SalesLT.SalesOrderHeader;


/*3. Add Shipping Date Details
To extend the query to include columns named ShipYear, ShipMonth, and ShipDay that contain the year, month, and day of the ShipDate, with the ShipMonth value displayed as the month name:*/


SELECT 
    SalesOrderID, 
    ROUND(Freight, 2) AS FreightCost, 
    LOWER(ShipMethod) AS ShippingMethod, 
    YEAR(ShipDate) AS ShipYear, 
    DATENAME(MONTH, ShipDate) AS ShipMonth, 
    DAY(ShipDate) AS ShipDay 
FROM 
    SalesLT.SalesOrderHeader;



/*Challenge 7: Aggregate product sales
The sales manager would like reports that include aggregated information about product sales.
1.	Retrieve total sales by product
o	Write a query to retrieve a list of the product names from the SalesLT.Product table and the total revenue for each product calculated as the sum of LineTotal from the SalesLT.SalesOrderDetail table, with the results sorted in descending order of total revenue.
2.	Filter the product sales list to include only products that cost over 1,000
o	Modify the previous query to include sales totals for products that have a list price of more than 1000.
3.	Filter the product sales groups to include only total sales over 20,000
o	Modify the previous query to only include only product groups with a total sales value greater than 20,000.*/



/*1. Retrieve Total Sales by Product
To retrieve a list of product names and the total revenue for each product, calculated as the sum of LineTotal from the SalesLT.SalesOrderDetail table, sorted in descending order of total revenue:*/


SELECT 
    P.Name, 
    SUM(SOD.LineTotal) AS TotalRevenue 
FROM 
    SalesLT.Product AS P
JOIN 
    SalesLT.SalesOrderDetail AS SOD 
ON 
    P.ProductID = SOD.ProductID 
GROUP BY 
    P.Name 
ORDER BY 
    TotalRevenue DESC;


/*2. Filter the Product Sales List to Include Only Products That Cost Over 1,000
To modify the previous query to include sales totals for products that have a list price of more than 1000:*/


SELECT 
    P.Name, 
    SUM(SOD.LineTotal) AS TotalRevenue 
FROM 
    SalesLT.Product AS P
JOIN 
    SalesLT.SalesOrderDetail AS SOD 
ON 
    P.ProductID = SOD.ProductID 
WHERE 
    P.ListPrice > 1000 
GROUP BY 
    P.Name 
ORDER BY 
    TotalRevenue DESC;

/*3. Filter the Product Sales Groups to Include Only Total Sales Over 20,000
To modify the previous query to only include product groups with a total sales value greater than 20,000:*/


SELECT 
    P.Name, 
    SUM(SOD.LineTotal) AS TotalRevenue 
FROM 
    SalesLT.Product AS P
JOIN 
    SalesLT.SalesOrderDetail AS SOD 
ON 
    P.ProductID = SOD.ProductID 
WHERE 
    P.ListPrice > 1000 
GROUP BY 
    P.Name 
HAVING 
    SUM(SOD.LineTotal) > 20000 
ORDER BY 
    TotalRevenue DESC;