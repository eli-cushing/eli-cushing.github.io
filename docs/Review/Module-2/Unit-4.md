---
Module 2: Using Databases
Unit 4: Review Questions
---

# Review

1. What are the structural elements of a database table?

   > Each table stores information about records (rows in the table) in fields (columns in the tables).

2. What term is used to describe selecting and viewing information in a database?

   > Query.

3. How does an RDBMS such as Microsoft SQL Server differ from Microsoft Excel when used to store a dataset?

   > Excel is an example of a flat file system. These do not scale well, and usually support a single user only. RDBMS platforms enable many hundreds or thousands of users to connect concurrently and can support very large datasets. Also, an RDBMS can enforce data types for each column and validate information entered as fields and records.

4. What language is usually used to request data from an RDBMS such as Oracle?

   > Structured Query Language (SQL) is used to query RDBMS-based database platforms.

5. What is it that defines the relationship between tables in an RDBMS?

   > Each table contains a primary key whose value is unique for each record in the table. A foreign table can use the value of a primary key as a relation, storing the value in a foreign key field.

6. Give an example of unstructured data.

   > Images and text files and other document formats are unstructured data.

7. Give two examples of semi-structured data stores.

   > Key/value pair databases and markup language document stores.

8. Is an INSERT statement an example of a definition or manipulation language statement?

   > Manipulation language—it depends on the structure of a table (columns, data types, and constraints) being established already.

9. You need a development environment with a library of database functions. What type of interface are you using?

   > Programmatic access.

10. How can a client-server application architecture be described if there is the potential for the structure of the application platform to be developed further?

> This could be described as a two-tier application. It could be re-developed as a three-tier application by specifying presentation, application, and data layers.
