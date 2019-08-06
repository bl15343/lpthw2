cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers,"drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car." 

# Study drill questions
# 0. car_pool_capacity was not defined; the variable does not exist
# 1. 4.0 for space_in_a_car is necessary if you want the actual floating point 
# average for average_passengers_per_car. It's nonsensical in the realistic sense
# as you cannot transport half a person
# 2. Floating point is an integer number with a fractional component expressed
# after a decimal (assuming base10) point
# 3. Skipping
# 4. Yep
# 5. Remembered
# 6. Skipping
