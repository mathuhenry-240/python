"""
loops
Aloop is a block of code to be executed repeatedly for as may times as a given condition is true.

types of loops
    1.while loop
    2.for loop
"""
#while loop syntax
#while (condition == true):
 #   code to execute

"""
number=50
while number<100:
    number=number+1
    print(number)"""

#loop control statements
   # 1.break - terminate a loop
   #2.continue - skip
   #3.pass

number=1
while number<10:
    number+=1
    if number==5:
        continue
       # break
    print(number)
else:
    print("loopsuccessfully completed")

print("second loop")

n=1
while n<5:
    print(f"count {n}")
    n+=1


#for loop
#for object in iterable
    #code

numbs=[1,2,3,4,5]
for i in numbs:
    print(i)

#loop through a tuple
tup=(1,2,3,4,5,6)
for t in tup:
    print(t)
#2nd tuple
tup2=("game time","lets go")
for z in tup2:
    print(z)

#loop through a string
name="django"
for n in name:
    print(n)

#loop through a dictionary
machine={"'subaru':26","'volvo':12","'toyota':65"}
for cars in machine:
    print(cars)
for key in dict.key:
    print(dict[key])