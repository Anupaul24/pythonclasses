"""
num = int(input("enter the integer value"))
a = 0
b = 1
if num<1:
    print("Invalid number")
else:
      print("Fabnoci series of ",num,"is" ) 
      print(a)
      print(b)
      for i in range(2,num):
        c = a + b  
        a = b 
        b = c 
        print(c)      
"""

"""
num = int(input("enter the number"))
for i in range(1,num+1):
    for j in range(i,num+1):
     print("*\n")
"""
#num = int(input("enter the number"))
arr= {}
print("Table")
for i in range(1,11):
    arr[i] = 1*i   
print(arr)
for i in range(1,11):
    arr[i]= 2*i
print(arr)
for i in range(1,11):
    arr[i]= 3*i
print(arr) 
for i in range(1,11):
    arr[i]= 4*i
print(arr) 
for i in range(1,11):
    arr[i]= 5*i
print(arr) 
for i in range(1,11):
    arr[i]= 6*i
print(arr) 
for i in range(1,11):
    arr[i]= 7*i
print(arr)
for i in range(1,11):
    arr[i]= 8*i
print(arr) 
for i in range(1,11):
    arr[i]= 9*i
print(arr) 
for i in range(1,11):
    arr[i]= 10*i
print(arr) 
"""
num = int(input("enter the the number"))
fact =1
if num <0:
    print("Invalid number")
elif num ==0:
    print("Factorial of ",num, "is:=",1)
else:
    i=1
    while(i<num+1):
         fact= fact*i
         i+= 1
    print("Factorial of ",num, "is:=",fact)      
        
num = int(input("enter the the number"))
i=1
while(i<11):
    n = num*i
    print(num,"*",i,"=",n)
    i+= 1

   
def findarea(r):
    pi= 3.14
    area = pi* r* r
    return area
num =int(input("enter the number"))
print("Area of Circle is :=",findarea(num))

num =int(input("enter the number"))
flag=0
if num<0:
    print("invalid number")
elif num== 1:
    print(num,"is prime number")
elif num >1:
     i=2
     while(i<=n/2):
         if num % i== 0:
            flag=1 
            break
            i+= 1
if flag:
    print(num,"not a prime number")
else:    
    print(num,"is prime number")
           
"""  
        
            
      
    
    
     
     
        