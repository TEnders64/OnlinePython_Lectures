#sum List

a = [1,2,5,10,255,3]
def sum_list(list):
	summation = 0
	for i in range(0, len(list)):
		# print list[i]
		summation += list[i]
	print summation
sum_list(a)



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

for key, data in users.items():
    print key
    index = 1
    for student in data:
        full_name = student['first_name'] + ' ' + student['last_name']
        name_length = len(full_name) - 1
        print str(index) + ' - ' + full_name + ' - ' + str(name_length)
        index += 1
