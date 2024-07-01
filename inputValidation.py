def validateIntInput(textForUser):
	while True:
		userInput = input(textForUser)
		try:
			userInput = int(userInput)
			return userInput
		except:
			print("Invalid input. Try again")


def validateInputInList(textForUser, ValidInputs):
	while True:
		userInput = input(textForUser)
		if userInput in ValidInputs:
			return userInput
		else:
			print(f"Input must be one of following {ValidInputs}")