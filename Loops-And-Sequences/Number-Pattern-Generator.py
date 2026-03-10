#In this lab you will practice the basics of Python by building a small app that creates a number pattern.
#here is our function we are going to be using to generate the number pattern
def number_pattern (n):
    #we have some built in edge cases to verify that the n value proived is an integer and is a postive number (not 0)
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."
    #here we are creating a variable to be used later to store the string of numbers
    numbers = ""
    #this is our for loop used to create a string that we are gradually building (it's more like growing a sentence). We are using the range() function since the input of the function is a single int and not a list
    #range() allows us to start with the value of 1 and stop at the end result since this is really saying range(1,5) which gives us 1,2,3,4 since it stops at the number before the last
    for number in range(1, n+1):
        #this is what we are using to build the actual string accumulator by saving the number generated for each loop and placing a space at the end of it to the numbers variable that we made earlier (gets updated with each loop)
        numbers += str(number) + " "
    # here we are storing the final string of numbers and we use the .strip() to remove the last space at the end of this string (works for beginning and end only and nothing in the middle)
    return numbers.strip()
    
#this is what we are using to test the functions created. We needed to add print() to them so that we can actuall see the result in the terminal rather than simply storing the vlaues
print(number_pattern(4))
print(number_pattern(12))