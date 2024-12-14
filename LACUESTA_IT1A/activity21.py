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