#this FCC workshop goes over inheritance (parent and child classes) and polymorphism (different classes can respond differently to the same method call)
#A parent class can define common behavior, child classes can override that behavior, and code can use either object without needing to know which specific class it is working with.

#we are using this class to handle error messages
# this is technically a child class inheriting from Python's built-in Exception class
class MediaError(Exception):
    #here we are using a docstring to add notes of what this class is rather than comments uings the #
    """Custom exception for media-related errors."""

    #constructor method that runs when a new object is created with this class
    def __init__(self, message, obj):
        #Run Exception's constructor and give it the message. This is the same as writting Exception.__init__(self, message)
        super().__init__(message)
        #assigning of the instance attribute to the object being created
        self.obj = obj

#here we have the parent class that the child class builds off of
class Movie:
    #here we are using a docstring to add notes of what this class is rather than comments uings the #
    """Parent class representing a movie."""
    
    #constructor method that runs when a new object is created with this class
    def __init__(self, title, year, director, duration):
        #validation of the instance attribute given with the following if statement
        #stripping away any spaces from the title instance attribute and checking if there is anything left
        if not title.strip():
            raise ValueError('Title cannot be empty')
        #verify that the year instance attribute is greater than 1895 otherwise raise error
        if year < 1895:
            raise ValueError('Year must be 1895 or later')
        #stripping away any spaces from the director instance attribute and checking if there is anything left
        if not director.strip():
            raise ValueError('Director cannot be empty')
        #check that the movie instance attribute is longer than 0 otherwise raise an error
        if duration <= 0:
            raise ValueError('Duration must be positive')
        #assigning of the instance attribute to the object being created
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration

    #with the use of the __str__ special method we are setting up the default print layout for this class
    def __str__(self):
        return f'{self.title} ({self.year}) - {self.duration} min, {self.director}'

#here is our child class that is building off of the parent class
class TVSeries(Movie):
    #here we are using a docstring to add notes of what this class is rather than comments uings the #
    """Child class representing an entire TV series."""

    #constructor method that runs when a new object is created with this class
    def __init__(self, title, year, director, duration, seasons, total_episodes):
        #with the use of super(). we are reusing the special method __init__ from the parent class to pass these same instance attribute through
        #call the parent class constructor so title, year, director, duration and their validation logic don't need to be rewritten
        super().__init__(title, year, director, duration)
        #validation of only the additional instance attribute given since the validation from the parent class is still used for everything else
        if seasons < 1:
            raise ValueError('Seasons must be 1 or greater')
        if total_episodes < 1:
            raise ValueError('Total episodes must be 1 or greater')
        #assigning of only the new instance attribute to the object being created. Due to the ones coming from the parent class reusing code from that class
        self.seasons = seasons
        self.total_episodes = total_episodes

    #with the use of the __str__ special method we are setting up the default print layout for this class
    def __str__(self):
        return f'{self.title} ({self.year}) - {self.seasons} seasons, {self.total_episodes} episodes, {self.duration} min avg, {self.director}'

