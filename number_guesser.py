import random

hr = "**********"

print hr + "LET'S PLAY GUESS A NUMBER" + hr

random_number = random.randint(1, 100)

hot_range = range((random_number - 10), (random_number + 10))

def checkCounter( counter ):
		if counter == 3: 
			print "You're out of guesses"
			quit()

def getGuess():
	guess = raw_input("Guess a number between 1 and 100 > ")

	if guess.isdigit() == False:
			print "guess must be a number, dummy"
			quit()
	else:
		return int(guess)

def checkGuess( guess ):
	if guess != random_number:
			answer = False
			return answer
	else: 
			answer = True
			return answer

answer = False
counter = 0

while answer  == False:
	g = getGuess()
	result = checkGuess(g)
	counter += 1
	if result == False and g in hot_range:
			checkCounter(counter)
			print "Not quite, but close!"
			continue
	elif result == True:
			print "YOU GOT IT"
			quit()
	else:
			checkCounter(counter)
			print "Nope, try again"
			continue

