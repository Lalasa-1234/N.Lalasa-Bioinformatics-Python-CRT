str=input("enter the string :")
uppercase_alpha=0
lowercase_alpha=0
numeric=0
special_charecter=0
for ch in str:
    if ch.isupper():
        uppercase_alpha+=1
    elif ch.islower():
        lowercase_alpha+=1
    elif ch.isdigit():
        numeric+=1
    else:
        special_charecter+=1
print(f"count of upper case letters :{uppercase_alpha}")
print(f"count of lower case letters :{lowercase_alpha}")
print(f"count of numeric :{numeric}")
print(f"count of apecial_charecter :{special_charecter}")