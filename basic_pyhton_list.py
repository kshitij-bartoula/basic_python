# collection data types in the Python programming language:
#List is a collection which is ordered and changeable. Allows duplicate members.
list1=["apple","orange","mangoes","grapes","papaya"]
print(list1)
print(len(list1))
print(type(list1))
thislist=list(("apple","banana")) #list constructor
print(thislist)
print(list1[3])
print(list1[-1])
print(list1[1:3])
print(list1[::-1])

if "apple" in list1:
    print("yes,apple is present in list1")

for i in list1:   #loop through items
    print(i)

for i in range(len(list1)):   #loop through index number
    print(i)

while i<len(list1):   #looping through while
    print(list1[i])
    i=i+1
    
list1.insert(2,"coconut")
print(list1)

thislist.append("cherry")
print(thislist)

newlist=[]
newlist.extend(list1)
print(newlist)

thistuple=("kiwi","dragonffruit")
newlist.extend(thistuple)
print(newlist)

newlist.remove("apple")
print(newlist)

del newlist[0]
print(newlist)

del newlist

thislist.clear()

print(thislist)
print(list1)


#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list



