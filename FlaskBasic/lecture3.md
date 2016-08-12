#Python Flask Week - Part 3
####Final Touches on Flask
- Validations
- Advanced Routing

####Why Validate?
- We need to validate form data because there are malicious threats out there
  - Malicious SQL statements
- When we validate, we have to tell our users or else we have a bad UX

####How Do We Validate?
- We can check lengths of inputs for presence (len("") is 0)
- We can check regular expressions for validating emails
- We can do basic conditional statements in combination with Flash
- We can worry about encryption checks next week

####Advanced Routing?
- How else can we pass information? Through the route itself!
```
@app.route('/users/<username>')
def show(username):
  return render_template('show.html', that_username=username)
```
