import re

email_regex  = r".+([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+)"

another_regex = r".+[a-z]"
print email_regex

thing = "well hello there, my email is marbogast@codingdojo.com and I like trees"


print re.match(email_regex, thing)


print "we are here"
