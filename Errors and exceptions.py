"""
ERRORS AND EXCEPTION
TYPES OF ERRORS
    1.syntax errors - caused by failure to follow syntax rules.
    2.logic errors - caused by wrong implementation of program logic.
    3.runtime errors - errors that occur during program execution.

 An exception is an error detected during program execution

 1.zero division error
 2.EOF error
 3.name error
 4.stop iteration error(loops)
 5.overflow error
 6.system exit error

 HANDLING EXEPTIONS
 1.TRY...EXCEPT BLOCK


 2.TRY...EXCEPT...ELSE ERROR

 try:
    code to try
except:
    code if error occurs

else:
    code if no error occurs


3.TRY...EXCEPT...FINALLY
try:
    code to try
except:
    code if error occurs

finally:
    code whether there errors or not

"""
#print("hello) #syntax errors
#print(name)
try:
    print(name)
except:
    print("whoops! looks like 'name' is not defined")

try:
    print(1/0)

except ZeroDivisionError:
    print("u can't divide a no by 0")

except IOError:
    print("something else went wrong")


try:
    a = int(input("Enter a number:"))

except ValueError:
    print("please enter a number")

else:
    print(a)
try:
    print(2/0)

except ZeroDivisionError as e:
    print(f"error occurred. {e}")

else:
    print("done")
"""
#raising an exception
if 1/0:
   # raise Exception("cant divide by zero")

#USER DEFINED EXCEPTION
#syntax
#class your error class(built-in error class):
 #   code here

#class NetworkError(RuntimeError):
 #   def __init__(self,arg):
#        self.args=arg


#try:
    #try code here
    raise NetworkError("bad host name")

#except:
    pass


#assertions - is a sanity check that you can turn on and off when you are done with your program

#syntax
#assert (Expression [args])
"""

def KelvinToFahreinheit(temp):
    assert (temp>=0),"colder than absolute zero"
    return (temp-273)*1.8+32
print(KelvinToFahreinheit(273))
print(KelvinToFahreinheit(-5))







