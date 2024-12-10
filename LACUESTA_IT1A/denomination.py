name = input("Enter your name: ")
deposit = eval(input("Enter the amount to deposit: "))

n1 = deposit // 1000
n11 = deposit - (n1 * 1000 )

n2 = n11 // 500
n22 = n11 % 500

n3 = n22 // 200
n33 = n22 % 200

n4 = n33 // 100
n44 = n33 % 100

n5 = n44 // 50
n55 = n44 % 50

n6 = n55 // 20
n66 = n55 % 20

n7 = n66 // 10
n77 = n66 % 10

n8 = n77 // 5
n88 = n77 % 5

n9 = n88 // 1
n99 = n88 % 1

print("\n Hi" , name , "your deposit exchange in PH denomination are as follow: ")
print("\n" , n1 ,"-  1000" , "\n" , n2 , "-  500" , "\n" , n3 , "-  200" , "\n" , n4 , "-  100" , "\n" , n5 , "-  50" , "\n" , n6 , "-  20" , "\n" , n7 , "-  10" , "\n" , n8 , "-  5" , "\n" , n9 , "-  1")