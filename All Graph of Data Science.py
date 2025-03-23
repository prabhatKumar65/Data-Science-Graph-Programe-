import matplotlib.pyplot as plt
#Creating Simple Plot
x=[10,20,30,40,50,60]
y=[20,30,40,50,60,70]
plt.plot(y,x)
plt.title('❤❤Simple Plot Created❤❤')
plt.ylabel('❤X-axis❤')
plt.xlabel('❤Y-axis❤')
plt.show()
#Creating Simple Histogram For Practice
x=[1,2,3,4,5,6,7,8]
y=[1,2,3,4,5,6,7,10]
plt.hist(x,y)
plt.title('❤❤Simple Histogram❤❤')
plt.xlabel('❤X-axis❤')
plt.ylabel('❤Y-axis❤')
plt.show()
#Creating Simple Scatter Plot
P=[5,8,1,4,2,3,4,5,3,2,5,5,7,6,3,4,4,1,5]
K=[2,4,5,4,2,5,7,5,8,6,1,4,5,3,4,5,6,8,4]
plt.scatter(P,K)
plt.title('❤❤Simple Scatter❤❤')
plt.xlabel('❤X-axis❤')
plt.ylabel('❤Y-axis❤')
plt.show()
#Creating Simple Pie Chart 
import matplotlib.pyplot as plt
import numpy as np
x=np.array([80,120,140,200])
mylabel=['❤❣‍Banana❤❣‍','❤❣‍Mango❤❣‍','❤❣‍Lichi❤❣‍','❤❣‍Graps❤❣‍']
plt.pie(x,labels=mylabel)
plt.title('❤❣‍Pia Chart❤❣‍')
plt.show()

