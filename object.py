first_name = 'Cloyd'
last_name = 'Abad'
age = 20
sex = 'M'

profile = {
	'fname':first_name,
	'lname':last_name,
	'age':age,
	'sex':sex,
	'address':{
		'street':'National Highway',
		'city':'Dumaguete',
		'province':'Negros Oriental',
	}
}
print(profile)
print('My specific street is '+ profile['address']['street'])

newProfile = profile
tempAddress = {
	'street':'Medina St.',
	'city':'Sta. Catalina',
	'province':'Negros Oriental',
}
newProfile['address'] = tempAddress

print(newProfile)