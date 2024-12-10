for x in range(1,6):
    for y in range(6,0,-1):
        print(" ", end= " ")
    for z in range(1,x+1):
        print("*", end= " ")
    print()

for x in range(5,0,-1):
    for y in range(x,6):
        print(" ", end= " ")
    for z in range(1,x+1):
        print("*", end= " ")
    print()