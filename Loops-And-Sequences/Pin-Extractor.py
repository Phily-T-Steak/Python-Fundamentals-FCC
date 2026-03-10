#In this workshop you will create a pin extractor, the pin digits are hidden in each line of a poem.
#starting off with our function used to extract the pin from the poems
def pin_extractor(poems):
    #we are creating a variable that is being used as a blank list to be updated later
    secret_codes = []
    #our first for loop is iterating through each poem in the poems list
    for poem in poems:
        #here we are creating a secret_code variable as an empty string to be updated later
        secret_code = ''
        #we are creating a variable lines and using the .split() function to break up poems into indivual lines using the \n function
        lines = poem.split('\n')
        #in our second for loop we are iterating throughe ach line in the lines list from the newly made lines variable while also having the enumerate add a value with the help of the line_index variable
        for line_index, line in enumerate(lines):
            #here is where we are breaking it down to its final size of words with the use of the .split() function which is seperating each of the stings into individual words in the form of a list
            #.split() by defult splits on whitespaces (spaces, tabs, newlines) since nothing was specified it went with spaces
            words = line.split()
            #built in if statement to capture the edge case of checking if the list has enough words to access thecurrent index
            if len(words) > line_index:
                #This is what is making the pin 
                #words[line_index] is grabbing the word from the list based on the index value, len() is counting the characters of the selected word, str() is turning that value into a string so that is compatiable with secret_code
                secret_code += str(len(words[line_index]))
            #if there are less words in a sentence than the index value it adds a 0 rather than breaking the code
            else:
                #this is what is adding a string value of 0 to secret_code if there is no word for the index value
                secret_code += '0'
        #here we are using the .append to add the updated secret_code value to our secret_codes list
        secret_codes.append(secret_code)
    #with this we are sending the final list of secret_codes back to where the function was called
    return secret_codes        

#variable 1 that we are extracting a pin from using """ to break out lines
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""
#variables 2 & 3 that we are extracking a pin from using \n to break out lines
poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

#final print command that runs the function with a list of poems rather than just 1 poem
#this gives us a pin of the lenght of a given word from a poem, selected based on the index value of the line its on
print(pin_extractor([poem, poem2, poem3]))