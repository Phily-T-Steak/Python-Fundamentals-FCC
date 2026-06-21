#this FFC workshop was focused on the OOP concept of Abstraction
#Abstraction means defining WHAT behavior is required without defining HOW it is performed
#The abstract class acts like a blueprint or contract. Concrete child classes must provide their own implementation of the required methods
#Abstract classes are not meant to be instantiated directly. Instead they exist to define behavior that child classes must implement
#Abstraction lets us define a required interface without implementing it while Polymorphism allows multiple child classes to be treated as the same type

#here we are importing the "abstract base class" throught he abc import along with the abstractmethod decorator
from abc import ABC, abstractmethod

#with the first class we are setting up the structure for the products that we will be using as the base to do all of our math off of
class Product:
    
    #of course we have our constructor method that runs when a new object is created with this class
    #in the workshop we also covered optional type hints for parameters/results. This can be seen by the parameter: hint as well as the return type "hint" () -> return type both of which are used to represent the expected type
    #Constructors initialize new objects and do not return a value, so they use the return type hint -> None
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    #setting up the defualt print format of this object with the use of the special method __str__
    def __str__(self) -> str:
        return f'{self.name} - ${self.price}'

#Here we are setting up the abstract base class that will be used as the framework for our concrete subclasses that we will make later on
#this is technically a child class to the ABC that we imported at the start of this workshop
class DiscountStrategy(ABC):
    
    #with the use of the @abstractmethod decorator we are laying out the frame work for a "is_applicable" method that the concrete classes can use
    #@abstractmethod forces child classes to implement this method before objects can be created from those child classes
    @abstractmethod
    #again adding in the new type hints for not only the parameters but for the return type as well
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        #using a pass here since this is just building out the framework and the concrete individual usecases will have their own logic
        pass

    #with the use of the @abstractmethod decorator we are laying out the frame work for a "apply_discount" method that the concrete classes can use
    #@abstractmethod forces child classes to implement this method before objects can be created from those child classes
    @abstractmethod
    #again adding in the new type hints for not only the parameters but for the return type as well
    def apply_discount(self, product: Product) -> float:
        #using a pass here since this is just building out the framework and the concrete individual usecases will have their own logic
        pass

#this is the first concrete subclass that implements the abstract method, this is acting as a child class to the abstract base class
class PercentageDiscount(DiscountStrategy):
    
    #of course we have our constructor method that runs when a new object is created with this class
    #again adding in the new type hints for not only the parameters but for the return type as well
    #Constructors initialize new objects and do not return a value, so they use the return type hint -> None
    def __init__(self, percent: int) -> None:
        self.percent = percent

    #Here we are using the "is_applicable" method that is overriding the method from the parent abstract class
    #again adding in the new type hints for not only the parameters but for the return type as well
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        #originally this was written as if self.percent <= 70, return true, else, return false. However writing that as return self.percent <= 70 returns the same thing
        return self.percent <= 70

    #Here we are using the "apply_discount" method that is overriding the method from the parent abstract class
    #again adding in the new type hints for not only the parameters but for the return type as well
    def apply_discount(self, product: Product) -> float:
        #when this method is called we are calculating the discounted price using the percentage stored in self.percent
        return product.price * (1 - self.percent / 100)

#this is the second concrete subclass that implements the abstract method, this is acting as a child class to the abstract base class
class FixedAmountDiscount(DiscountStrategy):
    
    #of course we have our constructor method that runs when a new object is created with this class
    #again adding in the new type hints for not only the parameters but for the return type as well
    #Constructors initialize new objects and do not return a value, so they use the return type hint -> None
    def __init__(self, amount: int) -> None:
        self.amount = amount

    #Here we are using the "is_applicable" method that is overriding the method from the parent abstract class
    #again adding in the new type hints for not only the parameters but for the return type as well
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        #originally this was written as if product.price * 0.9 > self.amount, return true, else, return false. However writing that as return product.price * 0.9 > self.amount returns the same thing
        #The comparison itself evaluates to either True or False, so we can return the result directly instead of using an if/else statement
        return product.price * 0.9 > self.amount

    #Here we are using the "apply_discount" method that is overriding the method from the parent abstract class
    #again adding in the new type hints for not only the parameters but for the return type as well
    def apply_discount(self, product: Product) -> float:
        #when we call on this method we are calculating the new product price based on the "fixed" value that is passed through at the start of this class
        return product.price - self.amount

