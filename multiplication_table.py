num=int(input("enter the value: "))
for i in range (1,num+1):
    print(f"{i}:")
    for j in range (1,11):
        print(f"{i}x{j}={i*j}")