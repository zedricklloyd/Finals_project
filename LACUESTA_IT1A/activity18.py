ngi=eval(input("How many triangles you want to create? "))

for x in range(1,6):
    for y in range(1,ngi+1):
        for z in range(1,x+1):
            print("*", end= " ")
        for a in range(5,x,-1):
            print(" ", end= " ")
        print( end= " ")
    print()
               