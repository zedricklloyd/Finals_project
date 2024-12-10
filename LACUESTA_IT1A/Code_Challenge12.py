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
