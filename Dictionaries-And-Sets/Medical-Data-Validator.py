#In this workshop, you'll validate a set of medical data to ensure that it complies with a set of rules. Not the biggest fan initally of how this was strucutred since I have grown acustom to keeping all in 1 line but I can see how this can be benifical
#Here we are importing the pythong standard library re to be called later on for the use of "regular expressions"
import re
#here is the working list [] set up which is made up of 4 dictionaries {keys: values} acting as our data set for this lab
medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]

#here is the first def that we set up which will be called later on in this code. this was created earlier in the code so that we can reference it later down the line
# this is set up to review all of the keys found in a given dictionary and evaluate all of their associated values. Not the biggest fan of how this code is structered but its cool to see that its an option I guess
def find_invalid_records(
    patient_id, age, gender, diagnosis, medications, last_visit_id
):
    #here is what we are using to verify the values of the keys found in the dictionaries. This results in a true or false state based on if the value is found to be correct or incorrect.
    constraints = {
        #for patient_id we are checking that the value is a string and then using the regular expressions library to see if there if a full match 
        #its stats with p regardless of upper or lower case and that there are numbers that follow with the use of the \d+
        'patient_id': isinstance(patient_id, str)
        and re.fullmatch('p\d+', patient_id, re.IGNORECASE),
        #verifying that the age value is an integer and that is greater than or equal to 18
        'age': isinstance(age, int) and age >= 18,
        #verifying that the gender value is a string and that its specified as male or female
        #using gender.lower() here to help verify that its male or female so we can ignore the casing. Same thing as using re.IGNORECASE
        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),
        #verifying that the value of diagnosis is a string or have None entered
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,
        #verifying that the value of medications is written as a list and that all instantances found in the list are string values
        'medications': isinstance(medications, list)
        and all([isinstance(i, str) for i in medications]),
        #verifing that the value of last_visit_id is presented as a string value and that there is a full match using the regular expressions
        # also ignore the upper or lower case values while checking that it has numbers that follow with the use of \d+
        'last_visit_id': isinstance(last_visit_id, str)
        and re.fullmatch('v\d+', last_visit_id, re.IGNORECASE)
    }
    #This is being used to return the keys where the validation fails(gives a false value) when looking at the .items() aka the keys & values found in constraints
    return [key for key, value in constraints.items() if not value]

#here is the second def that is being used to sort out the data from the main list
def validate(data):
    #verifying that what is being used in this def is in fact a list or tuple (list in our case)
    is_sequence = isinstance(data, (list, tuple))
    #if the inital check is not true then print and retun a false value
    if not is_sequence:
        print('Invalid format: expected a list or tuple.')
        return False
    
    #here we are creating a varaible to be used later but initally setting it to the false state    
    is_invalid = False
    #here we are creating another varaible to be used later but making this a set(). This is done because sets ignore order and compare membership (aka do the keys match exactly regardless of order)
    key_set = set(
        ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
    )

    #this is the first for loop used to iterate across the inital list (in our case medical_records) and break it up so that each item in the list is indexed
    for index, dictionary in enumerate(data):
        
        #using an if statement to capture the edge case of not having the items being iterated through as dictionaries using the "dict" syntax
        if not isinstance(dictionary, dict):
            #if the statement reads true then printing the following and calling our where in the list this issue is using the f' string with our variable {index} and setting the newly created variable is_invalid to true
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            #the continue is being used to say that if this read true you can skip the rest of the for loop here and go onto the next iteration
            #this is useful to help the program from not crashing
            continue
        
        #here we are using another if statemnet to verify that the keys found in the dictionary variable created from the for loop has the proper keys by compairing that set to the set we created earlier (key_set)
        if set(dictionary.keys()) != key_set:
            #assuming this reads true then it prints the following error message citing what dictionary and at what index this error occured followed by setting the is_invalid to true
            #not the biggest fan of how this code is strucutred but its cool to see that its an option I suppose
            print(
                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
            )
            is_invalid = True
            #the continue is being used to say that if this read true you can skip the rest of the for loop here and go onto the next iteration
            #this is useful to help the program from not crashing
            continue
        
        #here is where we are using that first def function on the dictionary variable we iterated through in this def. We are using the ** to unpack the dictionary typing to see the variables (this is considered keyword argument unpacking)
        invalid_records = find_invalid_records(**dictionary)
        
        #this is nested for loop inside of our first for loop to pull the keys out of the invalid records found by the first def written in this code
        for key in invalid_records:
            #the value of this dictionary is being assigned to the key that we are itterating through with this nested for loop (this is done through something called dictionary indexing)
            value = dictionary[key]
            #this print function is being used to showcase what key/value is in the wrong formating as well as its location. Here we are calling in the two variables key and value from this for loop but also pulling in the index variable from the previous for loop
            print(f"Unexpected format '{key}: {value}' at position {index}.")
            #assuming that something is found with the wrong formate it sets the is_invalid variable to true    
            is_invalid = True  

    #this is acting as a global error flag (did we dectet ANY errors during validation?). If one was detected then this reads true which would mean the dataset is invalid
    if is_invalid:
        return False
    
    #assuming no errors where found print the following and return true
    print('Valid format.')
    return True

#this is the actual running of the test to verify that the records provided actually meet all of the standards put in place
validate(medical_records)