#we are using this class to represent both the parent and the child class in a "final form"
#MediaCatalogue does not know how a Movie or TVSeries is formatted. It simply calls str() on the object and lets the object decide how to represent itself.
#This is a key OOP principle: objects are responsible for their own behavior.
class MediaCatalogue:
    #here we are using a docstring to add notes of what this class is rather than comments uings the #
    """A catalogue that can store different types of media items."""

    #constructor method that runs when a new object is created with this class
    def __init__(self):
        #each MediaCatalogue object starts with its own empty list of media items. This will get updated later
        self.items = []

    #creating an add method so that we can update objects from the parent/child class to the placeholder list
    def add(self, media_item):
        #validating that the media_item passed into this agrument is representing the parent class and in turn the child class
        #TVSeries objects pass this check because TVSeries inherits from Movie
        if not isinstance(media_item, Movie):
            #if it is not the parent class or the child class then it raises the following error
            raise MediaError('Only Movie or TVSeries instances can be added', media_item)
        #assuming it passes the validation and is from the parent or child class the placeholder list we created earlier gets updated with the new entry
        self.items.append(media_item)

    #when I did this in the workshop it was formated a bit differently but the concept is the same
    def get_movies(self):
        #inside of the new list we are creating [], we are iterating through the list at the start of this class, we are then using the type() to see if the parent class movie is called out, assuming it is we are then appending (behind the scenes) that result to the list []
        #we must use type() here rather than isinstance() since the child class would technically be a movie instance due to it inheriting its properties from the parent class movie
        #this is being used to break out the movies from the total list
        return [item for item in self.items if type(item) is Movie]

    #when I did this in the workshop it was formated a bit differently but the concept is the same
    def get_tv_series(self):
        #inside of the new list we are creating [], we are iterating through the list at the start of this class, we are then using the isinstance() to see if the child class tvseries is called out, assuming it is we are then appending (behind the scenes) that result to the list []
        #we can get away with using isinstance() here beacause only TVSeries objects will return True. Movie objects are not considered TVSeries objects (parent/child class relationship is one way)
        #this is being used to break out the tv series from the total list
        return [item for item in self.items if isinstance(item, TVSeries)]
    
    #with the use of the __str__ special method we are setting up the default print layout for this class
    def __str__(self):
        #validation to check if the placeholder list we made at the start of this class is empty
        if not self.items:
            return 'Media Catalogue (empty)'
        
        #creating variables that call on the new sub lists made in the previous methods
        movies = self.get_movies()
        series = self.get_tv_series()

        #creating a variable that we will be updating with the two variables we just created assuming they pass validation
        result = f'Media Catalogue ({len(self.items)} items):\n\n'
        
        #validating the movies variable we just created based off the get_movies method we built in the code above
        if movies:
            #assuming there are movies found in the variable we add in the movies banner
            result += '=== MOVIES ===\n'
            #iterating through the movie varible that is calling on the get_movies method we want to enumerate each entry starting with 1
            for i, movie in enumerate(movies, 1):
                #with each loop through this iteration we are updating the movie list with the enumeration of that loop followed by the movie on that index
                #this is an example of polymorphism since we are actually asking python to call str(movie) and then movie.__str__() and if movie is a Movie then it runs Movie.__str__(). This is how the object handles itself without formatting here and now it reused the exisiting code
                #Python calls the correct __str__() method based on the object's type. MediaCatalogue doesn't need to know whether this is a Movie or TVSeries
                result += f'{i}. {movie}\n'
        
        #validating the movies variable we just created based off the get_tv_series method we built in the code above
        if series:
            #assuming there are tv series found in the variable we add in the TV banner
            result += '=== TV SERIES ===\n'
            #iterating through the tv varible that is calling on the get_tv_series method we want to enumerate each entry starting with 1
            for i, show in enumerate(series, 1):
                #with each loop through this iteration we are updating the tv list with the enumeration of that loop followed by the tv series on that index
                #this is an example of polymorphism since we are actually asking python to call str(show) and then show.__str__() and if show is a TV series then it runs TVSeries.__str__(). This is how the object handles itself without formatting here and now it reused the exisiting code
                #Python calls the correct __str__() method based on the object's type. MediaCatalogue doesn't need to know whether this is a Movie or TVSeries
                result += f'{i}. {show}\n'
        
        #lastly we are returning the final result so that we have our new updated list after all the validations were performed. This is what is getting printed
        return result

#this is the actual creation of an object
catalogue = MediaCatalogue()

#we are then using this try except method to run the logic
try:
    #creating an object from the movie class
    movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
    #then updating the "main" object with this new object we created
    catalogue.add(movie1)
    #creating an object from the movie class
    movie2 = Movie('Inception', 2010, 'Christopher Nolan', 148)
    #then updating the "main" object with this new object we created
    catalogue.add(movie2)

    #creating an object from the tv class
    series1 = TVSeries('Scrubs', 2001, 'Bill Lawrence', 24, 9, 182)
    #then updating the "main" object with this new object we created
    catalogue.add(series1)
    #creating an object from the tv class
    series2 = TVSeries('Breaking Bad', 2008, 'Vince Gilligan', 47, 5, 62)
    #then updating the "main" object with this new object we created
    catalogue.add(series2)

    #final print of the "full" class
    print(catalogue)
#with this except part of the logic we are formatting the ValueError found in any of the validation checks to be displayed as follows with the print()
except ValueError as e:
    print(f'Validation Error: {e}')
#with this except part of the logic we are formatting the MediaError for when the parameters are not used properly
except MediaError as e:
    print(f'Media Error: {e}')
    print(f'Unable to add {e.obj}: {type(e.obj)}')