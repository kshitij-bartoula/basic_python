#sets are collection data types that are unordered,immutable and
#doesn't allow duplicate
thisset={"apple","mangoes","grapes","papaya"}
print(thisset)

#these are unordered i.e unindexed thus we cannot access set item by index
#to access set items
for x in thisset:
    print(x)

thatset={"a","b","c"}
newset=thisset.union(thatset)
#return new set from both set containing items removing duplicates  
print(newset)

set1={1,2,3}
thatset.update(set1)  #insert items of one set to another set
print(thatset)

set2={2,3,4,5,6}
set1.intersection_update(set2)#return set contain in both set
print(set1)

set2.symmetric_difference_update(set1) #
print(set2)


#add()	Adds an element to the set
#clear()	Removes all the elements from the set
#copy()	Returns a copy of the set
#difference()	Returns a set containing the difference between two or more sets
#difference_update()	Removes the items in this set that are also included in another, specified set
#discard()	Remove the specified item
#intersection()	Returns a set, that is the intersection of two other sets
#intersection_update()	Removes the items in this set that are not present in other, specified set(s)
#isdisjoint()	Returns whether two sets have a intersection or not
#issubset()	Returns whether another set contains this set or not
#issuperset()	Returns whether this set contains another set or not
#pop()	Removes an element from the set
#remove()	Removes the specified element
#symmetric_difference()	Returns a set with the symmetric differences of two sets
#symmetric_difference_update()	inserts the symmetric differences from this set and another
#union()	Return a set containing the union of sets
#update()	Update the set with the union of this set and others






