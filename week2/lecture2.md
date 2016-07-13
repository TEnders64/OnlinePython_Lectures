#Python - MySQL Week

####SQL Queries - Using the World DB

####Basic CRUD Operations with a DB
- Create
- Read/Retrieve
- Update
- Delete  

####Let's Do Some CRUD with SQL
- SELECT (Read/Retrieve)
  - Example: ```SELECT * FROM countries```

- INSERT (Create)
  - Example: ```INSERT INTO countries (code, name, continent, region) VALUES ('PET', 'Petoria', 'North America', 'North America')```

- UPDATE (Update!)
  - Example: ```UPDATE countries SET continent = 'North and South Petoria' WHERE name = 'Petoria'```

- DELETE (Delete!)
  - Example: ```DELETE FROM countries WHERE name = 'Petoria'```

####JOINS!
- JOIN vs. LEFT JOIN vs. RIGHT JOIN vs. ...
![alt text](Joins.jpg "JOINS Venn Diagram")
- Let's bulk up an earlier ```SELECT``` statement, because we want to know the languages that Americans speak.
  - ```SELECT * FROM countries JOIN languages ON countries.id = languages.country_id```
    - Cool! We just slammed the two tables together.  Granted, it's way too much info for us, but we can deal with that.
- WHERE clause helps us add specificity or conditions
  - ```SELECT * FROM countries JOIN languages ON countries.id = languages.country_id WHERE countries.name = 'United States'```
  - Let's hone in on the fields we actually WANT to bring back.
  - ```SELECT countries.name, languages.language FROM countries JOIN languages ON countries.id = languages.country_id WHERE countries.name = 'United States'```

####Lemo - MySQL Countries
![alt text](MySQLCountries.png "Countries ERD")
- What query would you run to get all the countries that speak Slovene? Your query should return the name of the country, language and language percentage. Your query should arrange the result by language percentage in descending order.
- What query would you run to get all the cities in Mexico with a population of greater than 500,000? Your query should arrange the result by population in descending order.
