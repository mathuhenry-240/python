##sets
#sets are an unordered collection of *unique*elements
#we construct them using set() function

#empty set

set1=set()
print(type(set1))

#add items in a set
set1.add(1)
print(set1)
set1.add(2)
print(set1)

set1.add(1)
print(set1)

set1.add("henry")
print(set1)

l=[1,2,1,1,1,1,3,2,42,2,3,2,3,4]
print(set(l))

#a boolean is data type that has two predefined values,True and False
#although it comes with a place holder None

isAProgrammer=None
isLoggedIn=True
"""
all values are considered "truthy" :except
none
False
0
0.0
0j
decimal(0)
0/1(fraction)
[]
()
""
{}
set()
range(0)
"""