sum = 1
num = eval(input("Enter a number: "))

for x in range(num, 0, -1):
    sum *= x
print(f"the factorial of {num} is {sum}")