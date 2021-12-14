"""
strings-sequence of characters usually enclosed between single quotes or double quotes
"""
print("this is a string")
print('this is another string')
sentence='they  didn\'t like how she reacted'
sentence2="they  didn't like how she reacted"
print(sentence)
#escape sequence
sentence3="This is pytho\\n class.\n \twe are handling strings"
print(sentence3)
#use triple quote for sentenses spanning multiple lines
msg="""
This
is
an
example of a sentense spanning multiple lines
"""
print(msg)
msg2="""
This \ris an example of a sentense spanning multiple lines"""
print(msg2)
number=1
print(type(number))
number=2
print(type(number))
#string concatanation
print(1+1)
print(str(1) + "1")
print(1 + int("1"))

#string indexing
string="python"
print(string[0])
#slicing strings
print(string[2:])
#strings are immutable
#string[0]="j"
print(string[::2])


#string repetition
letter="p"
print(letter*5)
name="henry"
print(name*2)

#string methods
#sytanx stringname.method([parameters/args])
#upper()-convert a string to uppercase
str1="python"
print(str1.upper())
print(str1.lower())
print(str1.capitalize())

#count()-count occurences of a letter in a str
a="washroom"
print(a.count("o"))


#startswidth()-find if str starts with specified char
print(a.startswith("w"))

#endswidth()-find if str ends with specified char
print(a.endswith("w"))

#find()-returns the index of char specified
print(a.find("o"))

#other methods
#format()-performs string operation
language="python"
name="guido van rossum"
#i am guido van rossum and i invented python

print("i am {name} and i invented {language}".format(name="rasmus",language="rasmus"))

age=67
nickname='jd'
print("iam %s and iam %i years old" % (nickname, age))

print(f"iam {nickname} and iam {age} yrs old")

s='django'
#use indexing to print
print(s[0])
print(s[-1])
print(s[0:4])
print(s[1:4])
print(s)
print(s)
print(s.isalpha())
print(s.isalnum())
print(s[::-1])


l=[3,7,[1,4,'hello']]
print(l[2][2])
print(l)
l.reverse()
print(l)
#
print("-".join("1234"))
joiner="."
print(joiner.join("USA"))
nmm="."
print(nmm.join("henry"))
jina="+"
print(jina.join("henry" "mathu"))
#replacing strings(.replace(old,new)

s1="this is python programming. python python"
print(s1.replace("python","jyhton",1))
#removing chars in a string-split()
b="     python     "
print(b.split())
b1="this is a toy"
print(b1.split())
print(b1.split("i"))
print(len(b1))

print(bool(b1))

print(bool(""))

a="some"
b="more"
#i want some more
print(f"i want {a} {b}")


