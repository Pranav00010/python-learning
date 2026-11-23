# Module 1, Lesson 3: Loops and control flow

# Exercise 1: Loops and celestial object luminosities
# Print each celestial body with a for loop, store the luminosities in a list, then use a
# while loop and a conditional to print every luminosity below 200 solar units.
# Expected output for the while loop: 25, 6e-05, 100

celestialBodyLuminosity = {
    "Sirius" : 25, 
    "Andromeda Galaxy" : 1000000, 
    "Jupiter" : 0.00006,
    "Pleiades" : 100,
    "Orion Nebula" : 10000
    }

for obj in celestialBodyLuminosity.items():
    print(obj[0] + ":", obj[1], "solar units")

luminosities = []
for obj in celestialBodyLuminosity.items():
    luminosities.append(obj[1])
index = 0
while index < len(luminosities):
    if luminosities[index] < 200:
        print(luminosities[index])
    index = index+1

    
# Exercise 2: Mission control flow
# Use a while loop that runs while mission_time <= mission_duration. Each loop, reduce the
# distance and fuel, print the mission time, fuel level and distance, and break if either
# reaches 0 or below. Add one to mission_time each loop.

mission_duration = 10  # Duration of the mission in hours
fuel_level = 1000  # Initial fuel level in gallons
distance_to_destination = 500000  # Distance to the destination in kilometers
mission_time = 0  # Initialize mission time
fuel_consumption_rate = 50  # gallons per hour 
distance_traveled_per_hour = 50000  # kilometers per hour

while mission_time <= mission_duration:
    distance_to_destination -= distance_traveled_per_hour
    fuel_level -= fuel_consumption_rate
    print("The mission time is :",mission_time,"Hours")
    print("The fuel level is :",fuel_level,"gallons")
    print("The distance to destination is :",distance_to_destination,"Km\n")
    if fuel_level <= 0 or distance_to_destination <= 0:
        break
    mission_time += 1
print("Mission complete")
