import calendar
#function - is a block of code or nmed grup of statement that do a specific task
#def.functionname(parameters-/aruments)
"""
two categories f functions
1.build in function
str(),print(),int(),float(),type(),srt(),log(),abs()

2.user defined function
syntax
def functionname():
    block of code...

    def functionname(parameters/aruments)
        block of cde...

"""

"""def printhello():
    print('hello world')

    #calling the printhello function
printhello()

def printsum():
    print(4+5)
printsum()

def greeting():
    name = input("Enter your name:")
    print(f"hello,{name}")
greeting()
print("results for greeting 2")
def greetings2():
    name = input("Enter your name:")
    return f"hello,{name}"
print(greetings2())

def square():
    x = int(input("Enter a num:"))
    return 
print(square())"""

# def greet(name,age):
#     return f"hi, my name is {name} and iam {age} tears old"
# print(greet('mark',29))
#
# def number(product):
#
#     x=int(input('enter number'))
#     y=int(input('enter number'))
#     z=int(input('enter number'))
#
#     return f"The product of x,y,z is {x*y*z}"
# #print(number('product'))
#
# #x,y,z=input("enterx,y,z:").split(",")
# #print(f"x is{x},y is{y} and z is{z}")
#
# """
# key words arguments - these ae named arguments where names of args re treated s
# key words and matched during function call and definition.
# """
#
# def messageto(name,message):
#     return f"{message}. from{name}"
# #print(messageto(message="you in a scandle?",name="Echesa"))
#
# """
# 3.default args - allow uus to initialize args in functio definition such tha if the initialised arg is not provided in function call then function uses te default value
#
# """
#
# def printdata(name,age=40):
#     return f"my name is {name} and iam {age} yrs old"
# #print(printdata("ruto",34))
# #print(printdata("ruto"))
#
# """
# 4.variable length args - these are args that you are not surre how many they will be in the function definiton
#
# type of variable length args
# 1. *args
# 2. **keyword args
# """
#
# def printnames(*names):
#     print(type(names))
#     for name in names:
#         print(name)
# printnames("henry", "mathu", "jeff")
#
#
# def printdetils(**data):
#     print(type(data))
#     for name, age in data.items():
#         print(f"{name}-> {age}")
# printdetils(name="hausa",age=45)
#
# def listnames(**marks):
#     for name,mark in marks.items():
#         print(f"{name} scored {mark} marks")
#
# listnames(telvin=329,olivia=290)
#
#
# """
# variable scope
# this is location within a program where a valiable can be accessed
# types of variable scope
#     1.global valiable scope - vriables defined outside a function
#
#     2.local variables scope -vriables defined inside a function
#     3.enclosed
#     4.built-in
#
# """
# x=20 #global variable
# def square():
# #    x=10 #local variable
#     global x
#     return x*x
# print(square())
#
# a=10
# def log():
#     x=10
#     return x*x
# print(log())
#
# def scope():
#     a=5
#     def enclosed():
#         b=6  #enclosed
#
# #lambda function
# #sytanx
# #lambda args : expression
#
# def add2no(x,y):
#     return x+y
#
# ans=lambda x,y:x+y
# print(ans(2,4))
#
# def table(n):
#     return lambda a:a*n
#
# n=int(input("enter a number"))
# b=table(n)
# for i in range(1,11):
#     print(n,"x",i,"=",b(i))



y=int(input("Enter year:"))
m=int(input("Enter month: "))
print(calendar.month(y,m))

