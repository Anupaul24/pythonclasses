import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints)
# plt.grid()
# plt.show()
# from matplotlib import pyplot as pp
# pp.plot([2,4,6,8,9],[1,3,7,2,5])
# pp.show()
cars={"Carname" : ["bmw","vovo","uv","vw","ford","vw","tesla","bmw","volvo","ford","toyota","vw","toyota"],
   "Color": ["red","black","gray","white","white","white","red","black","gray","white","gray","white","blue"],
   "Age": [5,7,8,7,2,17,2,9,4,11,12,9,6,],
   "Speed": [99,86,87,88,111,86,103,87,94,78,77,85,86],
   "Autopass": ["Y","Y","N","Y","Y","Y","Y","Y","N","N","N","N","Y"]
    }
n=np.array(cars["Speed"])
plt.plot(n,marker="o")
plt.xlabel("Speed")
plt.grid()
plt.show()

# s=np.array([1,3,5,7,8])
# plt.bar(xpoints,ypoints)
# plt.pie(s)
# plt.show()