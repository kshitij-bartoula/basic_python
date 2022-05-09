thisdict={
    "employee_id":100,
    "emp_name":"shyam",
    "pos":"ASE",
    "salary":30000
    }
print(thisdict)
for i in thisdict:  #print keys name in dict one by one
    print(i)
print(thisdict["emp_name"])
x=thisdict["pos"] #get value
print(x)
y=thisdict.get("salary")#alt method to get val
print(y)

z=thisdict.keys()
print(z)

a=thisdict.values()
print(a)

b=thisdict.items()
print(b)

for i in thisdict:
    print(thisdict[i])

dict2=thisdict.copy()  # alt dict2=dict(thisdict)
print(dict2)

#Method	Description
#clear()	Removes all the elements from the dictionary
#copy()	Returns a copy of the dictionary
#fromkeys()	Returns a dictionary with the specified keys and value
#get()	Returns the value of the specified key
#items()	Returns a list containing a tuple for each key value pair
#keys()	Returns a list containing the dictionary's keys
#pop()	Removes the element with the specified key
#popitem()	Removes the last inserted key-value pair
#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update()	Updates the dictionary with the specified key-value pairs
#values()	Returns a list of all the values in the dictionary







