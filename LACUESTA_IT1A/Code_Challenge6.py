prelim = eval(input("Enter your Prelim grade ---->"))
midterm = eval(input("Enter your Midterm grade----->"))
semifinal = eval(input("Enter your Semi - final grade -->"))
final = eval(input("Enter your final grade --->"))
quiz = eval(input("Enter your quiz grade -->"))
project = eval(input("Enter your project grade ------->"))

if (prelim >= 65 and prelim <= 100) and (midterm >= 65 and midterm <= 100) and (semifinal >= 65 and semifinal <= 100) and (final >= 65 and final <= 100) and (quiz >= 65 and quiz <= 100) and (project >= 65 and project <= 100):
	FG=(prelim * .15) + (midterm * .15) + (semifinal * .15) + (final * .15) + (quiz * .25) + (project * .15)

	print(f"\nYour final grade is: {round(FG , 2)}")

	if FG >=75:
		print("Congratulations! You passed the course ")

	else:
		print("Sorry you failed")

else:
	print("Invalid Grades")