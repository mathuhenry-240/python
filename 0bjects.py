"""
oop - obbject oriented programming

An objecct represents an entity in real world that can be be distinctly identified
an object has 1. unique identity eg ssn,id no
               2.state/properties/attributes eg data field like radius of a circle
               3.behaviour represented by methods eg getarea() of a circle


method is a special kind of a function that is defined in a class


CLASSES
A CLASS is a user defined prototype of an object. that defines a set of attributes nd behavior that characterize an object.
AN OBJECT is an instance of a class
          is an entity that has state and behaviour
AN INSTANCE is an individual class.


A CLASS VARIABLE is a var that is shared by all instances of a class.

AN INSTANCE VARIABLE/DATA MEMBER
def1  is a var that is specific to a particular instance of a class
def2  is a variable that holds data associted with class and its objects

INSTANTIATION is creating of an instance of a class

FUNCTION  OVERLOADING
    Assignment of more than one behavior to a function

OPERATOR OVERLOADING
    assignment of more than one functionality to a particular operator

INHERITANCE
    transfer of the characteristics of one class to another
    defining/creating  new class from existing class


POLYMORPHISM  is a way of implementing same functionality in different ways
poly - many
morphs - forms

ENCAPSULATION - is restriction of access to methods and attributes

DATA ABSTRACTION - is hiding of internal details and show only the functionality



CRETING A CLASS
def __init__(self,[args])
    #class attribute
    self.attribute=something
sytanx:
class classname:
'''
    optional docstring
'''
initialiser
    class attributes
methods/class suite

"""
import math
class circle:
    """implement finding area and perimeter of a circle"""
    #class variables here
    def __init__(self,radius):
        #instance attributes/data members
        self.radius=radius

    def getperimeter(self):
        return 2*math.pi*self.radius

    def getarea(self):
        return math.pi*self.radius**2

#constructing objects from class/instantiation
#syntax:
#objectvariable = nameofclass([args])

circle1=circle(6)
print(type(circle1))

#Accessing attribute
#objectname.attribute
print(circle1.radius)

#Accessing the methods
#objectname.methodname()

print(f"The perimeter of the circle is {circle1.getperimeter()}")

print(f"The area of the circle is {circle1.getarea()}")

#create a class rectangle with height and width as class attribute
#write methods get area and get perimiter of the rectangle
#create two instances of class rectangle printing perimiter and area of each


class rectangle:
    def __init__(self,height,width): #parameterised
        self.height = height
        self.width = width

    def getperimeter(self):
        return 2*(self.height + self.width)

    def getarea(self):
        return self.height * self.width


rectangle1 = rectangle(8,9)
rectangle2 = rectangle(6,7)

print(rectangle1.width)
print(rectangle1.height)

print(rectangle2.width)
print(rectangle2.height)

print(f"The perimeter of Rectangle1 is {rectangle1.getperimeter()}")
print(f"The area of Rectangle is 1{rectangle1.getarea()}")
print(f"The perimeter of Rectangle2 is {rectangle2.getperimeter()}")
print(f"The area of Rectangle2 is {rectangle2.getarea()}")


#calculate the area of a triangle and its perimeter
class triangle:
     def __init__(self,height,base):
         self.height=height
         self.base=base

     def getarea(self):
         return 1/2 * self.height * self.base

triangle1=triangle(5,6)
triangle2=triangle(7,8)

print(triangle1.height)
print(triangle1.base)
print(triangle2.height)
print(triangle2.base)


print(f"The area of  triangle1 is {triangle1.getarea()}")
print(f"The area of  triangle2 is {triangle2.getarea()}")

 #calcularing area of a trapezium

class trapezium:
    def __init__(self,height,a,b):
        self.height=height
        self.a=a
        self.b=b
    def getarea(self):
        return 1/2*(self.a+self.b)*self.height
trapezium1=trapezium(3,4,5)

print(trapezium1.height)
print(trapezium1.a)
print(trapezium1.b)

