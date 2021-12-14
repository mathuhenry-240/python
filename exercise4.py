#write a function that checks if a number is even
num=int(input("Enter a number :"))
if (num % 2) == 0 :
    print("{0} is even number".format(num))

else :
    print("{0} is odd number".format(num))


##write a function that checks if a number is odd



#write a function that takes a list , names and
#print those names one by one


count ={}
count[(1,2,4)] = 5
count[(4,2,1)] = 7
count[(1,2)] = 6
count[(4,2,1)] = 2
tot = 0
for i in count:
    tot = tot + count[i]

print(len(count)+tot)

