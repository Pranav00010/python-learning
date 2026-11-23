# Module 1, Lesson 2: Typecasting, lists and user input

# Exercise 1: Having fun with typecasts
# Typecast fuelRemaining to an int and oxygenLevels to a float, then print them like this:
# Fuel Remaining: 33 L
# Oxygen Levels: 21.0 kPa

fuelRemaining = 33.0
oxygenLevels = 21
intFuelRemaining = int(fuelRemaining)
floatOxygenLevels = float(oxygenLevels)
print("Fuel Remaining:",intFuelRemaining,"L")
print("Oxygen Levels:", floatOxygenLevels,"kPa")

# Exercise 2: Array manipulation
# Using the values list, in order: delete the last item, set the second element to 8,
# flip the list, append 5 and 9, then print it.
# Expected output: [4,3,8,1,5,9]

values = [1, 2, 3, 4, 5]
values.pop()
values[1] = 8
values.reverse()
values.append(5)
values.append(9)
print(values)

# Exercise 3: Rocket engine performance calculator
# Ask the user for thrust and propellant mass flow rate (as floats), then calculate
# and print the specific impulse and exhaust velocity.
# Specific Impulse = Thrust / (Mass Flow Rate * 9.81)
# Exhaust Velocity = Specific Impulse * 9.81

thrust = float(input("Enter the thrust : "))
massFlowRate = float(input("Enter the mass flow rate of the propellent : "))
specificImpulse = thrust/(massFlowRate*9.81)
exhaustVelocity = specificImpulse * 9.81
print("specific impulse "+str(specificImpulse)) 
print("exhaust velocity "+str(exhaustVelocity))
