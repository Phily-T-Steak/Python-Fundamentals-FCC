class GameCharacter:
    def __init__ (self, _name,):
        self._name = _name
    
        self._health = 100
        self._mana = 50
        self._level = 1

    #created a name property for read-only access to the character's name
    @property
    def name (self):
        #because we only defined a getter and not a setter, outside code can read the name but cannot modify it through this property
        return self._name

    #defined a getter that reurns the current health
    @property
    def health (self):
        return self._health

    #created a setter that allows us to update the _health value within a range
    @health.setter
    def health (self, new_health):
        #basic if statement so that if the new_health value is less then 0 it defaults to 0
        if new_health < 0:
            self._health = 0
        #added on to that if statement that if the new_health value is greater than 100 (max) it will default to 100
        elif new_health > 100:
            self._health = 100
        #lastly saying that if it passes the previous two checks then it must fall within the range and can be updated to the new_health value
        #if the value is already within the valid range, store it unchanged (this can be refered to as "clamping")
        else:
            self._health = new_health

    #defined a getter that reurns the current mana
    @property
    def mana (self):
        return self._mana

    #created a setter that allows us to update the _mana value within a range much like the _health setter
    @mana.setter
    def mana (self, new_mana):
        if new_mana < 0:
            self._mana = 0
        elif new_mana > 50:
            self._mana = 50
        else:
            self._mana = new_mana

    #defined a getter that reurns the current level
    @property
    def level (self):
        return self._level

    #created a level_up method for this class
    def level_up (self):
        #when this is called increase the level by 1
        self._level += 1
        #when this is called it resets health to "max" aka back to the 100 mark. However we are calling on the setter for this because we are using self.health rather than self._health to make sure the values still pass all of our validations
        self.health = 100
        #when this is called it restet mana to "max" aka back to the 50 mark. However we are calling on the setter for this because we are using self.mana rather than self._mana to make sure the values still pass all of our validations
        self.mana = 50
        #finally it pritns a message letting you know the character leveled by calling out their name and current level
        print(f'{self._name} leveled up to {self._level}!')

    #made a __str__ special method to standerdize the prints for this class
    def __str__ (self):
        #__str__ must return a string. Using print() inside __str__ returns None, which causes a TypeError when Python tries to display the object. Therfore you must use a return for the __str__ special method
        return f'Name: {self._name}\nLevel: {self._level}\nHealth: {self._health}\nMana: {self._mana}'

#testing
# Creates a new character named Kratos
hero = GameCharacter('Kratos')
# Displays the character's stats
print(hero)

# Decreases health by 30
#this is reading the current health through the getter, then subtracting 30, then sending the new value back through the setter for validation (could also be seen as hero.health = hero.health - 30)
hero.health -= 30
# Decreases mana by 10
#this is reading the current mana through the getter, then subtracting 10, then sending the new value back through the setter for validation
hero.mana -= 10
# Displays the updated stats
print(hero)  

# Levels up the character
hero.level_up()  
# Displays the stats after leveling up
print(hero)