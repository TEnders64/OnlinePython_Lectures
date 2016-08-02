#Python - AJAX & APIs
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
