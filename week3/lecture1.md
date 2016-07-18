#Python - Flask Week

####Where Are We?
- We've learned Python
  - Those fundamentals are going to come in handy!
- We've learned MySQL
  - SQL queries are tough, but they're necessary to CRUD our database.
- Now where?
  - Let's build some stuff!

####The Flask Mini-Framework
- HTTP Request/Response Cycle
  - What's that look like again?
- Where does Flask come in?
  - Flask is going to be able to cover us from front to back and even handle DB communication
    - We can catch incoming HTTP requests!
    - We can handle <form> data & validate it!
    - We can then do some logic and render pages (templates) with embedded Python in there!
    - We could redirect users elsewhere!

#####GET & POST requests
- GET requests
  - Links and redirects
- POST requests
  - Forms package up information for us in an envelope and deliver it on a 'wire'
  - ```<form action="/users" method="post">``` Here our 'wire' is the route ```/users```

#####Templates
- Client-side views  
  - Client-side meaning HTML we are going to deliver to the user
  - Jinja2 templating is built into Flask when we install it.
  - All we have to do is set up a templates folder in our project!

#####Let's Get Flasking with a Lemo
