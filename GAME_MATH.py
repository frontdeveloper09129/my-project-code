#arithmetic operator 

#additon
#adding number to a value of variables
#you can also the a substarctiob, multiplication, and so on
#exp:
quantity = 20
quantity = quantity + 20
#but i can also do (quantity += 20) that also will be the same result
print(quantity)


#another exp:
#multipication
price = 150
quantity2 = int(input("how many pizza did you buy? :"))
total = price * quantity2
print(f"the total of your bill is: {total}")


#modulos:
value = 8
value %= 3
print(value)



#/
x = 3.14
y = -4
z = 5

#In Python, round() is a built-in function that rounds a number to the nearest whole number or to a specified number of decimal places.
result2 = round(x)

#abs() in Python gives you the absolute value of a number — which means it makes the number positive.
#So no matter if the number is negative or positive, abs() always returns a positive value.
result3 = abs(y)

#pow() in Python is used to raise a number to a power (do exponents).
result4 = pow(4, 3)

print(result2)
print(result3)
print(result4)


#max() finds the biggest (highest) value from a list of numbers or values.

x1 = 2
y1 = 3
z1 = 4

result5 = max(x1, y1, z1)
print(result5)
#output: 4

#max() is not only for integers, like lets say string
#when you use max() in string always the last will be print
string = ["apple", "cherry", "mango"]
print(max(string))


string1 = "hello"
print(max(string1))



#min() min() is the opposite of max().
#It finds the smallest (lowest) value.

x2 = 1
y2 = 2
z2 = 3

result6 = min(x2, y2, z2)
print(result6)

