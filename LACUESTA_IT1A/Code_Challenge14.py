dang = True
bilang = 0

while dang == True:
    num = eval(input("Write a number:   "))

    if num == 0:
        print("Loop has terminated")
        print(f"The sum of all numbers given is {bilang}")
        break
           
    else:
        bilang += num
        continue


