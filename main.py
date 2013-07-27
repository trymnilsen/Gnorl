gameRunning = True

print("Welcome to the adventures of Gnorl \nyour adventure starts now")

while gameRunning:
	inputString = raw_input("Select Attack: ")
	commandArgs = inputString.split()
	for arg in commandArgs:
		print("Args : "+arg)
	gameRunning = False
