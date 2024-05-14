import matplotlib.pyplot as plt 
import numpy as np 

x = np.arange(1,6)
y = np.arange(2,11,2)

fgr = plt.figure()

axes1 = fgr.add_axes([0.1,0.1,0.8,0.8])
axes2 = fgr.add_axes([0.2,0.5,0.3,0.3])

axes2.plot(x,y)
axes2.set_xlabel("inner X")
axes2.set_ylabel("inner y")
axes2.set_title("inner graph")


axes1.plot(y,x)
axes1.set_xlabel("outer X")
axes1.set_ylabel("outer y")
axes1.set_title("outer graph")
plt.show()

