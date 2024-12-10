prelim = eval(input("Enter your Prelim grade ---->"))
midterm = eval(input("Enter your Midterm grade----->"))
semifinal = eval(input("Enter your Semi - final grade -->"))
final = eval(input("Enter your final grade --->"))
quiz = eval(input("Enter your quiz grade -->"))
project = eval(input("Enter your project grade ------->"))

FG=(prelim * .15) + (midterm * .15) + (semifinal * .15) + (final * .15) + (quiz * .25) + (project * .15)

print(f"\nYour final grade is: {round(FG , 2)}")

if FG >=101:
	print("Invalid input")

elif FG >=75:
	print("Congratulations! You passed the course ")

else:
	print("Sorry you failed")