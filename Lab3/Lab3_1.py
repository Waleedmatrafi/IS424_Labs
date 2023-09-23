employ_Info = {}
user_Input = ""
while not user_Input == "no":
    print("Please enter Employee's name (Enter 'no' to exit)")
    user_Input = input()
    temp = user_Input
    employ_Info[user_Input] = ""
    if not user_Input == "no":
        print(f"Please enter {user_Input} salary (Enter 'no' to exit)")
        user_Input = input()
        employ_Info[temp] = user_Input