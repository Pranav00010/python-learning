# Module 2, Lesson 1: NumPy arrays

# Exercise 1: Spacecraft telemetry modeling with NumPy arrays
# Create time (0 to 100 s) and altitude (100 m per second) arrays, then calculate velocity
# and acceleration (9.81 m/s^2) arrays. Print the shape and data type of each array.

import numpy as np

constantAcceleration = 9.81

timeInSeconds = np.arange(0,101,1)
print(timeInSeconds)

altitudeInMeters = timeInSeconds * 100
print(altitudeInMeters)

velocity = altitudeInMeters[1:]/timeInSeconds[1:]
print(velocity,)

acceleration = np.full(timeInSeconds.shape, constantAcceleration)
print(acceleration)

print("The shape of the timeInSeconds array is",timeInSeconds.shape)
print("The shape of the altitudeInMeters array is",altitudeInMeters.shape)
print("The shape of the velocity array is",velocity.shape)
print("The shape of the acceleration array is",acceleration.shape,"\n")

print("The data type of the timeInSeconds array is",timeInSeconds.dtype)
print("The data type of the altitudeInMeters array is",altitudeInMeters.dtype)
print("The data type of the velocity array is",velocity.dtype)
print("The data type of the acceleration array is",acceleration.dtype)

# Exercise 2: Mission profiling
# Generate 1000 random altitude, velocity and acceleration values, slice out subsets, find the
# critical points (altitude > 5000 m, velocity > 300 m/s, acceleration < -9.8 m/s^2),
# and concatenate them into one array.

import numpy as np
np.set_printoptions(suppress=True) #Makes sure standard form is not used in the data

altitude = np.random.rand(1000)*10000
velocity = np.random.rand(1000)*1000
acceleration = np.random.randn(1000)*20

criticalAltitude = altitude[np.where(altitude > 5000)]
criticalVelocity = velocity[np.where(velocity > 300)]
criticalAcceleration = acceleration[np.where(acceleration<-9.8)]

criticalPoints = np.concatenate((criticalAltitude,criticalVelocity,criticalAcceleration))
print(criticalPoints)

firstTenAltitude = altitude[:10]
print(firstTenAltitude)
lastFiveVelocities = velocity[-5:]
print(lastFiveVelocities)
everyHunderedthAcceleration = acceleration[::100]
print(everyHunderedthAcceleration)

print("The length of critical Altitude array :",len(criticalAltitude))
print("The length of critical velocity array :",len(criticalVelocity))
print("The length of critical acceleration array :",len(criticalAcceleration))
