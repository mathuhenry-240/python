import re


""""
RE -is a special sequence of character that forms a search partern 
"""

#searching for a pattern  use - .search("pattern",object)

sentence = "this is python programming"

found = re.search("python",sentence)
#print(found)
if found:
    print("we have a match")

else:
    print("no match")

#find all matching patterns  .findall(pattern,object)

s2 = "we all love to code. code is amazing"

found = re.findall("code",s2)
print(found)

#split a string at every whitespace   .split

s3 = "we are now at regular expressions"
list=re.split(" \s",s3)
print(list)

#replace/substitute a string with another

s4="this is android class"
result=re.sub("android","python",s4)
print(result)


""""
special characters
 
 \Axxx - returns a match if a string starts with given characters "xxx"
 
  \babc - returns a amtch if specifed char are at the begining or at the end of a word
   \B returns a match if ispecified char are present but not at the begining or at the end eg  \bci
   
    \d returns match for digits (0-9) -  \d
    
 \D returns matc if str does not contain digit
 
  \s match space
  
   \S match no space 
   
   
 \w reurn match of word characters(a-Z,0-9,_)
 
 \W  returns a match where str does not have word char

 \zxxx returns match if specified char are at the end of a string
"""
s5="The wonder..."
x = re.findall("\AThe",s5)
print(x)

s6="iam 101 years old"
x=re.findall("\d",s6)
print(x)


"""
SETS - a group of chars given inside a pair of square brackets
[abc] - returns match if any ofspecified char is found
[a-n] - returns match for lowercase a to n

[^abc] - match any other char other than a,b,c

[0123] - 
[0-9] - 
[0-5][0-9] - match a 2 digit no btwn 00-59
[a-zA-Z] match any lowercase or upper case char

[\d+]

"""

s7="the article was awesome"
match = re.findall("[abc]",s7)
print(match)

#match object methods
#.span() - returns a tupple of stsrt and end of match
#.string() - returns a string passed into search function
#.group() - returns part of string where match was found


s8="traverse the iterable. i do not know"
match = re.search("[v]",s8)
print(match)
print(match.group())