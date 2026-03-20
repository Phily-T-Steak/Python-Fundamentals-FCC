#build a User Configuration Manager that allows users to manage their settings such as theme, language, and notifications. You will implement functions to add, update, delete, and view user settings.
# many of these functions follow a similar pattern:
# 1. normalize input (convert to lowercase)
# 2. check if the key exists in the dictionary
# 3. perform the operation only if allowed
# 4. return a message describing the result

#this function is being used to add in key: value pairs that dont already exisit in the dictionary
def add_setting (settings, pair):
    
    #unpacking the tuple by having key and value represent the 2 variables given in "pair"
    key, value = pair
    
    #making our key & value into lowercase
    key = key.lower()
    value = value.lower()
    
    #saying if the key is found in the settings do the following
    if key in settings:
        #this should be a return but for testing I made it a print
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
     #saying if the key is not found in the settings do the following
    else:
        #this dictionary assignment will either add a new key or overwrite an existing one, so we guard it with an if statement to prevent overwriting an existing key (which would turn this into an update instead of an add)
        settings[key] = value
        #this should be a return but for testing I made it a print
        return f"Setting '{key}' added with value '{value}' successfully!"

#this functions is being used to updated existing key: value pairs in the dictionary
def update_setting (settings, pair):
    
    #unpacking the tuple by having key and value represent the 2 variables given in "pair"
    key,value = pair
    
    #making our key & value into lowercase
    key = key.lower()
    value = value.lower()
    
    #saying if the key is found in the settings do the following
    if key in settings:
        #dictionary assignment replaces the existing value for this key, so we allow it only if the key already exists
        settings[key] = value
        #this should be a return but for testing I made it a print
        return f"Setting '{key}' updated to '{value}' successfully!"
    #saying if the key is not found in the settings do the following
    else:
        #this should be a return but for testing I made it a print
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

#this value is deleting keys and in turn their value pair found in the dictionary
def delete_setting (settings, key):
    
    #making our key into lowercase
    key = key.lower()
    
    #saying if the key is found in the settings do the following
    if key in settings:
        #.pop(key) removes the key and returns its value (though we are not using the returned value here)
        settings.pop(key)
        #this should be a return but for testing I made it a print
        return f"Setting '{key}' deleted successfully!"
    #saying if the key is not found in the settings do the following
    else:
        #this should be a return but for testing I made it a print
        return "Setting not found!"

#this function is being used to verify what the current dictionary is and if there is one at all
def view_settings (settings):

    #using this if statement to say if the settings parameter is empty then return the given phrase. This works because empty dictionaries evaluate to false in python so this is similar to saying if not true then ... (in our case checks if the dictionary is empty)
    if not settings:
        #this should be a return but for testing I made it a print
        return "No settings available." 
    
    #creating a "collector" string with the inital text to be later added on to
    results = f"Current User Settings:\n"
    
    #based on the requirements of the project I needed to report the key and values of the setting parameter found in this def
    #using a for loop going over the setting. using .items() returns key-value pairs, allowing us to unpack them into key and value in the loop 
    for key, value in settings.items():
        #the project had a requirement that the first letter of each key be capitalized so I used the .title() to perform that
        key = key.title()
        #we are using the += to append each formatted line to the existing "collector" stored in the results variable defined outside the loop with the key and value variables we broke out of the settings parameter
        #also updating the results with a new line for each iteration through the for loop with the use of \n due to project requirements
        results += f'{key}: {value}\n'
    
    #summarizing the results. Originally had this as a print so that I could verify the code was working but switched back to a return for the project specifications
    return results

      

#dictionary setup used for reference but not actually being used in this lab
test_settings = {
    "Theme" : "dark",
    "Notifications" : "enabled",
    "Volume" : "high"
}

#testing defs
add_setting({'theme':'light'}, ("THEME", "dark"))
add_setting({'theme': 'light'}, ('volume', 'high'))

update_setting({'theme': 'light'}, ('theme', 'dark'))
update_setting({'theme': 'light'}, ('volume', 'high'))

delete_setting({'theme': 'light'}, 'theme')

view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'})