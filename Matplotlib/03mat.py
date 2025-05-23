import matplotlib.pyplot as plt
import numpy as np
t=np.arange(0.0, 5.0, 0.2)#this creates an array of numbers from 0 to 5 with a step of 0.2
plt.plot(t, t**2, 'b--', label='^2')#blue dashed line
plt.plot(t, t**2.2, 'rs',label='^2.2')#red squares)
plt.plot(t, t**2.5, 'g^', label='^2.5')#green triangles
plt.grid()
plt.legend()#add legend based on the line labels
plt.show()