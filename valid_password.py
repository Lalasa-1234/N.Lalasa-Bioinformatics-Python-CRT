name = input("Enter the name: ")
phone = input("Enter the phone number: ")
email = input("Enter the email: ")
password = input("Enter the password: ")
if len(phone) != 10 or not phone.isdigit():
    print("phone number is invalid")
else:
    if '@' not in email or '.' not in email:
        print("email is invalid")
    else:
        attherate_index = email.find('@')
        dot_index = email.rfind('.')
        if attherate_index < 1 or dot_index < attherate_index + 2 or dot_index + 4 != len(email):
            print("email is invalid")
        else:
            if len(password) < 10:
                print("password is invalid")
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
                    print("password is valid")
                else:
                    print("password is invalid")