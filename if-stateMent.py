import math

age = int(input("enter your age : "))

if age >= 18:
    print("you are ready to sign the conract")
else:
    print("you are not old enough to sign this contract")



age1 = int(input("enter your age : "))

if age1 >= 100:
    print("you are too old to drive the car")
elif age1 >= 18:
    print("you are ready to sign this contract")
else:
    print("you are not enough to sign this contract")


#another conditon:

number = 100
input_number = int(input("enter the number 1 - 100 : "))

if number == input_number:
    print(f"{number} is equal to {input_number}")
elif number > input_number:
    print(f"{number} is greather than {input_number}")
else: 
    print(f"{number} is less than {input_number}")




#another condition of if else:

value = input("enter your name : ")

if value == "":
    print("you have to type your name!..")
else:
    print(f"your name is {value}")




#another exp:
#this is just my own idea i dont know what is this for!!!..
#math the formula of cercumference (a = 2 * math.pi * raduis) is for calculatin the edge of circle
raduis2 = 10
raduis = int(input("enter number 1- 10: "))
result = 2 * math.pi * raduis
result1 = 2 * math.pi * raduis2

if result > result1:
    print(f"{result} is grether than {result1}")
elif result < result1:
    print(f"{result} is less than {result1}")


#you can also use boolean or true or false:

value3 = True

if value3:
    print("this is for sale")
else:
    print("this is not for sale")




