num=int(input("enter the value: "))
print(f"natural numbers from 1 to {num} : ")
for i in range(1,num+1):
    print(i,end=" ")
#reverse 
num=int(input("enter the value: "))
for i in range(num,0,-1):
    print(i,end=" ")
#squares
num=int(input("enter the value: "))
for i in range(1,num+1):
    print(i**2)
#reverse of square
num=int(input("enter the value: "))
for i in range(num,0,-1):
    print(i**2)
#cubes
num=int(input("enter the value: "))
for i in range(1,num+1):
    print(i**3)
#reverse cubes
num=int(input("enter the value: "))
for i in range(num,0,-1):
    print(i**3)