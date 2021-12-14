"""
dictinaries are mappings
mappings are a collection of objects that are stored by a key unlike a sequence that stored objects by their relative position
a python dictionaty consists of a key and then an associated value.
"""

#dictioanry syntax
#dictname={"key":"value","key1":"value 1"...}

#empty dictionary
data={}
data3=dict()
print(type(data))

data2={"monitors":28,"keyboard":27,"mouse":27}
#how to access items in a dict syntax
#dictname['key']

print(data2["keyboard"])
print(data2["monitors"])

#create new items through assgnment
data2["cpu"]=28
print(data2)

data2["vga"]=28
print(data2)
data2["class"]=6
print(data2)

my_dict={'key1':123,'key2':[12,23,33],'key3':['item0','item1','item3']}
print(my_dict)
print(my_dict["key2"][1])
print(my_dict['key3'] [1])
li=my_dict['key3']
print(li)
print(li[1])
print(my_dict['key3'][0].upper())
print(my_dict['key2'][2]-15)

#updating dictionary value
my_dict["key1"]=150
print(my_dict)

#deleting a single value in the dict
del my_dict["key3"]
print(my_dict)

#deleting all the items in the dict

#nested dictinary
d={"key1":{"nestkey":{"subnestkey":"value"}}}
print(d["key1"]["nestkey"]["subnestkey"])
#dict function
print(len(d))

result=str(d)
print(type(result))

#dict method

#my_dict.clear()
#print(my_dict)

my_dict2=my_dict.copy()
print(my_dict2)

#display keys only
print(my_dict2.keys())

#dict values
print(my_dict2.values())

#dict items
print(my_dict2.items())

ages={"henry":18,"telvin":23}
print(ages.get("henry"))