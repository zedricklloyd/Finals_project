from activity2 import act2
from activity6 import act6
from activity7 import act7
from activity9 import act9
from activity11 import act11
from activity12 import act12
from activity13 import act13
from activity14 import act14


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

name = input("Enter your name: ")
deposit = eval(input("Enter the amount to deposit: "))

n1 = deposit // 1000
n11 = deposit - (n1 * 1000 )

n2 = n11 // 500
n22 = n11 % 500

n3 = n22 // 200
n33 = n22 % 200

n4 = n33 // 100
n44 = n33 % 100

n5 = n44 // 50
n55 = n44 % 50

n6 = n55 // 20
n66 = n55 % 20

n7 = n66 // 10
n77 = n66 % 10

n8 = n77 // 5
n88 = n77 % 5

n9 = n88 // 1
n99 = n88 % 1

print("\n Hi" , name , "your deposit exchange in PH denomination are as follow: ")
print("\n" , n1 ,"-  1000" , "\n" , n2 , "-  500" , "\n" , n3 , "-  200" , "\n" , n4 , "-  100" , "\n" , n5 , "-  50" , "\n" , n6 , "-  20" , "\n" , n7 , "-  10" , "\n" , n8 , "-  5" , "\n" , n9 , "-  1")