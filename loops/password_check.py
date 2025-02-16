password = "123abc"

limit = 3

while limit > 0:
    userPass = input("Enter your password: ")
    limit = limit - 1
    if userPass == password:
        print("Password Matched!!!")
        break
    else:
        print(f"Incorrent Password! {limit} attempts remaining!")