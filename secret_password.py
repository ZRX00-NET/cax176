RightP = "python123"
attempts = 0

while attempts < 3:
    UserP = input("Password:")

    if UserP == RightP:
        print("Access Granted.")
    else:
        attempts += 1


else:
    print("Access blcoked.")

    