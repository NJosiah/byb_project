# The following variables will be converted into different data types

num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

# num1 will be converted from a float into an integer using int()
# Python will cut off the decimal and will get the integer value 99
print(int(num1))

# num2 will be converted from a integer to a float using float()
# Python will add the decimal and we will get the float value 23.0
print(float(num2))

# num3 will be converted from an integer to a string using str()
# Python will add quotations marks around the number to signify it is now a string value
a = str(num3)
print(a)

# string1 will be converted from a string into an integer using int()
# Python will remove the quotation marks and will leave the integer value
print(int(string1))