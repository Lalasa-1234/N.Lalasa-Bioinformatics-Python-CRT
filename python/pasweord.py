password = input("Enter your password: ")

if len(password) < 10:
    print("Invalid password ")
else:
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    special_count = 0
    special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?\\`~"  
    for ch in password:
        if ch >= 'A' and ch <= 'Z':
            uppercase_count += 1
        elif ch >= 'a' and ch <= 'z':
            lowercase_count += 1
        elif ch >= '0' and ch <= '9':
            digit_count += 1
        elif ch in special_chars:
            special_count += 1
    if uppercase_count >= 3 and lowercase_count >= 3 and digit_count >= 1 and special_count >= 3:
        print("pasword is valid ")
    else:
        print("password is invalid")
