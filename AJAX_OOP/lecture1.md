#Python - AJAX & APIs
####New Changes
- **Weekly Mentor Sessions Have a New Look ~ Moving to Slack**
  - More Responsive Help from your classmates and thosewho are ahead, plus Instructor & TAs
  - Could come in the form of a Text response, Hangout, or Screenhero
  - There are 3 **MUSTS** we ask you provide before reaching out for help...
    1. Put your code in a GitHub **repository**, **gist** or Slack **snippet**
    2. Articulate what **you think** the problem is
    3. List what you’ve already tried to solve the problem

- **Code Reviews**
  - Keep Submitting Your Code to the Learning Platform
  - Key Assignments will be code reviewed
    - **WEEK 4** The Wall
    - **WEEK 5** Ajax Notes
    - **WEEK 6** Ninja Gold, Disappearing Ninjas (Django)
    - **WEEK 7** Semi-Restful Routes, Belt Reviewer
    - **WEEK 8** Black Belt Week! No Code Reviews
  - Push your assignments to GitHub repos and send the link to your repo to me on Slack in a DM.  I can code review and submit pull requests to you!
- **Algorithms**
  - The Algorithms Slack Channel is where all things Algorithms will take place.  With the algorithm book in hand, you will self-pace but have a place to discuss them with other students and instructors/TAs.
- **4 more weeks of Python instruction**
  - 4 sessions a week
    - Prompt us for topics/demos to discuss in more depth
  - **Monday/Tuesday/Wednesday/Thursday 3pm Pacific**
  - We commence **September 30th**

####What Do We Know So Far?
- We can set up Flask servers to handle...
  - Requests (form data), rendering templates (client views), redirects, Validations
  - Incorporating BCrypt to encrypt passwords
  - Connecting to our MySQL DBs and run queries (CRUD operations)

####What Else Can We Do?
- So far, we've only managed our own data, but what if someone else (external) wants our data or we want THEIR data?
  - Enter APIs

####Application Program Interfaces
- APIs are what apps use to allow access points to their information
  - The information they WANT to be seen that is (think Facebook or Twitter)
  - APIs tend to return JSON data

####JSON data (Javascript Object Notation)
- An example of JSON:
```
var data = {
            results: [
              {
                name: 'Heather',
                hobby: 'Coding'
              },
              {
                name: 'Jeff',
                hobby: 'Coding'
              },
              {
                name: 'Todd',
                hobby: 'Teaching Others To Code'
              }
            ],
            date: '08-01-2016',
            version: 0.9
          }
```
- Nothing to be afraid of because what does it look like?  Python Dictionaries and Lists!
- But we need to know a little bit about Javascript in order to manipulate/manage JSON

####Comparisons Between Python and Javascript
- Javascript lives mostly on the client-side so we're talking `<script>` tags in our templates!
- If you haven't been keeping up with your algorithms, here's a fast and dirty breakdown of how to get into JS
- The JSON example above, we're going to iterate over the results array (array in JS, not list) from inside the data var
```
for (var i = 0; i < data.results.length; i++){
  console.log("name: ", data.results[i].name, " Hobby: ", data.results[i].hobby);
}
```
- For loops are a bit different and we need semicolons!  We can use dot notation or bracket notation as well to access properties.

####Where APIs Come In with Flask
- We can turn our Flask Apps into APIs that serve out data in the form of JSON!
  - Why would we want to do this?
    - So our back-end (Flask server and MySQL DB) only serves data out to the front-end
    - Single Page Applications or SPAs
      - AJAX allows us to send requests out 'behind the scenes' and update our pages dynamically without leaving or refreshing!

####AJAX!!!
- Asynchronous Javascript and XML
- Allows us to send an HTTP request (POST or GET) that will send or fetch data for us
- We absolutely need jQuery for this!
- An External API Example
```
<script>
$(document).ready(function(){
  $.get('http://someurl.com/users', function(data){
      console.log(data);
    }, 'json');
});
</script>
```
- Example of Hitting Our Own Flask Server
```
<script>
$(document).ready(function(){
  $.get('/users', function(data){
      console.log(data);
    }, 'json');
});
</script>
```
####Lemo - OpenWeatherMap API
