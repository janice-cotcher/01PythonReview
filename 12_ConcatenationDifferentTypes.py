# the following with cause a type errror
room = 146
message = "We'll meet in room "
print(message + room)

# correct print message
print(message + str(room))

# we can also convert floats to strings
light = 3e8
print("The speed of light is " + str(light) + "m/s")

# I will receive an TypeError message if I try to add these values
num1 = "23" # Python reads any numbers in quotation marks as a string
num2 = 23 # Python reads any number without a decimal as an int
print(num1 + num2)

# correct print message
print(int(num1) + num2) # num1 is now an int

# we can aslo convert string to floats
x = 45
y = "-9.9"
print(x * float(y))

# Converting a string into a number only works if there is only a number
# contained in the string. The code will produce a ValueError because Python
# cannot figure out which part of the string is the number.
light = "3e8 m/s"
frequency = "10e-10 m"
wavelength = float(light) / float(frequency)
print(wavelength)