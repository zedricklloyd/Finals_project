even_number =[]
odd_sum = 0
isCont = True

while isCont == True:
    user_input = int(input("Enter a number(type 0 to stop): "))


    if user_input == 0 :
        break

    if user_input % 2 == 0:
        even_number.append(user_input)

    else:
        odd_sum += user_input
        continue

print(f"sum of odd nummbers:{odd_sum}")
print(f"even numbers: {even_number}")