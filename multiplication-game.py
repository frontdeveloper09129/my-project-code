import random
import time


list_number = []
operator = ["+", "-", "*", "/"]

def funtion_game():
   global list_number
   global operator
   
   for i in range(10):
     num = random.randint(1, 100)
     list_number.append(num) #In Python, append() is a list method that means “add something to the end of a list.”
     get_number = random.choice(list_number)

   for operators in operator:
      user_fisrt_number = int(input("enter thhe first number: "))
      user_operator = input("enter the operator that would you like: ")
      print(f"the second number is {get_number}")
      second_number_random = get_number

      if user_operator != operators:
            print("please enter the valid operator")

      if user_operator == "+":
          add = user_fisrt_number + second_number_random
          print(add)
      elif user_operator == "-":
         subtration = user_fisrt_number - second_number_random
         print(subtration)
      elif user_operator == "*":
          multiplication = user_fisrt_number * second_number_random
          print(multiplication)
      elif user_fisrt_number == "/":
          division = user_fisrt_number / second_number_random
          print(division)
    


while True:
   user_permission = str(input("would you like to play?: y/n (for yes and no): "))

   if not user_permission:
      print("please enter a y or n!")

   else:
      for i in range(1, 4):
         print(i)
         time.sleep(1)
      print("lets start")
      funtion_game()
      
      

      

      
      



