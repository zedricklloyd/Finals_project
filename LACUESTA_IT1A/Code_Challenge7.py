grocery = input("Did you buy a grocery? (yes/no):  ")
if grocery.lower() == "yes":
	name = input("Name of the item:  ")
	price = eval(input("Price of the item:  "))
	age = eval(input("Age:  "))
	amount = eval(input("Amount Given: "))
	
	tax = 0.123
	taxamount = price * tax
	total = price + taxamount

	if age <= 59:
		change = amount - total

		print(f"\nHi customer, you purchased a {name} , with a price of {price} plus 12.3 % tax ({taxamount}) total of {total} ")
		print(f"Amount Given: {amount}php")
		print(f"Change : {round(change , 2)}  ")


	if age >= 60:
		discount = 0.052
		disamount = price * 0.052
		distotal = price - disamount
		change1 = amount - distotal

		print(f"\nHello customer, you paid {price} for a {name} with a senior discount of 5.2 % ({disamount}). The total amount you paid is {round(distotal , 2)} ")
		print(f"Amount Given: {amount}php")
		print(f"Change : {round(change1 , 2)}  ")

else:
	print("No grocery purchased")
	