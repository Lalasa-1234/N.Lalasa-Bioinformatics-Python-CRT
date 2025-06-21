n=int(input("Enter the value of n: "))
for i in range(n):
  for j in range(i+1):
    print('*',end=' ')
  print()
print("------------------------------------------------------------------------------------------------------------")
n=int(input("Enter the value of n: "))
for i in range(n):
    for j in range(n):
        if(j<=i):
            print(f"* ",end="")
    print()