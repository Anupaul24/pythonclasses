import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,4,6,7],[4,3,7,9]])
for i in a:
    print(i)
print("shape of array a:- ",a.shape) 
s=0
for i in a:
    for j in i:
        s=s+j
print("sum of array a:- ",s)    
print("\n")
s=0   
b= np.array([[4,5,6,7],[3,4,5,6],[7,8,9,10],[9,3,4,5]])
for j in b:
    print(j)
for j in np.nditer(b):
    s=s+j
print("sum of array b :-",s)
print("size of array b:- ",a.size)

print("position of element 10 in array b:- ",np.where(b==10)) 
print("\n")
print("sorted array b:")
print(np.sort(b))
print("\n")
print("sum of two arrays a and b:")
print(np.add(a,b)) 
print(np.multiply(a,b))
s=0
arr=np.concatenate((a,b))
for i in np.nditer(arr):
    s=s+i
print(s)    

        
    