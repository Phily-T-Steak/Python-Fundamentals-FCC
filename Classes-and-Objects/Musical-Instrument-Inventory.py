#In this workshop, you'll get some practice with Python's classes and objects by building a musical instrument inventory.

#here is the creation of the class we are using in this lesson
#this acts more like a blueprint/framework and then the actual "instrument" get created later on
class MusicalInstrument:
    #this __init__ is automatically called during object creation and is used to initalize the object
    #'self' refers to the specific object being created or used. it lets us store and access data that belongs to that object
    def __init__(self, name, instrument_type):
        self.name = name
        self.instrument_type = instrument_type

    #creating some other defs to refererence later on. These are called methods (functions inside a class)
    def play(self):
        print(f'The {self.name} is fun to play!')

    #creating some other defs to refererence later on. These are called methods (functions inside a class)
    def get_fact(self):
        return f'The {self.name} is part of the {self.instrument_type} family of instruments.'

#here are the variables we are creating to be used with the class
#aka build a new object using this blueprint/framework
instrument_1 = MusicalInstrument('Oboe', 'woodwind')
instrument_2 = MusicalInstrument('Trumpet', 'brass')

#test case number 1 of calling the methods of the class. 
#MusicalInstrument.play(instrument_1) would also work,
#but instrument_1.play() is preferred because Python automatically passes the object as 'self'. this style is cleaner (scaleable) and follows object-oriented design (asking the object to act)
instrument_1.play()
print(instrument_1.get_fact())

#test case number 2 of calling the methods of the class. Since the get_fact uses a return we are then using a print() to have it show up in the terminal
instrument_2.play()
print(instrument_2.get_fact())