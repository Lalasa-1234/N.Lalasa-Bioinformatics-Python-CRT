num=int(input("Enter the integer value: "))
#using if else statements
if(num>0):
    print(f"{num} is positive")
elif(num<0):
    print(f"{num} is negetive")
else:
    print(f"{num} is 0")
#using ternary operator
res="positive number" if(num>0) else "negetive number" 
print(f"{num} 5{res}")