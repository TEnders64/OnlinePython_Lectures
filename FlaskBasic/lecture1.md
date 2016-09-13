#Python - Flask Week

####Where Are We?
- We've learned Python
  - Those fundamentals are going to come in handy!
- Now where?
  - Let's build some stuff!

####This Week's Key Assignments
- Ninja Gold
- Registration
- Disappearing Ninjas

####The Flask Mini-Framework
- HTTP Request/Response Cycle
  - What's that look like again?
- Where does Flask come in?
  - Flask is going to be able to cover us from front to back and even handle DB communication (in a couple weeks)
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
- Arrange for a GET request to render a template that has a form which POSTs to another route and then redirects
- Introduce embedded python which includes passing data into the view and executing python logic
