num=int(input("enter the value: "))
#using if else
if(num>=-9 and num<=9):
    print(f"{num} is digit")
else:
    print(f"{num} is number")
#using turnery operator
result="digit"if(num>=-9 and num<=9)else "number"
print(f"{num} is {result}") 