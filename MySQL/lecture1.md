#Python - MySQL Week

####Administrative
- Reminder for Slack: post questions in `#python-online` because we all benefit from that
- Another Reminder for Slack: pinned Python 1 Information Post in sidebar!

####Key Assignment: Sakila (Suh-KEE-luh)

####What's MySQL? What's SQL?
- Structured Query Language
  - We need some structured data in place first though
- What's Structured Data?
  - We need to separate out our representation of data and the relationships between data into tables.
  - But it's not good enough to just separate.  We need to be concerned about repetition.
    - Structured data strives to follow the DRY principle as well.  The process is called Normalization.
    - Let's build out an ERD (blueprint of our database) in MySQL Workbench to help us visualize.

####ERD Lemo
- Actors & Movies
  - Let's think about our data...
    - Actors might have a first and last name and then the films they've been in.
    - Movies might have a title and then the actors that have been in them.

![alt text](ActorsMoviesV1.png "ERD")

  - There is a whole lot of repetition going on here and a list of films for an actor is not great. How do we solve this?
    - RELATIONSHIPS!

####Relationships
- One to One (Social Security No.)
- One to Many (One country can have many states, but any one state can only belong to one country)
- Many to Many (One person can have many addresses and any one address can have many people at that address)

####Back to MySQL Workbench
- How do we describe the relationship between actors and movies?  How does our ERD need to change?

<<<<<<< HEAD
####Let's Forward Engineer this!
=======
####Group Activity: Cities & States
Using MySQL Workbench, build an ERD for a schema that will represent cities and states and how they relate to one another
- Make sure the table names follow the convention of plural lowercase
- Make sure to include `id`, `created_at`, `updated_at` in each table
- We only care about tracking a state's name and abbreviation
- We only care about tracking a city's name and population
- What relationship is there between the tables?
>>>>>>> 1924a6b9620bdf455c9927ec882595d7cb782631
