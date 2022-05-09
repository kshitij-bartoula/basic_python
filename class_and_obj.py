class my_class():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def tax(self):
        x= 0.10*self.salary
        print(x)

y=my_class("hello",34,30000)
y.tax()
print(y.name)

#inheritance

class child_cls(my_class):
    def __init__(self,name,age,salary,address):
        super().__init__(name,age,salary)
        self.address=address

    def print_something(self):
        print("name:",self.name,"age:",self.age,"salary:",self.salary,
              "address:",self.address)

x=child_cls("kshitij",26,20000,"morang")
x.print_something()

