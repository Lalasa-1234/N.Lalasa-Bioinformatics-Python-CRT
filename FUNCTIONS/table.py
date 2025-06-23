def table(num):
    for i in range (10):
     print(f"{num}*{num+i}=",num*(i+1))
n=int(input('enter the num:'))
table(n)
