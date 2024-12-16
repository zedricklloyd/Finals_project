import os
def menu():
    print("\nWelcome to code compilation of Zedrick Lloyd Lacuesta")
    print("BSIT-1A")
    print("\nChoose what action you want to do:")
    print("\n1. Open Activity Folder")  
    print("2. Open Code Challenge Folder")
    print("3. Open Denomination")
    print("4. Exit Program")

def act1():
    print("Hello World")

def act2():
    name = input("What is your name?  ")
    print("Hi,", name)

def act4():
    number1 = eval(input("Enter number: "))
    number2 = eval(input("Enter number: "))

    sum = number1 + number2
    print(f"The sum of number1 and number2 is {sum}.")

def act5():
    print("FAHRENHEIT TO CELCIUS CONVERTER PROGRAM")
    print(" ==================================== ")

    fahrenheit = eval(input("Enter a number: "))
    celcius = ((fahrenheit - 32) * 5) / 9
    print(f"{fahrenheit} degree fahrenheit converter to celcius is {celcius} degrees.")

def act6():
    x = 5
    print(x)

    x+=10
    print(x)

    x+=15
    print(x)

    x+=30
    print(x)

def act7():
    gold = 0
    name = input("Hi, Please enter your full name: ")

    isGold = input("is the mineral gold? ")

    #if yes is not in lower case the program will then proceed to the else statement

    if isGold.lower() == "yes":
        gold+=1
        print(f"\nHi {name}, Your total number of gold is {gold}")
    else:
        print(f"Hi {name}, Your total number of gold is {gold}")

def act8():
    password = input("Enter your password: ")

    if password.lower() == "bsit":
        print("Acces granted")
        print("Enjoy using the system")

    elif password.lower() == "it":
        print("Enjoy using the system")

    else:
        print("Access denied")

def act9():
    age = eval(input("Enter your age ----->"))

    if age >=1 and age <=7:
        print("\nYour age is categorized as Toddler")

    elif age >=8 and age <=13:
        print("\nYour age is categorized as Pre-teen")

    elif age >=14 and age <=18:
        print("\nYour age is categorized as Teenager ")

    elif age >=19 and age <=31:
        print("\nYour age is categorized as Early Adulthood ")

    elif age >=32 and age <=45:
        print("\nYour age is categorized as Mid Adulthood ")

    elif age >=46 and age <=59:
        print("\nYour age is categorized as Post Adulthood ")

    elif age >=60 and age <=90:
        print("\nYour age is categorized as Senior ")

def act10():
    name = input("Enter your name: ")
    isStudent = input("are your current student of DLL? (yes or No) -->")

    if isStudent.lower() == "yes":
        yearlevel = input("\n f - Freshman \n s - sophomore \n j - Junior \n r - Senior \n what is your current level right now in DLL? ")
        if yearlevel.lower() == "f":
            print(f"Hi {name} you are Freashman")
        elif yearlevel.lower() == "s":
            print(f"Hi {name} you are sophomore ")
        elif yearlevel.lower() == "j":
            print(f"Hi {name} you are junior")
        elif yearlevel.lower() == "r":
            print(f"Hi {name} you are senior")
        else:
            print("Invalid choice")

def act11():
    for x in range(1,10):
        print (x, "Goodbye IT DePARTMENT")

def act12():
    for x in range(10,0,-1):
        print(x)

def act13():
    sum = 1
    num = eval(input("Enter a number: "))

    for x in range(num, 0, -1):
        sum *= x
    print(f"the factorial of {num} is {sum}")

def act14():
    for x in range(0,11):
        print(x, end = " ")
    for y in range(0,11):
        print("*", end = " ")
    print()

def act15():
    for x in range(0,11):
        print(x, end =" ")
    for y in range(0, x):
        print("*", end= " ")
    print()

def act16():
    for x in range(1,11):
        for z in range(1, x+1):
            print(" ", end= " ")
        for y in range(11, x,-1):
            print("*", end= " ")
        print()

