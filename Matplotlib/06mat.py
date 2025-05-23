import matplotlib.pyplot as plt
import numpy as np
# muliple figures
plt.figure(1)
plt.subplot(211)
plt.plot([1,2,3,4],[1,8,27,64],'r')
plt.xlabel('Numbers')
plt.ylabel('Cubes')
plt.subplot(212)
plt.plot([1,2,3,4],[1,4,9,16],'b')
plt.xlabel('Numbers')
plt.ylabel('Squares')

plt.figure(2)
# plt.subplot(211)
plt.plot(np.sin(np.arange(0.0, 10, 0.1)),'r')
plt.show()