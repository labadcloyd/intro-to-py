secret_word = 'cloyd'
guess_count = 0

while(guess_count<3):
	guess = input('Guess the secret word: ')
	if(guess == secret_word):
		print('Congratulations, you won!')
		guess_count = 3
	elif(guess != secret_word):
		guess_count += 1
		if(guess_count==3):
			print('You have ran out of guesses')
		else:
			print('Wrong guess, try again.')