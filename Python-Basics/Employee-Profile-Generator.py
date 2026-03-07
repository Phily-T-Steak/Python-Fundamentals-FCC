#this lab was concentrating on adding and using string along with some slicing/extracting values out of strings
#inital variables
first_name = 'John'
last_name = 'Doe'
#here we are adding string together, we add in the ' ' so that the string dont squish together
full_name = first_name + ' ' + last_name

#here we are showing that you can add to existing variables with the use of +=. In the case of this string it just extends the string
address = '123 Main Street'
address += ', Apartment 4B'

#variable in the form of an integer
employee_age = 28
#here we are showing that you can add an integer to a series of strings by converting that varaible using the str()
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)

#variable in the form of an integer
experience_years = 5
#we are doing the same thing as mentioned above by using the str()
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

#variables created for this next example
position = 'Data Analyst'
salary = 75000
#here we are using the f' ' to be able to add varaibles to a string regardless of their typing by using {}
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)

#string variable created for this next slicing example
employee_code = 'DEV-2026-JD-001'
#here we are slicing the first 3 character to get our new department variable (0 based system)
department = employee_code[0:3]
print(department)
#here we are slicing again to extract the "year" from our orginal variable (doesnt include the last number in the 0 based system)
year_code = employee_code[4:8]
print(year_code)
#here we are slicing again to extract the initals
initials = employee_code[9:11]
print(initials)
#here we are slicing by using a negative number which allows us to work backwards rather than determining how many characters in we are
last_three = employee_code[-3:]
print(last_three)