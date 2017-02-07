students = [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# for idx in range(len(students)):
# 	print students[idx]['first_name']

users = {
 	'Students': [ 
    	{'first_name':  'Michael', 'last_name' : 'Jordan'},
    	{'first_name' : 'John', 'last_name' : 'Rosales'},
    	{'first_name' : 'Mark', 'last_name' : 'Guillen'},
    	{'first_name' : 'KB', 'last_name' : 'Tonel'}
  	],
 	'Instructors': [
     	{'first_name' : 'Michael', 'last_name' : 'Choi'},
    	{'first_name' : 'Martin', 'last_name' : 'Puryear'}
  	]
}

for category in users:
	print category
	counter = 1
	for user in users[category]:
		name_length = len(user['first_name']) + len(user['last_name'])
		print counter, "-", user['first_name'] + " " + user['last_name'] + " - " + str(name_length)
		counter += 1