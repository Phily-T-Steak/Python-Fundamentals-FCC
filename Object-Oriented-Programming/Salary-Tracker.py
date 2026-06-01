#key take away from this workshop is properties/setters make normal-looking attribute access secretly run methods
#here we are creating the class we are using for this workshop where we are working on the use of getters and setters
class Employee:
    #we are creating this dictionary to act as our reference point for some of the changes we will be making with our setters later on
    _base_salaries = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000,
    }
    
    #__init__ runs automatically when a new object is created from the class and is used to initialize the object's starting attributes/state
    def __init__(self, name, level):
        #normally we would directly assign the input parameter to an object attribute like name and asign that to self.name however since we have setters in this code we are actually calling on the setter here and running this through like its a new_name
        #this line passes the temporary input parameter into the name setter, because of the setter we created python redirects to "def name(self, new_name)" with the use of the setter, so new_name = the name we got fromm the object and runs through the setter
        self.name = name
        #same process as self.name but with the use of the level setter instead
        #this does NOT directly create self._level, it first calls the level setter, which performs validation before eventually storing the value in self._level
        self.level = level
        #with this one we are looking at the class, then the dictionary, then the value assocaited with the level (key) provided in the creation of the object to asign it a salary (value) from our dictionary
        #use the employee's level as the key to look up the matching salary from the class dictionary
        #after the look up is complete this follows the same process as self.name and self.level and we run that value through the salary setter we made in this class (this creates a cascading effect because changing the level also triggers salary-related logic automatically)
        self.salary = Employee._base_salaries[level]

    #here we are setting up our __str__ special method for the class so that when we use print() on the object we get our standardized format
    def __str__(self):
        return f'{self.name}: {self.level}'

    #here we are setting up our __repr__ special method which functions similarly to the __str__ special method. This is more focused on the "programer" side of the code where __str__ is more geared towards the "user" side of the code
    #__repr__ is ideally written so it returns a string that could recreate the object if entered back into Python code, ex: Class(input parameter, input parameter)
    def __repr__(self):
        return f"Employee('{self.name}', '{self.level}')"

    #here we are creating our first getter with the use of the @property decorator. @property allows a method to be accessed like a normal attribute instead of needing parentheses like a regular method, ex: class.method instead of class.method()
    #create a property that allows controlled access to _name. properties allow Python to intercept attribute access and assignment so validation or additional logic can run automatically
    @property
    def name(self):
        #we are using _name because this is meant to be a hidden value that is for internal use base on the _ convention
        return self._name

    #here we are creating our first setter with the use of the @property.setter decorator
    @name.setter
    def name(self, new_name):
        #validation to make sure the entered new_name is a string value otherwise raise an error
        if not isinstance(new_name, str):
            raise TypeError("'name' must be a string.")
        #updating the hidden value with the new_name assuming it passes validation
        self._name = new_name
        #documenting that the update happened with the new value
        print(f"'name' updated to '{self.name}'.")

    #here we are creating our second getter with the use of the @property decorator
    @property
    def level(self):
        #we are using _level because this is meant to be a hidden value that is for internal use base on the _ convention
        return self._level

    #here we are creating our second setter with the use of the @property.setter decorator
    @level.setter
    def level(self, new_level):
        #validation to make sure the entered new_level is a string value otherwise raise an error
        if not isinstance(new_level, str):
            raise TypeError("'level' must be a string.")
        #validation used to compare the new_level to the levels (keys) in the dictionary we created at the start of this class
        if new_level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{new_level}' for 'level' attribute.")
        #validation to check if the new_level is the same as the current level of the object. Need to use hasattr() to verify that the _level of the object already exist otherwise python will throw an error before it can check
        if hasattr(self, '_level') and new_level == self.level:
            raise ValueError(f"'{self.level}' is already the selected level.")
        #validation to make sure the new_level's salary (value from the key) is grater than the current level's salary (value from the key) otherwise it with raise an error. Again used hasattr() to verify that the variable exists so python doesn throw an error
        if hasattr(self, '_level') and Employee._base_salaries[new_level] < Employee._base_salaries[self.level]:
            raise ValueError("Cannot change to lower level.")
        #assuming the new_level passes all validations we show that it has been updated with this print() function
        print(f"'{self.name}' promoted to '{new_level}'.")
        #once the new_level has passed validations we update the salary based on its key:value pair in the dictionary we made at the start of this class
        #this intentionally calls the salary setter so salary validation logic is reused instead of bypassed
        self.salary = Employee._base_salaries[new_level]
        #last but not least we then update the objects level to the new_level after it passes all validations
        self._level = new_level

    #here we are creating our third getter with the use of the @property decorator
    @property
    def salary(self):
        #we are using _salary because this is meant to be a hidden value that is for internal use base on the _ convention
        return self._salary

    #here we are creating our third setter with the use of the @property.setter decorator
    @salary.setter
    def salary(self, new_salary):
        #validation to make sure the entered new_salary is an integer or a float value (since it has to be a number) otherwise raise an error
        if not isinstance(new_salary, (int, float)):
            raise TypeError("'salary' must be a number.")
        #validation that makes sure the new_salary is not below the minimum allowed salary for the employee's current level, otherwise it raises an error. Again using hasattr() to ensure the variable exisits before validating to avoid python throwing an error for trying to look at something that isnt there
        if hasattr(self, '_level') and new_salary < Employee._base_salaries[self.level]:
            raise ValueError(f'Salary must be higher than minimum salary ${Employee._base_salaries[self.level]}.')
        #after passing all validations update the objects salary value with this new salary value
        self._salary = new_salary
        #using a print() function to show that the update has happened sucessfully
        print(f'Salary updated to ${self.salary}.')

#testing of the code that was just made by creating an object
charlie_brown = Employee('Charlie Brown', 'trainee')
#testing out the use of the __str__ special method
print(charlie_brown)
#testing out the use of the third getter for salary
print(f'Base salary: ${charlie_brown.salary}')
#testing of the second setter for level and its cascading effects
charlie_brown.level = 'junior'