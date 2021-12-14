"""
Arithmetic operators -+ * // / % **
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators

"""
# comparison/relational ioperators
# == != > < >= <=
#they usually return a true or false value
print(1==1)

#logical operator
# and or not
#also return true or false
print(1==1 and 2==3)
#and returns true if all the conditions are true

#or returns true if either or all the conditions are true
print(1==1 or 2==3)

#not used to negate to return the opposite
print(not True)

#Assignment operator
# = += -= *=  /= **= //=%=

x=3
ans=x
ans += 4 #or ans=x+4
print(ans)
y=6
ans=y
ans -=2
print(ans)

#bitwise operators
# | - binary or & - binary and ^binary xor >> << ~
print(500 | 200)

#membership operators - in not in
print('o' in 'python')
print('o' not in 'python')

#identity operator
#used to compare memory location of two objects --is is not
list1=[1,3,4]
list2=list1
print(list1 is list2)