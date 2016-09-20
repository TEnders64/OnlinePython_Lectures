#Python - MySQL Week

####Administrative
- Reminder for Slack: Push code to GitHub when needing help.
- Getting To Know You: DM me on Slack with your availability.

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