#this is the third concrete subclass that implements the abstract method, this is acting as a child class to the abstract base class
class PremiumUserDiscount(DiscountStrategy):
    
    #Here we are using the "is_applicable" method that is overriding the method from the parent abstract class
    #again adding in the new type hints for not only the parameters but for the return type as well
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        #simply check to see if the user qualifies for the discount based on the user_tier value
        return user_tier.lower() == 'premium'

    #Here we are using the "apply_discount" method that is overriding the method from the parent abstract class
    #again adding in the new type hints for not only the parameters but for the return type as well
    def apply_discount(self, product: Product) -> float:
        #when we call on this method we are applying a 20% discount to the product price, assuming they qualify
        return product.price * 0.8

#with this class we are determining the "best" price compairing between all of the discount options
#The DiscountEngine never needs to know which discount class it is using. It simply calls methods defined by the DiscountStrategy contract
class DiscountEngine:
    
    #again adding in the new type hints for not only the parameters but for the return type as well
    #Constructors initialize new objects and do not return a value, so they use the return type hint -> None
    def __init__(self, strategies: list[DiscountStrategy]) -> None:
        self.strategies = strategies

    #this is the method being used to actually sort out the best price
    #again adding in the new type hints for not only the parameters but for the return type as well
    def calculate_best_price(self, product: Product, user_tier: str) -> float:
        
        #here we are setting up a placeholder list that we will later go back and update with the final price
        prices = [product.price]

        #This is an example of polymorphism. Each object in the list may be a different class, but because they all inherit from DiscountStrategy they can all respond to is_applicable() and apply_discount()
        #with the use of a for loop here we are iterating through the self.strategies list provided by the object created from this class (should be a list of discount strategy objects)
        #Because all strategies inherit from DiscountStrategy, the engine can treat them all the same way even though each class has different internal logic
        for strategy in self.strategies:
            #validating for each iteration through the list to see if the discount is even applicable based on the product and the user tier given
            if strategy.is_applicable(product, user_tier):
                #assuming it is a valid discount, the discount is then applied using the specific strategy object from the current iteration
                discounted = strategy.apply_discount(product)
                #the prices placeholder list is then updated with the discounted price 
                prices.append(discounted)

        #The original product price was added to the list first, so if no discounts are applicable, the original price will be returned
        #once all the iterations have been run and we have our updated prices list of all the discount effects, we use the min() to grab the smallest value from the list to get our "best" discount for the product
        return min(prices)

#here is what we are actually using to test with for 1 product type. This can be reused by modifying the product, user_tier, and strategies
#This check allows the file to be run directly for testing. If another file imports this file, the code inside this block will not execute
if __name__ == '__main__':
    
    #creating an object from the Product class to give us a base to do our math off of
    product = Product('Wireless Mouse', 50.0)
    
    #also adding in the user_tier as a standalone variable to be used later on
    user_tier = 'Premium'

    #this is the list of objects we are using to iterate through
    strategies = [
        PercentageDiscount(10),
        FixedAmountDiscount(5),
        PremiumUserDiscount()
    ]

    #creating an object from the price sorting class passing through the list of classes
    engine = DiscountEngine(strategies)
    
    #creating a new variable to then use that newly made object to run the method in the price sorting class based off the product object and the user_tier variable created earlier
    best_price = engine.calculate_best_price(product, user_tier)
    #after running the best_price variable we then print the results. final cost is being held to a 2 decimal place value with the use of :.2f
    print(f'Best price for {product.name} for {user_tier} user: ${best_price:.2f}')    