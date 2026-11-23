# Module 2, Lesson 2: Pandas Series and DataFrames

import numpy as np
import pandas as pd
# Practice examples from the lesson
data = np.array([10, 20, 30, 40, 50])
series = pd.Series(data)
print("Series from NumPy array:")
print(series.values)

data = {'Name': ['John', 'Emma', 'Peter'],
        'Age': [30, 25, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)
df['Gender'] = ['Male', 'Female', 'Male']
filtered_df = df[df['Age'] > 25] 
df['Age'] = df['Age'].apply(lambda x: x + 1)
print(df['Age']+1)

# Exercise 1: Planetary analysis with pandas
# Make a Series of planet distances from the Sun (million km) and a DataFrame of moon data.
# Planets: closest and furthest planet, Mars's distance, average distance, planets over 1000 million km.
# Moons: moons over 3000 km diameter, largest diameter, smallest orbital period, mean diameter.

import pandas as pd
import numpy as np

planet_distances = {
    'Mercury': 57.9,
    'Venus': 108.2,
    'Earth': 149.6,
    'Mars': 227.9,
    'Jupiter': 778.6,
    'Saturn': 1433.5,
    'Uranus': 2872.5,
    'Neptune': 4495.1,
    'Pluto': 5906.4
}

moon_data = {
    'Planet': ['Jupiter', 'Jupiter', 'Saturn', 'Saturn', 'Uranus', 'Neptune'],
    'Moon': ['Io', 'Ganymede', 'Titan', 'Rhea', 'Titania', 'Triton'],
    'Diameter (km)': [3642, 5262, 5150, 1528, 1578, 2707],
    'Orbital Period (days)': [1.77, 7.15, 15.95, 4.52, 8.71, 5.88]
}

seriesPlanetDistances = pd.Series(planet_distances)
print(seriesPlanetDistances)
dfMoonData = pd.DataFrame(moon_data)
print(dfMoonData,"\n")

closestDistanceToSun = seriesPlanetDistances.min()
closest = seriesPlanetDistances[seriesPlanetDistances == closestDistanceToSun]
closestPlanetToSun = closest.index[0]

print("The planet closest to the sun is",closestPlanetToSun,"with a distance of",closestDistanceToSun)

distanceToMars = seriesPlanetDistances.loc["Mars"]
print("The distance to Mars is",distanceToMars)

sumOfDistances = seriesPlanetDistances.sum()
averageDistance = sumOfDistances/len(seriesPlanetDistances)
print("The average distance of all planets from the sun is",averageDistance)

print("Planets that are further than 1000 million km are \n"+str(seriesPlanetDistances[seriesPlanetDistances > 1000]))
print("Data of moons with a diameter greater than 3000km :\n"+str(dfMoonData[dfMoonData['Diameter (km)'] > 3000]))

largestMoonDiameter = dfMoonData["Diameter (km)"].max()
print("The largest Moon diameter is",largestMoonDiameter)

smallestOrbitalPeriod = dfMoonData["Orbital Period (days)"].min()
print("The smallest orbital period in days is",smallestOrbitalPeriod)

print("The mean moon diameter is",dfMoonData["Diameter (km)"].mean())

print(seriesPlanetDistances.loc["Mars"])

# Exercise 2: Deeper dive into the SpaceX launch dataset
# Load the dataset, view the first rows with head(), print the "Customer Country" column and its
# unique values, group by country, print launches with payload mass under 4000 kg, and print the
# median payload mass for the United States.

SpaceXCSVLink = "https://raw.githubusercontent.com/BriantOliveira/SpaceX-Dataset/master/dataset/SpaceX-Missions.csv"
launchesDataset = pd.read_csv(SpaceXCSVLink)

print(launchesDataset.head())
print(" ")
print(launchesDataset["Customer Country"])
print(" ")
print(pd.unique(launchesDataset["Customer Country"]))
print(" ")
launchesByCountry = launchesDataset.groupby("Customer Country")
print(launchesDataset[launchesDataset["Payload Mass (kg)"] < 4000])
print(" ")
medianlaunchesByCountry = launchesByCountry["Payload Mass (kg)"].median()
print(medianlaunchesByCountry["United States"])
