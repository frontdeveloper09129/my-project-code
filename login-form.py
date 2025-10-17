user_pass_validation = int()
user_email_validtion = "@"
def file_open():
    with open("user_name_info.text", "a") as file1: 
        file1.write(f"email: {user_email}\npass: {user_pass}\n")
    print("you been successfull save your info!")

def saved_info():
    global user_pass
    global user_email

    while True:
        user_email = str(input("your email: "))
        user_pass = str(input("your password: "))

        if user_email.startswith("@"):
            if  user_email.strip() and user_pass.strip() != "":
                file_open()
            else:
                print("no info saved")
        elif user_pass.strip() != user_pass_validation and user_email_validtion:
            print("your password should have a number in the last item.. ")
            print("your email should start to @")
            
saved_info()



