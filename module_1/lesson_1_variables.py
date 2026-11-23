# Module 1, Lesson 1: Variables and basic data types

# Exercise 1: Your first variable
# Assign a number to random_number and print it.

random_number = 33
print(random_number)

# Exercise 2: Mission to Mars
# Create variables of each data type (str, int, float, bool, list, dict) for a mission report.

astronaut_name = "Bob"
astronaut_age = 33
fuel = 43.2
is_engine_running = True
astronauts = ["Bob", "Alice", "Charlie"]
astronaut_ages = {"Bob": 33, "Alice": 25, "Charlie": 22}

print(astronaut_name, astronaut_age, fuel, is_engine_running, astronauts, astronaut_ages)

# Exercise 3: Space resource calculations
# Calculate distance, fuel consumed and time to destination.
# Distance = Speed x Time
# Fuel consumed = Distance / Fuel efficiency
# Time = Distance / Speed

travel_time = 10
speed = 5000
fuel_efficiency = 10
first_name = "Sally"
last_name = "Ride"

total_distance = speed * travel_time
fuel_consumed = total_distance / fuel_efficiency
total_time = total_distance / speed
full_name = first_name + " " + last_name

print("Total Distance", total_distance)
print("Fuel Consumed", fuel_consumed)
print("Total Time", total_time)
print("Full Name", full_name)
