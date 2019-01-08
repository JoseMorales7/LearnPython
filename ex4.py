#This creates a variable called cars that has a value of 100
cars = 100
#This creates a variable called space_in_a_car that has a value of 4.0
space_in_a_car = 4.0
#This creates a variable called drivers that has a value of 30
drivers =  30
#This creates a variable called passengers that has a value of 90
passengers = 90
#This creates a variable called cars_not_driven that has a value of cars(100) - drivers(30)
cars_not_driven = cars - drivers
#This creates a variable called cars_driven that has a value of drivers(30)
cars_driven = drivers
#This creates a variable called carpool_capacity that has a value of cars_driven(70) * space_in_a_car(4.0)
carpool_capacity = cars_driven * space_in_a_car
#This creates a variable called average_passengers that has a value of passengers(90) / cars_driven(30)
average_passengers_per_car = passengers / cars_driven

#This prints out "there are" then the value of cars, then "cars available"
print("There are", cars, "cars available.")
#This prints out "there are only" then the value of drivers, then "drivers available"
print("There are only", drivers, "drivers available.")
#This prints out "there will be" then the value of cars_not_driven, then "empty cars available"
print("There will be", cars_not_driven, "empty cars today.")
#This prints out "we can transport" then the value of carpool_capacity, then "people today"
print("We can transport", carpool_capacity, "people today.")
#This prints out "We have" then the value of passengers, then "to carpool today"
print("We have", passengers, "to carpool today.")
#This prints out "We need to put about" then the value of average_passengers_per_car, then "in each car"
print("We need to put about", average_passengers_per_car, "in each car.")