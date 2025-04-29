import keyword
from tkinter import Variable

print(keyword.kwlist)

# Variable variable_name= variable_value

age = 94
age = 64
print(age)

# Type of Variable

age = 14  # int
pi = 3.14  # decimal
name = "Satyajit"  # str

# Rules for the Identifier/variable_name

_name = "Rajat"
_ = 56
print(_name)
print(_)

_ = 24
_ = _ + 20
print(_)

# Type
myage = 30
_Income = 1.2
Gender = "Male"

print(type(myage))
print(type(_Income))
print(type(Gender))

complex_number = 2 + 3j
print(complex_number.imag)
print(complex_number.real)

# Dynamically Typed (In Python we can convert the data type at runtime that python is Dynamically typed lang)


age = 35
print(type(age))
age = "Rajat"
print(type(age))
age = True
print(type(age))

Long_Variable_Name_Satyajit = "Rajat"
print(Long_Variable_Name_Satyajit)

# BODMAS
a = 10 + 20 * 30 - 1
print(a)

# Multiple Variable

a, b, c = 10, 20, 30
print(a)
print(b)
print(c)
print(a,b,c,sep="| ")

# To Find max number

result =max(10,30)
print(result)

result =min(10,30)
print(result)