def act17():
    col= eval(input("Enter nummber of column --> "))
    for x in range(1,11):
        for y in range(1,col+1):
          print(f"{x} x {y} = {x*y}",end= "\t")
        print()

def act18():
    ngi=eval(input("How many triangles you want to create? "))

    for x in range(1,6):
        for y in range(1,ngi+1):
            for z in range(1,x+1):
                print("*", end= " ")
            for a in range(5,x,-1):
                print(" ", end= " ")
            print( end= " ")
        print()
               
def act19():
    tuloy = True
    while tuloy == True:
        name = input("Enter your name: ")
        if  name.lower()== "stop":
            print("Program Terminated")
            break
        else:
            continue

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

def act21():
    tuloy = True
    count = 0

    while tuloy == True:
        name = input("Please enter a name(type 'end' to stop the loop ) ---> ")
            
        if name.lower() == "end":
            print("Loop has now stopped")
            print(f"You have entered {count} names")
            break
            tuloy = False
        else:
            count += 1

def act22():
    def acti22():
        def activity1():
            print("Hello World")
        activity1()
    acti22()

def act23():
    def factorial(number):
        """ This function's purpose is to compute/calculate the factorial of any number given """
        fact = 1
        for x in range(number, 0, -1):
            fact *= x

        return fact

    print(f"THe factorial of 13 is {factorial(13)}")

def act24():
    from activity23 import factorial

    print(f"the factorial of 7 is {factorial(7)} ")

def act25():
    courses = ["BSIT", "BSA", "BSAIS", "BTVTED", "BSSW", "BSPA", "Delete w/o index", "Delete with index"]

    courses.remove("Delete w/o index")
    courses.pop()
    courses.append("DHRS")
    courses.insert(0, "ABELS")

    print(courses)

def cc1():
    print("\t\t\t\t\t\t\t\t\t\t\t  * \n\t\t\t\t\t\t\t\t\t\t\t *** \n\t\t\t\t\t\t\t\t\t\t\t***** \n\t\t\t\t\t\t\t\t\t\t       ******* \n\t\t\t\t\t\t\t\t\t\t\t***** \n\t\t\t\t\t\t\t\t\t\t\t ***\n\t\t\t\t\t\t\t\t\t\t\t  *")

def cc2():
    name = input("Enter your name - - - > ")
    print("\t\t\t\t\t\t\t\t\t\t\t       * \n\t\t\t\t\t\t\t\t\t\t\t    * * * * \n\t\t\t\t\t\t\t\t\t\t\t  * * * * * * \n\t\t\t\t\t\t\t\t\t\t       * Hi!," , name ,"* \n\t\t\t\t\t\t\t\t\t\t\t  * * * * * * \n\t\t\t\t\t\t\t\t\t\t\t    * * * * \n\t\t\t\t\t\t\t\t\t\t\t       *")

def cc3():
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

def cc4():
    n1= eval(input("Enter a number - - > "))
    n2= eval(input("Enter a number - - > "))

    ans1 = n1 + n2
    ans2 = n1 - n2
    ans3 = n1 * n2
    ans4 = n1 // n2
    ans5 = n1 / n2
    ans6 = n1 % n2
    ans7 = n1 ** n2

    print("\nThe sum of " , n1 , "and" , n2 , "is" , ans1)
    print("The difference of " , n1 , "and" , n2 , "is" , ans2) 
    print("The product of " , n1 , "and" , n2 , "is" , ans3) 
    print("The floor division of " , n1 , "and" , n2 , "is" , ans4) 
    print("The quotient of " , n1 , "and" , n2 , "is" , ans5) 
    print("The remainder of " , n1 , "and" , n2 , "is" , ans6) 
    print(n1 , "exponent by " , n2 ,"is" , ans7) 

def cc5():
    print("=======================================================================================================")

    fahrenheit = eval(input("Enter temperature in Fahrenheit - - - >  "))

    c = ((fahrenheit - 32 ) * 5 ) / 9

    print(f"{fahrenheit} degrees Fahrenheit converted to celcius is {round(c, 2)} degrees")

