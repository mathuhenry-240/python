#tuples a comma sepparated sequence of values
#tuple are immutable

#create an empty tuple
tuplname=()
#create a tupple
tupl1=(1,2,3,4,5)
print(type(tupl1))

tupa=("me")
tupb=("you",)
print(type(tupa))
print(type(tupb))

t=("ban",[1,2,3,4])
print(type(t))
 #access tuple items
print(t[0])
print(t[1][1])

t2=(1,2,3,4,5,6)
print(t2[::-1])
#concatination

print(tupl1+t2)
#delete
del t2
#find the length
print(len(tupl1))

#tuiple repetation
print(tupb*2)