def user_info(name, age=0, city="Tucson"):
    ''' This function prints name, age, and city
      from an argument provided to the function'''
    print("{} is {} years old, from {}.".format(name, age, city))

user_info("Janet", 58, "Oklahoma City")

#error if you dont specify the right amount of arguments
#user_info(34, "New York")

#using default arguments values
user_info("Micah")

#you can change the order of the arguments by specifying their names
user_info(age=56,name="Kadeem")