def cc6():
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

def cc7():
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
	
def cc8():
    sum = 0
    for u in range(1, 11):
        num = int(input(f"Enter number {u} :"))
        sum += num
        
    print(f"The summation of all provided number is {sum}")

def cc9():
    for x in range(0,11):
        print(" ", end= " ")
    for y in range(0,x):
        print(" ", end= " ")
    for z in range(x, 10):
        print("*", end= " ")
    print()

def cc10():
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

def cc11():
    for x in range(1,4):
        for u in range(6,x,-1):
            print(" ",end= " " )

        for v in range(x,1,-1):
            print("*", end= " ")

        for y in range(1,x+1):
            print("*", end= " ")
        print()

    for x in range(4,0,-1):
        for u in range(6,x,-1):
            print(" ",end= " " )

        for v in range(x,1,-1):
            print("*", end= " ")

        for y in range(1,x+1):
            print("*", end= " ")
        print()

def cc12():
    for x in range(1,6):
        for u in range(6,x,-1):
            print(" ",end= " " )

        for v in range(1,x+1):
            print("*", end= " ")

        for y in range(1,x+1):
            print("*", end= " ")
        print()

    for x in range(4,0,-1):
        for u in range(5,0,-1):
            print(" ",end= " " )

        for v in range(6,x,-5):
            print("*", end= " ")

        for y in range(6,x,-5):
            print("*", end= " ")
        print()

def cc13():
    for x in range(1,6):
        for u in range(6,x,-1):
            print(" ",end= " " )

        for v in range(x,1,-1):
            print(v, end= " ")

        for y in range(1,x+1):
            print(y, end= " ")
        print()

    for x in range(4,0,-1):
        for u in range(6,x,-1):
            print(" ",end= " " )

        for v in range(x,1,-1):
            print(v, end= " ")

        for y in range(1,x+1):
            print(y, end= " ")
        print()

def cc14():
    dang = True
    bilang = 0

    while dang == True:
        num = eval(input("Write a number(type 0 to stop):   "))

        if num == 0:
            print("Loop has terminated")
            print(f"The sum of all numbers given is {bilang}")
            break
            
        else:
            bilang += num
            continue

def cc15():
    import os

    ting = True
    nut = 0

    while ting == True:
        ilan = input("\nDo you wish to create more triangle (yes/no) ? ")

        if ilan.lower() == "no":
            os.system("cls")
            print("Program terminated")
            break

        elif ilan.lower() == "yes":
            os.system("cls")
            nut += 1
            for x in range(1,6):
                for y in range(1,nut+1):
                    for z in range(1,x+1):
                        print("*", end= " ")
                    for a in range(5,x,-1):
                        print(" ", end= " ")
                    print( end= " ")
                print()
                continue
        else:
            os.system
            print("\nInvalid input, Please enter 'yes' or 'no' only")
            continue
                
def cc16():
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

