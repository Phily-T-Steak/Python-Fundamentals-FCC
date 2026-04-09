#Planet class made as the template/blueprint to create planet objects
#the general idea here is to take the input, validate the input, store it as object attributes
class Planet:
    #all classes start with a __init__ since this is the constructor method that runs when a new object is created
    def __init__ (self, name, planet_type, star):
        #created a for loop to iterate through the parameters of the object being created
        for var in (name,planet_type,star):
            #verifying that any given parameter is a string
            if not isinstance(var,str):
                raise TypeError("name, planet type, and star must be strings")
            #verifying that any given parameter is not a blank string (empty or a whitespace). Also using .strip to remove any strings that are just a space
            if var.strip() == "":
                raise ValueError("name, planet_type, and star must be non-empty strings")
        #storing the validated parameter as attributes of the object
        self.name = name
        self.planet_type = planet_type
        self.star = star
      
    #creating an instance method to describe what planet is orbiting around what star
    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'

    #creating a special method to define readable string representation of the object
    #called automatically when using print() or str() on an object
    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'

#creation of instances (objects) of the Planet class
planet_1 = Planet("earth","livable","sun")
planet_2 = Planet("mars","unlivable","sun")
planet_3 = Planet("planet x","unlivable","black hole")

#demonstrate that printing the object uses the __str__ method
#python automatically calls __str__ to convert the object into a string for printing
print(planet_1)
print(planet_2)
print(planet_3)

#demonstrate calling a regular method (orbit) on the object
#python only calls regular methods when explicitly invoked
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())