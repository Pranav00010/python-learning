# Module 1, Lesson 5: Writing to files

# Exercise 1: Saving orbital details
# Create a text file called orbital_details and write each planet's orbital details into it.

planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# Orbital periods (in Earth years)
orbital_periods = [0.24, 0.62, 1.0, 1.88, 11.86, 29.46, 84.01, 164.8]
# Axial tilts (in degrees)
axial_tilts = [0.03, 177.36, 23.44, 25.19, 3.13, 26.73, 82.23, 28.32]

file = open("orbital_details.txt", "w")
for i in range(len(planet_names)):
    file.write("Planet name : "+str(planet_names[i])+" , "+"Orbital period : "+str(orbital_periods[i])+" Years"+" , "+"Axial Tilt : "+str(axial_tilts[i])+" Degrees"+"\n")
file.close()
