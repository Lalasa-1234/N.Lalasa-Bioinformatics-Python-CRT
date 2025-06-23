name = input("Enter your name: ")
phone = input("Enter your phone number: ")
email = input("Enter your email: ")
password = input("Enter your password: ")
if len(phone) != 10 or not phone.isdigit():
    print("Invalid phone number")
else:
    if '@' not in email or '.' not in email:
        print("Invalid email")
    else:
        at_index = email.find('@')
        dot_index = email.rfind('.')
        if at_index < 1 or dot_index < at_index + 2 or dot_index + 4 != len(email):
            print("Invalid email")
        else:
            if len(password) < 10:
                print("Invalid password")
            else:
                upper = 0
                lower = 0
                digit = 0
                special = 0
                special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?\\`~"
                for ch in password:
                    if ch >= 'A' and ch <= 'Z':
                        upper += 1
                    elif ch >= 'a' and ch <= 'z':
                        lower += 1
                    elif ch >= '0' and ch <= '9':
                        digit += 1
                    elif ch in special_chars:
                        special += 1
                if upper >= 3 and lower >= 3 and digit >= 1 and special >= 3:
                    print("valid password")
                else:
                    print("Invalid password")