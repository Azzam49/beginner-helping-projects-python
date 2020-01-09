#! python3

user_pass = {"User":"Adam", "Password":"ABC123"}

while True:


    userName = input("Username : ")

    if userName == user_pass["User"]:
        print("Username Found!")
    else:
        print("Username not Found! Try again...")
        continue

    password = input("Password : ")

    if password == user_pass["Password"]:
        print("Login success!")
        break
    else:
        print("Wrong password ! Try again...")
        continue
