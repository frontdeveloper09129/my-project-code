input_1 = input("enter your operator: ")
input_2 = int(input("enter the number that would you like to add: "))
input_3 = int(input("enter the number again: "))

if input_1 == "+":
    result = input_2 + input_3
    print(result)
elif input_1 == "-":
    result = input_2 - input_3
    print(result)
elif input_1 == "*":
    result = input_2 * input_3
    print(result)
elif input_1 == "/":
    result = input_2 / input_3
    print(result)
elif input_1 == "%":
    result = input_1 % input_2
    print(result)
else:
    print("invalid")

