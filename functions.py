from math import sqrt

# Creating a function
# def functionName(parameter...):
#	code inside

# Coding Standard Rules to function
# 	name is a verb/action/command
# 	descriptive but short
#	should only do a single thing

# Colons define scope

def sayHelloToUser(userName):
	print("Hello, " + userName + " I hope you are having a good day today.")

def getUserName():
	userName = input("What is your name?\n--> ")
	return userName

def getHypotenuseLength(a, b):
	c = a**2 + b**2
	c = sqrt(c)
	return c

def main():
	userName = getUserName()
	sayHelloToUser(userName)

	a = 3
	b = 4
	print(getHypotenuseLength(a, b))

main()
