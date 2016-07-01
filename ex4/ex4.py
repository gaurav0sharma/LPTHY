cars = 100
space_in_a_car = 4.0
driver = 30
passenger = 90
cars_not_driven =  cars - driver
cars_driven = driver
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passenger / cars_driven


print "cars", cars
print "space in car" , space_in_a_car
print "drivers",driver
print "passanger",passenger
print "cars_not_driven",cars_not_driven
print "cars_driven",cars_driven
print "carpool_capacity",carpool_capacity
print "average_passangers_per_car",average_passengers_per_car

print "hey %s there" % "you"
