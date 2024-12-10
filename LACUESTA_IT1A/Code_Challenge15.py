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
               

