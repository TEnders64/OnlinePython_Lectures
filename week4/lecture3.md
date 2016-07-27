#Python - Flask + MySQL Week ( THE WALL WEEK )
####Bcrypt + Flask
- Import bcrypt (after you've pip installed of course into your virtualenv)
- What it does for us
  - Hashes/encrypts passwords from something like: 'password' to something like 'hasdhf234ry5asdfjasdfoi'
  - The nice thing about bcrypt is that it does everything for us
  - like `generate_password_hash()`
```
hashed_pw = bcrypt.generate_password_hash(request.form['password']) #generate a password hash
```
  - Next thing it does is validate a password for us with `check_password_hash(arg1, arg2)` where arg1 is an existing hashed password and arg2 is our guess (password from a login form)
```
bcrypt.check_password_hash(user[0]['hash_pass'], request.form['password'])
```
####What order to do things in Login/Registration
- Registration
+ Validate the form for presence, length, EMAIL_REGEX, etc.
+ If the form info checks out, hash the password via `generate_password_hash()`
+ `INSERT` it into the corresponding table in your DB
- Login
+ Validate the form for presence, EMAIL_REGEX, etc.
+ Query your DB for an existing email or username
+ If their guess at an email or username does not exist, redirect back to login
+ Username or Email exists, so now check the saved password against the form's password via `check_password_hash()`
+ If it is correct, save the user's id into session and redirect, otherwise redirect to the login

####Lemo - Continue Building the Countries App Using Semi-RESTful routes
