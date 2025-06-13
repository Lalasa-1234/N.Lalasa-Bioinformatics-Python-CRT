num=int(input("enter the value :"))
digitsum=0
rem=0
while(num!=0):
    rem=num%10
    digitsum=digitsum+rem
    num=num//10
print(f"summation is{digitsum} ")