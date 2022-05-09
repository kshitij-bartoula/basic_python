# tuple is a collection data type of python programming language
#tuple is ordered,allows duplicate but is immuteble i.e cannot altered
#or add contents once created

thistuple=("apple","orange","banana")
print(thistuple)

#we can access tuple by slicing or from index

print(thistuple[1:])

#but to add,update or remove items we need to convert tuple to list and after
#adding,updating or removing back to tuple

y=list(thistuple)
print(y)
y[0]="kiwi"
thistuple=tuple(y)
print(thistuple)

#we can unpack tuple

fruits=("grapes","dragon","pineapple")
(green,red,yellow)=fruits
print(green)
print(yellow)

#for loop and while loop are similar to list


#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found
