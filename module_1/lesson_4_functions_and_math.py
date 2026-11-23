# Module 1, Lesson 4: Functions and the math module

import math as m
# Exercise 1: Functional calculator
# Write add, subtract, divide and multiply functions, then use them in a calculator program.

def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def division(a,b):
    return a/b
def multiplication(a,b):
    return a*b
function = input("1.Addition\n2.Subtraction\n3.Division\n4.Multiplication\nEnter the process you would like to do : ")
if function == "1":
    num1 = int(input("Enter the first number to add : "))
    num2 = int(input("Enter the second number to add : "))
    print(addition(num1,num2))
elif function == "2":
    num1 = int(input("Enter the first number to subtract : "))
    num2 = int(input("Enter the second number to subtract : "))
    print(subtraction(num1,num2))
elif function == "3":
    num1 = int(input("Enter the first number to divide : "))
    num2 = int(input("Enter the second number to divide : "))
    print(division(num1,num2))
elif function == "4":
    num1 = int(input("Enter the first number to multiply : "))
    num2 = int(input("Enter the second number to multiply : "))
    print(multiplication(num1,num2))
else:
    print("Invalid input")

# Exercise 2: Modular calculator
# Write power, ceiling, floor and factorial functions using the math module.

def power(a,b):
    return m.pow(a,b)
def ceiling(a):
    return m.ceil(a)
def floor(a):
    return m.floor(a)
def factorial(a):
    return m.factorial(a)
function = input("1.Power\n2.Ceiling\n3.Floor\n4.Factorial\nEnter the process you would like to do : ")
if function == "1":
    print("Power")
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    print(power(num1,num2))
elif function == "2":
    print("Ceiling")
    num1 = int(input("Enter the first number : "))
    print(ceiling(num1))
elif function == "3":
    print("Floor")
    num1 = int(input("Enter the first number : "))
    print(floor(num1))
elif function == "4":
    print("Factorial")
    num1 = int(input("Enter the first number : "))
    
    print(factorial(num1))
else:
    print("Invalid input")
