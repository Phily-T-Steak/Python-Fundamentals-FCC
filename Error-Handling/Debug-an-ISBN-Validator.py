##The ISBN (International Standard Book Number) is a unique identifier assigned to commercial books. It can be either 10 or 13 digits long, and the last digit is a check digit calculated from the other digits.
##Camperbot has tried to build their own ISBN validator. However, they have made a few mistakes along the way.
##In this lab, you will fix the existing code and make it function properly.
##anything with a ## are comments left by me anything with a # are comments placed in the lab ahead of time 

def validate_isbn(isbn, length):
    ##changing this to check just the length of the isbn rather than having it try to verify both the isbn and the length variables
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return
    ##here we are breaking up the isbn into 2 sections with slicing [start:end]
    ##we are saying the main digits are everything but the last value [:length-1] by slicing up to the last digit and excluding it
    ##while also saying the digit to check is the last value [length-1] by indexing
    main_digits = isbn[:length-1]
    given_check_digit = isbn[length-1]
    
    ##using a list comprehension which uses a for loop internally to populate the list from the desired variable (in this case into integers)    
    main_digits_list = [int(digit) for digit in main_digits]
    
    # Calculate the check digit from other digits
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)
    
    # Check if the given check digit matches with the calculated check digit
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')

def calculate_check_digit_10(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 9 digits by its corresponding weight (10 to 2) and sum up the results
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    # Find the remainder of dividing the sum by 11, then subtract it from 11
    result = 11 - digits_sum % 11
    # The calculation result can range from 1 to 11.
    # If the result is 11, use 0.
    # If the result is 10, use upper case X.
    # Use the value as it is for other numbers.
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def calculate_check_digit_13(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 12 digits by 1 and 3 alternately (starting with 1), and sum up the results
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    # Find the remainder of dividing the sum by 10, then subtract it from 10
    result = 10 - digits_sum % 10
    # The calculation result can range from 1 to 10.
    # If the result is 10, use 0.
    # Use the value as it is for other numbers.
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def main():
    ## due to not being about to actually type in the terminal I am commenting this line out and then using user_input = to whatever I would have typed out
    user_input = input('Enter ISBN and length: ')

    ##verify if there is a comma
    if ',' not in user_input:
        print("Enter comma-separated values.")
        ##when python hits the return it will immediately exit the function (stopping the code at this error)
        return
        
    ##split the inout into 2 values
    values = user_input.split(",")
    ##using the .strip() to remove any spaces found before or after these new values
    isbn = values[0].strip()  
    length = values[1].strip()
    
    ##validate length
    ##rather than using an if statement to validate the length as an interger Im using the new "try" and "except" logic learned in these past lessons
    ##try handles errors after they happen where an if statement prevents errors
    ##here we are trying to turn the length into an integer
    try:
        length = int(length)
    ##except catches an error and handles it here
    ##this is what will happen if the try fails
    except:
        print("Length must be a number.")
        ##when python hits the return it will immediately exit the function (stopping the code at this error)
        return

    ##validate isbn
    ##rather than using an if statement to validate the length as an interger Im using the new "try" and "except" logic learned in these past lessons
    ##this handles the ISBN-10 edge case where the last character can be 'X' (which represents 10)
    try:
        if length == 10:
            ##attempts to test everything except the last character into integers with the use of slicing [start:stop]
            ##this ensures the first 9 digits are valid numbers for ISBN-10
            int(isbn[:-1])
            ##this is saying if the last character is not 'X', attempt to convert it to an integer to ensure it is numeric like the rest
            if isbn[-1] != "X":
                int(isbn[-1])
        ##this handles ISBN-13, where all characters must be numeric
        else:
            int(isbn)
    ##except catches an error and handles it here
    ##this is what will happen if the try fails
    except:
        print("Invalid character was found.")
        ##when python hits the return it will immediately exit the function (stopping the code at this error)
        return

    ##actual execution logic
    if length == 10 or length == 13:
        ##calls the validate_isbn which then calls either the calculate_check_digit_10 or calculate_check_digit_13 depending on length
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')

##this needs to be commented out for the lab to clear but I need to use it to run the program for testing so thats fun
##also not recommended to call this main() so that the __name__ doesnt get messed up if this file were imported elsewhere (only good if I run this file directly not if I import)
main()

##Tests

##1530051126,10 should = Valid ISBN Code.
##9781530051120,13 should = Valid ISBN Code.
##1530051125,10 should = Invalid ISBN Code.
##9781530051120,10 should = ISBN-10 code should be 10 digits long.
##1530051126,13 should = ISBN-13 code should be 13 digits long.
##15-0051126,10 should = Invalid character was found.
##1530051126,9 should = Length should be 10 or 13.
##1530051125,A should = Length must be a number.
##1530051125 should = Enter comma-separated values.
##9971502100,10 should = Valid ISBN Code.
##080442957X,10 should = Valid ISBN Code.
##9781947172104,13 should = Valid ISBN Code.