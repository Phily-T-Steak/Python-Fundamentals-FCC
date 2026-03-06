#In this lab you will practice the basics of Python by building a small app that creates a character for an RPG adventure.
#orginal lab has me using a bunch of returns but for testing purposes I switched them all to prints

# variable that we will use in the final product
full_dot = '●'
empty_dot = '○'

#main function used to create the "character" + stats
def create_character(character_name, strength, intelligence, charisma):
    #testing to see if the name is a string
    if not isinstance(character_name,str):
        print("The character name should be a string")
    #testing to see if the string contains any characters
    if character_name == "":
        print("The character should have a name")
    #testing to make sure then name is less than 10 characters
    if len(character_name) > 10:
        print("The character name is too long")
    #testing using the .find to see if the name contains any spaces. if no spaces are found the .find has a value of -1
    if character_name.find(" ") != -1:
        print("The character name should not contain spaces")

    # this is created to turn the stats into a tuple so that we can then use them in a loop
    stats = (strength, intelligence, charisma)
    # using a generator expression check each objest inside of stats for integer type
    if not all(isinstance(stat,int) for stat in stats):
        print("All stats should be integers")
    # testing the stats to verify none of them are less than 1
    if not all(stat >= 1 for stat in stats):
        print("All stats should be no less than 1")
    #testing stats to verify that none of them are more than 4
    if not all(stat <= 4 for stat in stats):
        print("All stats should be no more than 4")
    #testing to verify that the total stats do not exceed 7
    if sum(stats) != 7:
        print("The character should start with 7 points")
    #with a combination of the f' string function to insert variables into the string and \n to create new lines we get the final result
    print(f'{character_name}\nSTR {strength*full_dot+(10-strength)*empty_dot}\nINT {intelligence*full_dot+(10-intelligence)*empty_dot}\nCHA {charisma*full_dot+(10-charisma)*empty_dot}')

#actual use of the main function
create_character("ren",4,2,1)