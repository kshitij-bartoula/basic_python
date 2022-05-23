#count total numbers in a digit

number= "123456"
count=0
for i in number:
    count=count+1
print(count)

#print some pattern
n=5
k=5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end='')
    print()

#print list in reverse order using loop

list1=[10,20,30,40,50]
for i in range(1,len(list1)+1):
    print(list1[-i])

#display numbers from -10 to -1 using for loop
num=-10
while(num<0):
    print(num)
    num=num+1

#Use else block to display a message “Done” after successful execution of for loop
for i in range(5):
    print(i)
else:
    print("Done!")
#Write a program to display all prime numbers within a range
start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    # all prime numbers are greater than 1
    # if number is less than or equal to 1, it is not prime
    if num > 1:
        for i in range(2, num):
            # check for factors
            if (num % i) == 0:
                # not a prime number so break inner loop and
                # look for next number
                break
        else:
            print(num)


#display fibonacci series up to 10 terms
a=0
b=1
n=2
summ=0
print(a)
print(b)
while (n<10):
    summ=a+b
    print(summ)
    a=b
    b=summ
    n+=1

#Find the factorial of a given number
num = 5
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # run loop 5 times
    for i in range(1, num + 1):
        # multiply factorial by current number
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)

#Reverse a given integer number
num = 456786748
while(num>0):
    a = num%10
    print(a,end='')
    num=num//10

#Calculate the cube of all numbers from 1 to a given number
print("\n")
abc=10
for i in range(1,abc+1):
    print("the current number is: ",i,"and cube is ",i*i*i)

#Find the sum of the series upto n terms
n=5
num=2
sum=0
for i in range(1,6):
    print(num,end='+')
    sum+=num
    num=num*10+2
print("\n sum of above series is : ",sum)

#Print the pattern
count=0
for i in range(1,10):
    if(i<=5):
        print("*"*i)
    else:
        count=count+1
        print("*"*(i-2*count))

#first 10 natural numbers
i=1
while i<11:
    print(i)
    i=i+1

#pattern print

for r in range(1,6):
    for j in range(1,r+1):
        print(j,end='')
    print("\n")
    
#Calculate the sum of all numbers from 1 to a given number
sum=0
num=int(input("enter a num: "))
while num>0:
    sum=sum+num
    num=num-1
print("sum is: ",sum)

#Write a program to print multiplication table of a given number

mul_num=int(input("enter a num: "))
for i in range(1,11):
    print(i*mul_num)

#Display numbers from a list using loop dividible by 5,>150 skip,>500 stop
numbers = [12, 75, 150, 180, 145, 525, 50]
for x in numbers:
    if x%5==0 and x<=150:
        print(x)
    elif x>150 and x<500:
        continue
    elif x>500:
        break 
    else:
        pass
  

    
    
    
    
    
    
    
    
        
    
          
