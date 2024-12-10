gold = 0
name = input("Hi, Please enter your full name: ")

isGold = input("is the mineral gold? ")

#if yes is not in lower case the program will then proceed to the else statement

if isGold.lower() == "yes":
	gold+=1
	print(f"\nHi {name}, Your total number of gold is {gold}")
else:
	print(f"Hi {name}, Your total number of gold is {gold}")