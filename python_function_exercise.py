#create function in python
def add_num(x,y):
    return (x+y)
y=add_num(5,8)
print(y)

#Create a function with variable length of arguments
def func1(*args):
    print(*args)
func1(20,40,60)
func1(48,67)

#Return multiple values from a function
def calculation(a,b):
    return(a+b,a-b)
res=calculation(40,10)
print(res)
print(type(res))

#Create a function with default argument
def show_employee(namee,salaryy=9000):
    print("the name of emp is",namee,"and salary is",salaryy)
show_employee("kshitij",14000)
show_employee("ben")

#Create an inner function to calculate the addition in the following way
def outer_add(a,b):
    def inner_add(x,y):
        return(x+y)
    z=inner_add(a,b)
    return(z+5)
x=outer_add(4,5)
print(x)

#Create a recursive function
def add_till(num):
    if num:
        return num+ add_till(num-1)
    else:
        return 0
res=add_till(10)
print(res)

#Generate a Python list of all the even numbers between 4 to 30
print(list(range(4, 30, 2)))

    


