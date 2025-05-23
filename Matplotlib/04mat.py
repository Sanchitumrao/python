import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[1,8,27,64]
plt.plot(x,y,linewidth=4)#thickness of the line
plt.xlabel('Numbers')
plt.ylabel('Cubes')
plt.show()

#2 line plot
x1=[1,2,3,4]
y1=[1,4,9,16]
x2=[1,2,3,4]
y2=[2,4,6,8]
lines=plt.plot(x1,y1,x2,y2)
#use keyword arguments to set the properties of the lines
plt.setp(lines[0],color='r',linewidth=2.0,linestyle ='--')#red dashed line
#or Matlab style string value pairs
plt.setp(lines[1],'color','g','linewidth',2.0)#green solid line
plt.grid()
plt.show()