print(f"Area of trapezium is {trapezium1.getarea()}")
"""
def main():
    r=eval(input("Enter radius:"))
    circle33=circle(r)
    print(format(circle33.getarea(),'.2f'))

main()
"""
#example 2
class employee:
    #class variable
    paid = True
    count=0
    #constructor/init - special function used to initialize th
    #instancemember of the class
    def __init__(self,id,name):
        #isinstance variables/class attributes
        self.id=id
        self.name=name
        employee.count=employee.count+1

    def display(self):
        print(f"id : {self.id} name : {self.name}")

emp1 = employee(10,"john")
emp1.display()
emp2 = employee(12,"dan")
emp2.display()
emp3 = employee(11,"jaden")
emp3.display()
print(f"{employee.count} employees")


"""
builtin class function
    1.getattr(obj,name,default)- used to access attribute of an object
    2.setattr(obj,name,value) - used to set a pparticular value to the specific attribute of an object
    3.delattr(obj,name) - sed to delete a specific attribute
    4.hasattr(obj,name) - used to return True if the obj has some specific attribute
"""
print(getattr(emp3,'id'))

#get te name of emp3
print(setattr(emp3,'name','sam'))

#check if emp3 hs attr id
print(hasattr(emp3,"id"))

#del attr id for emp3
print(delattr(emp3,"id"))

#check if emp3 hs id
#print(delattr(emp3,"id"))
"""
BUILTINATTRR
"""

class rectangle:
    color="green"
    def __init__(self,l=1,w=1):
        self.l=l
        self.w=w

    def getperimeter(self):
         return 2*(self.l+self.w)
    def getarea(self):
        return self.l*self.w

    def setl(self,l):
        self.l=l

    def setw(self,w):
        self.w=w

rect1=rectangle()
rect1.setl(10)  #setattr(l,10)
rect1.setw(15)  #setattr(w,15)
print(rect1.getarea())
print(rect1.getperimeter())
"""
builtin class attribute
1. __doc__ - contains class doc string
2.__dict__ -contains info about class name space
3.__class__ - contains class name
4.__module__ - contains the name of the file where the class is defined
5.__bases__ - contains a tupple of base classes
"""

print(emp3.__doc__)
print(rect1.__dict__)
print(rect1.__class__)
print(rect1.__module__)

#deleting an object
#del objectname
del rect1


#INHERITANCE SYNTAX
""""
parent/base class-class being inherited from
child/derived class-class inheriting from the parent class


class parent:
    pass
    
class child(parent1,parent2...parentN):
    pass
    
      
"""

class person:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname

    def printname(self):
        return f"{self.firstname} {self.lastname}"

class child(person): #single level inheritance
    pass
child1=child("Ethanmark","mathu")
print(child1.printname())

class animal:
    def speak(self):
        print("animal is speaking")


class dog(animal):
        def barks(self):
            print("dog is barking")

jimmy=dog()
jimmy.speak()
jimmy.barks()

class parent:
    #class attr
    age=100
    #class constructor
    def __init__(self):
        print("calling init method")

    def perentmethod(self):
        print("calling parentmethod")

    def setattr(self,age):
        parent.age=age

    def getattr(self):
        print(f"parent's age is {parent.age}")


class child2(parent):
    def __init__(self): #overridding parent init method
        print("calling child _init__")

    def childmethod(self):
        print("calling child method")


dan=child2() #instance of child class
dan.perentmethod()
dan.setattr(5)
dan.getattr()
dan.childmethod()


#MULTI LEVEL INHRITANCE
class A:
    pass

class B(A):
    pass
class C(B):
    pass
class D(C):
    pass

#multiple inheritance
class E(parent,person,rectangle):
    pass

#hierachical inheritance
class parent():
    pass
class child1(parent):
    pass
class child2(parent):
    pass

#HYBRID INHERITANCE
class parent():
    pass
class child(parent):
    pass
class child1(parent):
    pass
class child3(parent,child1):
    pass

class computer:
    def __init__(self,type="del",cost=67000):
        self.type=type
        self.cost=cost

    def getcost(self):
        return self.cost

class laptop(computer):
    def __init__(self,touchpad):
        super().__init__()
        self.touchpad=True
    def hastouchpad(self):
        return self.touchpad



