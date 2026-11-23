# Module 2, Lesson 3: Plotting with Matplotlib and NumPy

import matplotlib.pyplot as plt
import math
import numpy as np
from mpl_toolkits.mplot3d import axes3d

# Example: Standard graph
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x,y, color = "green", linestyle = "--", marker = "o", markersize = 5)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Standard graph")
plt.show()

# Exercise 1: Plotting Supernova Brightness
# Plot brightness against time as a purple dashed line with "o" markers.
# Label the x-axis "Time", the y-axis "Brightness" and the title "Brightness of Supernova".
time_points = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Time points
brightness = [10, 30, 80, 140, 120, 100, 80, 60, 30, 10, 8]  # Brightness measurements
plt.plot(time_points, brightness, color = "purple", linestyle = "--", marker = "o", markersize = 7)
plt.xlabel("Time")
plt.ylabel("Brightness")
plt.title("Brightness of Supernova")
plt.show()

#Excercise 2: Plot a graph of the sine and cosine functions
x = np.linspace(0, 2*math.pi, 100)
y = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y)
plt.plot(x,y2)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Sin Curve")
plt.grid(True)
plt.show()

# Excercise 3: plot the function f(x) = sin(√(x² + y²)) in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

X = np.linspace(-5,5,100)
Y = np.linspace(-5,5,100)
X,Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))
ax.plot_surface(X, Y, Z, cmap = "viridis")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D surface plot")
plt.show()

# Exercise 4: Plotting Mathematical Functions
# Plot a tan function, then tan and cos together, each with a title, axis labels and a grid.
# Use 50 evenly spaced x values from 0 to 2*pi.
x = np.linspace(0, 2*math.pi, 50)
y = np.tan(x)
y2 = np.cos(x)
plt.plot(x,y, color = "red")
plt.plot(x,y2, color = "green")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Plot of Tan and cos functions")
plt.grid(True)
plt.show()
