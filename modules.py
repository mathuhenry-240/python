"""
modules is a python file containing a group of related functions that can be reused.
built-in modules
    -os module
    -random
    -math module#

user-defined module

loading modules
1.using the import statement
     eg import module1 module 2 modue n
2.using from...import statement
e.g from modulename import functional
"""
"""
#using import
import math  #import all the functions in the math modu



#using imported module
#sytanx
        #modulename.function name()

print(math.factorial(5))
print(math.log(100,10))
"""
# #import specific module required

from math import factorial, sqrt
print(factorial(5))
print(sqrt(121))

import time


#getting current time
print(time.ctime())

for i in range(0,6):
    print(i)
   # time.sleep(1)  #print element after 2sec


import datetime

print(datetime.datetime.now())

import calendar
print(calendar.month(2020,2))

print(calendar.prcal(2021))

#IRERATOR - OBJECT THAT CONTAINS COUNTABLE
#no of values

#__iter__() - used to create an iterator object
fruits = ("apple","pineapple","passion")
myit = iter(fruits)
print(type(myit))

print(next(myit))
print(next(myit))

#__next__() - points to the next iterator object



#json - javascript object notation

import json

#convert from json to python - json.loads
#json data
data = '{"name":"dan","age":"30","city":"nairobi"}'
#print(type(data))
python_data = json.load(data)
print(type(python_data))

#convert python to json

json_data = json.dumps(python_data)
print(type(json_data))
print(json_data)





