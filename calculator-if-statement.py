operator = input("enter your operator  : ")
num1 = int(input("enter the 1st number : "))
num2 = int(input("enter the 2nd number : "))


if operator== "+":
 result = num1 + num2
 print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "-":
   result = num1 - num2
   print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
   print(f"your {operator} is not valid")



#In Python, not is a logical operator that’s used to invert a Boolean value.
#If something is True, not makes it False.
#If something is False, not makes it True.
#exp:

value1 = input("enter your email : ")
value2 = input("enter your password : ")

if not value1:
   print("please enter your email!..")
if not value2:
   print("please enter your password!..")
else:
   print("you succecfully log in")


#the or operator meaning atleast one condition is true the the code will be run
#exp:

condition = 42
condition2 = 30


if 30 >= condition or condition2 <= 30:
   print("hellow")
else:
   print("good luck")


#the and operator meaning both condion should be true
#exp:

condition3 = True
condition4 = True

if condition4:
   print("hellow again")
else:
   print("good luck again")


# there are short cut in if statement!
#exp:

input_value = input("enter your name")

result1 = "please type something" if input_value == "" else (f"your name is {input_value}")
print(result1)
