a=50
b=20

def function1(l,m):
    return(l+m)
x=function1(a,b)
print(x)

#if number of arguments are unknown then add * before parrameter name in func

def func2(*numbers):
    return(numbers[0]*numbers[3])
y=func2(2,4,5,10,50)
print(y)

dict1={"name":"hellome","age":45,
       "loc":"pokhara","phone":989898,"email":"gg@gmail.com"}
def function3(**key):
    return(key["name"]+":"+key["loc"])
f=function3(name="hellome",age=45,loc="pokhara",phone=989898)
print(f)


