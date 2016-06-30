from random import randint


"""
if (boolean statement):
	do stuff ...
elif (another boolean statement):
	do this stuff instead ...
else:
	do other stuff ...

the if contorl structure is used for decisions
"""


def booleanExample():
	# Boolean Example
	isCat = False
	isDog = True

	if (isCat):
		print("Is a Cat !!! :3")
	# else if - elif
	elif (isDog):
		print("Is a Dog !!! :>")
	else:
		print("It's a nothing :T")


	age = int(input("Input your age. \n>>\t"))
	isMale = False

	userInputGender = input("Input your gender (M|F). \n>>\t")
	userInputGender = userInputGender.upper()

	if (userInputGender == "M"):
		isMale = True
	else:
		isMale = False

	# Integer Example
	if (age <= 10):
		print("That will be $5.00")
	elif (age < 65):
		if (isMale):
			print("That will be $11.00, SIR")
		else:
			print("That will be $10.00, milady")
	else:
		print("You can view the movie for free!!")



"""
while (boolean statement):
	do this stuff while the boolean statement is true

while loop: used to repeat an unknown number of times
"""
def getColorFromUser():
	favColor = None
	while (favColor == None):
		favColor = input("Enter favorite color. \n-->\t")
		favColor = favColor.lower()
		if (favColor == "blue"):
			print("Blue? Wahoo!")
		elif (favColor == "red"):
			print("Red? Go to bed!")
		elif (favColor == "yellow"):
			print("Yellow is wrong")
		else:
			print("That's a funny thing to say.")
			favColor = None
	print("Bye")
	return favColor



"""
for [object] in [list of objects]:
	do stuff for each of the objects in the list of objects

for loop: used to repeat a known number of times
"""
def forLoopExample():
	sumOfRandom = 0
	for i in range(0, 10):
		sumOfRandom += randint(1, 1000)
	print(sumOfRandom)


def main():
	userColor = getColorFromUser()
	forLoopExample()

main()