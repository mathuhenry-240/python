"""
#conditional statements/if sttements
1.if
2.if...else
3.if...elif...else

allow you to make a program do something only if a given condition is True
"""

#if statement syntax
#if condition:
  #  code executed if conditin is true....
score=75
if score>50:
    print("above averange")



#if...elif statement syntax:
#if condition:
    #code executed if condition is true
#else
  #code executed if condition is false
if score < 50:
    print("above averange")
else:
    print("below averange")

username="Testuser"
password="pass123"

form_username=input("usernme:")
form_password=input("password:")

if username==form_username and password==form_password:
    print("logged in successfully")
else:
    print("wrong username or password")


#if...elif...else statements syntax:
#if condition1:
 #   code to execute if cndition is true
#elif condition2:
 #   code excute if condition2 is true
 #elif condition2:
  #  code excute if condition2 is trueelif condition2:
   # code excute if condition2 is true
    #......
#else:
 #   code to be executed if all conditions fail

marks=int(input("enter your marks:"))
if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
elif marks>=60:
    print("Grade c")
elif marks>=50:
    print("Grade D")
elif marks>=40:
    print("Grade E")
else:
    print("you failed. try again")