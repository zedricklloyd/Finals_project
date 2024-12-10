import os
isContinue =True
nah = 0
while isContinue == True:
    ngi=input("Would you like to add another triangle (yes/no)? ")

    if ngi.lower() == "no":
        print("PROGRAM TERMINATED")
        break
    else:
        os.system('cls')
        nah += 1
        for x in range(1,6):
            for y in range(1,nah+1):
                for z in range(1,x+1):
                    print("*", end= " ")
                for a in range(5,x,-1):
                    print(" ", end= " ")
                print( end= " ")
            print()
        continue    

def codechalleng2():
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

def codechallenge10():
    for x in range(1,6):
        for u in range(6,x,-1):
            print(" ",end= " " )

        for v in range(1,x+1):
            print("*", end= " ")

        for y in range(1,x+1):
            print("*", end= " ")
        print()

    for x in range(1,6):
        for u in range(1,x+1):
            print(" ",end= " " )

        for v in range(6,x,-1):
            print("*", end= " ")

        for y in range(6,x,-1):
            print("*", end= " ")
        print()