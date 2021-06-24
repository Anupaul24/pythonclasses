
number = int(input("enter integer value:- "))
flag=0
if number < 1:
     print("invalid number")
elif number == 1:
     print(number,"is a prime number")
elif number > 1:    
    for i in range(2,number-1):
      if number%i == 0:
        flag=1
        break;
    if flag:       
       print(number,"is not a prime number")
    else:
      print(number,"is a prime number")

# for i in range(1,11):
    # for j in range(1,11):
       # print(j*i, end= " ")
    # print("\n")
    #
# for i in range(1,11):
     # print(i*2, end=" ")
# print("\n")              
# for i in range(1,11):
     # print(i*3, end=" ")           
# print("\n")          
# for i in range(1,11):
     # print(i*4, end=" ")           
# print("\n")
# for i in range(1,11):
     # print(i*5, end=" ")           
# print("\n")
# for i in range(1,11):
     # print(i*6, end=" ")           
# print("\n")
# for i in range(1,11):
     # print(i*7, end=" ")           
# print("\n")
# for i in range(1,11):
     # print(i*8, end=" ")           
# print("\n")
# for i in range(1,11):
     # print(i*9, end=" ")           
# print("\n")
# for i in range(1,11):
     # print(i*10, end=" ")           
# print("\n")


