col= eval(input("Enter nummber of column --> "))
for x in range(1,11):
    for y in range(1,col+1):
       print(f"{x} x {y} = {x*y}",end= "\t")
    print()