while True:
    user = input("enter your the firts user number: ")
    user2 = input("enter your second user number: ")
    user3 = input("enter your third  user number: ")
    try:
        if not user or not user2 or not user3:
            print("please enter your number!")
            continue

        firts_user = int(user)
        second_user = int(user2)
        third_user = int(user3)

        average = input("do you want to see the average of your number?: (y/n) for yes and no!: ").lower()
        if average == "n":
            quit()

        elif average == "y":
            add = (firts_user + second_user + third_user) / 3
            print(f"the average is: {add}")
            break
            
        else:
            print("try again")
    except:
        print("there something wrong!")
    

