# Creating Lists
# Lists contain elements of any type
emptyList = []
alist = ["A", "b", "1"]
elements = ["Fire", "Water", "Earth", "Air"]
ages = [1, 2, 3, 7, 3, 9, 1]
heights = [5.5, 5.4, 5.7]
randomList = [1, 5.5, "String", True]

# Accessing elements
# Indexes		0		1		2		3
elements = ["Fire", "Water", "Earth", "Air"]

# Accessing a single element
# print the second item in the list
print(elements[1])

# Access multiple elements
# print all but the first item
# listName[startIndex:endIndex]
print(elements[1:4])
# listName[:endIndex]
print(elements[:4])
# listName[startIndex:]
print(elements[1:])


# Append to list
# elements.append("Heart")
# print(elements)

# Extend
# elements.extend(alist)
# print(elements)

# Insert
elements.insert(1, "Heart")
elements.insert(3, "Heart")
print(elements)

# Remove
# elements.remove("Heart")
# print(elements)

# Pop
elements.pop(3)
print(elements)

# Cler
#elements.clear()
#print(elements)

# Global Pyhthon Function used for lists
# Len(alist)
print("Number of elements: " + str (len(elements)))



anElement = "Heart"
print(anElement[1:4])