isCont = True
while isCont == True:
    ask = input("Do you want to open the activities and codechallenge of this user(yes/no)? ")

    if ask.lower() == "yes":
        menu()
        know = input("Enter your choice number here ----> ")

        while True:
            if know == "1":
                print("\n==========ACTIVITY MENU===========")
                print("Choose the activity you want to see:")
                print("\nA. activity 1")
                print("B. activity 2")
                print("C. activity 3")
                print("D. activity 4")
                print("E. activity 5")
                print("F. activity 6")
                print("G. activity 7")
                print("H. activity 8")
                print("I. activity 9")
                print("J. activity 10")
                print("K. activity 11")
                print("L. activity 12")
                print("M. activity 13")
                print("N. activity 14")
                print("O. activity 15")
                print("P. activity 16")
                print("Q. activity 17")
                print("R. activity 18")
                print("S. activity 19")
                print("T. activity 20")
                print("U. activity 21")
                print("V. activity 22")
                print("W. activity 23")
                print("X. activity 24")
                print("Y. activity 25")
                print("Z. Return to Main Menu")
                show = input("Enter your choice here ---- > ")
                
                if show.lower() == "a":
                    act1()
                    
                elif show.lower() == "b":
                    act2()

                # elif show.lower() == "c":
                #     act3()

                elif show.lower() == "d":
                    act4()

                elif show.lower() == "e":
                    act5()

                elif show.lower() == "f":
                    act6()

                elif show.lower() == "g":
                    act7()

                elif show.lower() == "h":
                    act8()

                elif show.lower() == "i":
                    act9()

                elif show.lower() == "j":
                    act10()

                elif show.lower() == "k":
                    act11()

                elif show.lower() == "l":
                    act12()

                elif show.lower() == "m":
                    act13()

                elif show.lower() == "n":
                    act14()

                elif show.lower() == "o":
                    act15()

                elif show.lower() == "p":
                    act16()

                elif show.lower() == "q":
                    act17()

                elif show.lower() == "r":
                    act18()

                elif show.lower() == "s":
                    act19()

                elif show.lower() == "t":
                    act20()
                
                elif show.lower() == "u":
                    act21()

                elif show.lower() == "v":
                    act22()

                elif show.lower() == "w":
                    act23()

                elif show.lower() == "x":
                    act24()

                elif show.lower() == "y":
                    act25()
                
                elif show.lower() == "z":
                    print("\nRETURNING TO MAIN MENU....")
                    break

                else:
                    print("Invalid pick")
                    continue

                cont = input("\nDo you want to open other activities (yes/no)?")

                if cont.lower() != "yes":
                    print("\nReturning to Main Menu.....")
                    break


            elif know == "2":
                print("\n==========CODE CHALLENGE MENU===========")
                print("Choose the codechallenge you want to see:")
                print("\nA. Code Challenge 1")
                print("B. Code Challenge 2")
                print("C. Code Challenge 3")
                print("D. Code Challenge 4")
                print("E. Code Challenge 5")
                print("F. Code Challenge 6")
                print("G. Code Challenge 7")
                print("H. Code Challenge 8")
                print("I. Code Challenge 9")
                print("J. Code Challenge 10")
                print("K. Code Challenge 11")
                print("L. Code Challenge 12")
                print("M. Code Challenge 13")
                print("N. Code Challenge 14")
                print("O. Code Challenge 15")
                print("P. Code Challenge 16")
                print("Q. RETURN TO MAIN MENU")
                hello = input("Enter your choice here ---- > ")

                if hello.lower() == "a":
                    cc1()

                elif hello.lower() == "b":
                    cc2()

                elif hello.lower() == "c":
                    cc3()

                elif hello.lower() == "d":
                    cc4()

                elif hello.lower() == "e":
                    cc5()

                elif hello.lower() == "f":
                    cc6()

                elif hello.lower() == "g":
                    cc7()

                elif hello.lower() == "h":
                    cc8()

                elif hello.lower() == "i":
                    cc9()

                elif hello.lower() == "j":
                    cc10()

                elif hello.lower() == "k":
                    cc11()

                elif hello.lower() == "l":
                    cc12()

                elif hello.lower() == "m":
                    cc13()

                elif hello.lower() == "n":
                    cc14()

                elif hello.lower() == "o":
                    cc15()

                elif hello.lower() == "p":
                    cc16()

                elif hello.lower() == "q":
                    print("\nRETURNING TO MAIN MENU....")
                    break

                else:
                    print("Invalid pick")
                    continue

                hi = input("\nDo you want to open other code challenge (yes/no)?")

                if hi.lower() != "yes":
                    print("\nReturning to Main Menu.....")
                    break
            
            elif know == "3":
                print("========DENOMINATION=========")
                denomination()
                ya = input("\nDo you want to deposit again (yes/no)? ")

                if ya.lower() != "yes":
                    print("\nReturning to Main Menu.....")
                    break

            elif know == "4":
                print("PROGRAM TERMINATED")
                break
    elif ask.lower() == "no":
        print("PROGRAM TERMINATED")
        break

    else:
        print("INVALID PICK")
        continue
    