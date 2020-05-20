# python print() statement
_cars = 23
cars = 24
CARS = 25

number_of_cars = 23
kind_of_cars = 'Ferrari'

print(cars)
print(_cars)
print(CARS)
print(number_of_cars)
print(kind_of_cars)

"""
This is a multiline comment
You can use this kind of comment to 
make longer notes
"""

name = "Janelle"
type_of_car = "Rolls Joyce"
school = "Foundation Elementary School"

print(name + " " + school)

#python string.format
print("{} works at {}".format(name, school))

def addition():
    a = int(input("enter a number"))
    b = int(input("enter another number"))
    print(a+b)

addition()

