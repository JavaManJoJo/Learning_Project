"""
Arithmetic operators
	+	addition
	-	subtraction
	/	division
	//	integer divide
	*	multiplication
	%	modulus
	**	power
"""

#modulus example
numberOfPeople = 2
numberOfApples = 11
remainingApples = numberOfApples % numberOfPeople

print(str(remainingApples) + " apple(s) left")

"""
Assignment Operators
	=	equals
	+=	plus equals
	-=	minus equals
	*+	time equals
	/=	divide equals
	%=	mod equals
"""

#Modulus Equals example
a = 5
b = 10

a %= b

print(str(a))

"""
Comparison Operators
always result in a boolean
	<	less than
	>	greater than
	<=	less than or equal to
	>=	greater than or equal to
	==	equal to
	!=	not equal to
"""

isGreaterThan = 5 > 10
print(isGreaterThan)

"""
Logical Operators
must take booleans and result in booleans
	add	 &&
		True and True = True
		True and False = False
		False and True = False
		False and False = False
	or   ||
		True or True = True
		True or False = True
		False or True = True
		False or False = False
	not  !
		Not True = False
		Not False = True
"""