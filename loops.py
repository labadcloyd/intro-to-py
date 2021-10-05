# while loops
i=0
while(i<10):
	i+=1
	print(i)

# for loops
for letter in "Cloyd Abad":
	print(letter)

myFriends = ['joe', 'john', 'doe', 'meyer']

for friend in myFriends:
	# you can manipulate each element in each array
	# friend = "no one"
	# friend += " hey"
	friend = 'hey ' + friend
	print(friend)

for i in range(-10, 3):
	print(i)

for i in range(len(myFriends)):
	print(myFriends[i])

# exponent function
def raise_to_power(base_num, pow_num):
	result = int(base_num)
	for i in range(pow_num-1):
		result = result * int(base_num)
	return result
print(raise_to_power(3, 1))
