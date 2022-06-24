
def password_validator(password):
    password_valid = True
    digit_counter = 0
    if not 6 <= len(password) <= 10:
        password_valid = False
        print("Password must be between 6 and 10 characters")
    if any(not j.isalnum() for j in password):
        print("Password must consist only of letters and digits")
        password_valid = False

    for i in password:
        current_ch = i
        if i.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        print("Password must have at least 2 digits")
        password_valid = False

    if password_valid:
        print("Password is valid")


password = input()
password_validator(password)
