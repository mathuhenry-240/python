####concatenation####
# names1=["daniel","moi","kiprotich"]
 #c_lists=names+names1
#>c_lists
#['henry', 'gifton', 'francis', 'daniel', 'moi', 'kiprotich']
#>c_list*2
  #  c_list*2
# c_lists*2
#['henry', 'gifton', 'francis', 'daniel', 'moi', 'kiprotich', 'henry', 'gifton', 'francis', 'daniel', 'moi', 'kiprotich']###


#list slicing(:)
numbers = [1,2,3,4,5,6,7,8]

#sytanx for slicing
   #listname[startindex:stopindex]

print(numbers[2:5])
#print list item from stsrt index to last item
#listname[start index:]
print(numbers[0:3])
print(numbers[5:7])
print(numbers[-4])
numbers=(54,55,56,57,58,59)
print(numbers[1:4])

#reasigning list items
numbers=[5,6,7,8,9]
#print list item from stop index to last item
#listname(numbers[:stopindex])
print(numbers)
print(numbers[2:])
print(numbers[:4])
print(numbers[:3])

#mutability
#listname[index]=nem value
numbers[2]=12
print(numbers)
numbers[0]=20
print(numbers)

#list methods
#listname.method(value)
fruits=['orange']
#add item at the end of the list
fruits.append('pineapple')
print(fruits)
fruits.append('passion fruit')
print(fruits)

#remove items from a list using a specified item
#fruits.pop(1)
print(fruits)

#remove items from the items using a specified value
fruits.remove('pineapple')
print(fruits)

#sorting list items
age = [24,22,56,27,30]
age.sort()
print(age)

#reverse the list
age.reverse()
print(age)

data=['grif','kelvin','dan','dan']
print(data)
data.append('henry')
data.append('mathu')
print(data)
data.pop(4)
print(data)
data.pop(1)
print(data)
data.sort()
print(data)

#add items at specified location
data.insert(1,'brand')
print(data)

#to count no of items in alist
print(data.count('dan'))

#extend add a number of elments at the end of the list
list1=[1,2,3,4]
list2=[5,6,7]
list1.extend(list2)
list3=list1
print(list1)
print(list3)

#create an independent copy of the list
list3=list1.copy()
list1[1]=14
print(list3)
print(list1)

#find index of an onject in a list
list3=[1,2,3,4,5]
x=list3.index(4)
print(x)

#remove all items from a list
list3.clear()
print(list3)
"""
  list method
  copy()
  pop()
  extend(iterable)
  sort()
  insert()
  count()
  append(x)
  clear()
  index()
  insert(i,x)
  remove(x)
"""
#list functions
#len()-used to return the no. of items in alist
list4=[1,2,3,4,5]
print(len(list4))
#listr()-convert a collection into a list
x=(3,5,7,9)
print(type(x))
y=list(x)
print(type(y))
#min()-returns smalllest value in an iterable
print(min(y))
#max()-returns largest value in an iterable
print(max(y))
#range-returns a range of numbers as a list
print(list(range(5)))
#range(start,stop[,step]
print(list(range(5,10)))
print(list(range(5,10,2)))
#del listname[i] delete list items at a particular index
del y[-1]
print(y)
#del listname-delete the list completely
del y
print(y)
