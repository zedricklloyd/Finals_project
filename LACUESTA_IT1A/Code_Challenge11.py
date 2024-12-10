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