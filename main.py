import numpy as np 
import matplotlib.pyplot as plt 

f = open('values.txt', 'r') #opens up and reads the file
f.readline()
x = []
y = []

for line in f: #puts the values into lists
  x.append(float(line.split('\t')[1]))
  y.append(float(line.split('\t')[0]))


plt.plot(x,y) #plots a graph
plt.scatter(x,y) #plots the individual points
plt.title('velocity(km/h) as a function of the radius(kpc)')
plt.xlabel('radius(kpc)')
plt.ylabel('velocity(km/h)')
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x))) #draws a line of best fit
plt.show()

