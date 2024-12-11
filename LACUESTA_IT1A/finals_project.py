from activity2 import act2
from activity6 import act6
from activity7 import act7
from activity9 import act9
from activity11 import act11
from activity12 import act12
from activity13 import act13
from activity14 import act14

def act20():
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

def denomination():
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


def codechallenge16():
    balance = 0

    def create_account(name, initial_deposit = 0):
        Account_name = name
        b = 0
        b = initial_deposit
        balance = b
        print(f"\nAccount for {Account_name} with a initial deposit of {balance} has been created.")

    def deposit_amount(amount):
        global balance
        balance += amount
        print(f"\nYou deposited ₱{amount}. New balance is ₱{balance}")

    def check_balance():
        global balance
        print(f"Current balance is {balance}")

    def get_denomination(amount):
        libo = amount // 1000
        suk_libo = amount % 1000 

        five_h = suk_libo // 500
        five_suk = suk_libo % 500

        two_h = five_suk // 200
        two_suk = five_suk % 200

        one_h = two_suk // 100
        one_suk = two_suk % 100

        pipti = one_suk // 50
        suk_pip = one_suk % 50

        bente = suk_pip // 20
        suk_ben = suk_pip % 20

        sampo = suk_ben // 10  
        suk_sam = suk_ben % 10

        lima = suk_sam // 5
        suk_lima = suk_sam % 5

        piso = suk_lima // 1

        print(f"The Breakdown based on Philippine Denomination for the amount of {amount}")
        print(f"{libo} - 1000")
        print(f"{five_h} - 500")
        print(f"{two_h} - 200")
        print(f"{one_h} - 100")
        print(f"{pipti} - 50")
        print(f"{bente} - 20")
        print(f"{sampo} - 10")
        print(f"{lima} - 5")
        print(f"{piso} - 1")

    def withdraw_amount(amount):
        global balance
        if amount <= balance:
            balance -= amount
            print(f"Withdrew {amount}. New balance is {balance}")
        else:
            print("Insufficient balance")


    isCont = True
    while isCont == True:
        print("WELCOME TO MY BANK STIMULATION SYSTEM")
        print("================================")
        print("ENTER FROM THE OPTIONS BELOW")
        print("1 --- CREATE ACCOUNT")
        print("2 --- DEPOSIT")
        print("3 --- CHECK BALANCE")
        print("4 --- WITHDRAW")
        print("5 --- EXIT")


        pick = input("Enter your choice here ---> ")

        if pick == "1":
            print("BANK APPLICATION FORM")
            name = input("Enter your FULL name: ")
            amount = eval(input(f"Enter initial deposit for {name}: "))
            create_account(name, amount)
            print(f"\nAccount for {name} with a deposit of {amount} has been created.")
            continue

        elif pick == "2":
            deposit = eval(input("Enter the amount you want to deposit: "))
            deposit_amount(deposit)
        
            
        elif pick == "3":
            check_balance()
            get_denomination(balance)
            continue

        elif pick == "4":
            withdraw = eval(input("Enter the amount you want to withdraw: "))
            amount -= withdraw
            withdraw_amount(withdraw)
            continue 

        elif pick == "5":
            print("Program stopped")
            print(f"\nThank you for using our bank! \nPlease come again!")
            break

        else:
            print("Invalid pick. Please try again.")
            continue

def codechallenge3():
    fullname = input("Please type your full name: ")
    age = input("Please type your age: ")
    gender = input("Please type your gender: ")
    birthdate = input ("Please type your birth date: ")
    maritalStatus = input("Please type your marital status: ")
    religion = input("Please type your religion: ")
    nationality = input("Please type your nationality: ")
    height = input("Please type your height in cm: ")
    weight = input("Please type your weight in kl: ")
    contactnumber = input("Please type your contact number: ")
    email = input ("Please type your e-mail: ")
    address = input("Please type your home address: ")
    fathersname = input("Please type your father's full name: ")
    mothersname = input("Please type your mother's full name: ")
    hobby = input ("Please type your hobby: ")

    
    print ("\n Hi, My name is" , fullname , "and I'm" , str(age) , "years old" , gender , " born on" , birthdate, "\n My marital status is" , maritalStatus , "\n I'm " , religion , "\n I'm" , nationality ,  "My height is" , height , "cm" " and I'm" , weight , "kl" , "\n My number is" , contactnumber , "\n You may also contact me through my e-mail as" , email , "\n I live in" , address , "\n My father is" , fathersname , "and my mother is" , mothersname , "\n I love" , hobby )

    