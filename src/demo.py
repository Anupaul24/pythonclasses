import numpy
import statistics


l=[1,2,3,4,5]
x=numpy.median(l)
print(x)
cars={"Carname" : ["bmw","vovo","uv","vw","ford","vw","tesla","bmw","volvo","ford","toyota","vw","toyota"],
   "Color": ["red","black","gray","white","white","white","red","black","gray","white","gray","white","blue"],
   "Age": [5,7,8,7,2,17,2,9,4,11,12,9,6,],
   "Speed": [99,86,87,88,111,86,103,87,94,78,77,85,86],
   "Autopass": ["Y","Y","N","Y","Y","Y","Y","Y","N","N","N","N","Y"]
    }
y=cars["Age"]
y=sorted(y)
print(y)
x=numpy.median(y)
print("median of Age: ", x)
x=numpy.mean(y)
print("mean of Age: ",x)
x=statistics.mode(y)
print(x)
print("\n")
s=cars["Speed"]
s=sorted(s)
print(s)
x=numpy.median(s)
print("median of Speed :",x)
x=numpy.mean(s)
print("mean of Speed: ", x)
x=statistics.mode(s)
print(x)

# res={key :sorted(cars["Speed"]) 
# for key in sorted("Speed")}
# print(res)