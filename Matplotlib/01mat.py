#matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.

import matplotlib.pyplot as plt

plt.plot([2, 4, 6, 4])
plt.ylabel('Numbers')#y axis label
plt.xlabel('Indices')#x axis label
plt.title('Simple Plot')#title of the plot
plt.show()#show the plot
#grid 
plt.plot([1,2,3,4],[1,4,9,16])
plt.xlabel('Numbers')
plt.ylabel('Squares')
plt.grid()#grid on
plt.show()
