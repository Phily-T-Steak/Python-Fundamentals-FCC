# In this lab you will write a function that calculates the final price of an item after applying a percentage discount
    # This is really focusing on making a def with built in fail safes to test edge cases and showing how its reusable
# The lab had me use return instead of print so that in theory the program could uses these values in another instance
    # When initally testing I swapped all the returns to prints so that I could verify the code was working properly
def apply_discount (price, discount):
    # test that parameter 1 should be a number
    if not isinstance(price,(int, float)):
        return("The price should be a number")
    # test that parameter 2 should be a number
    if not isinstance(discount,(int, float)):
        return("The discount should be a number")
    # test to make sure out cost isnt negative
    if price <= 0:
        return("The price should be greater than 0")
    # test to keep the discount between 0-100 since its a %
    if discount < 0 or discount > 100:
        return("The discount should be between 0 and 100")
    # actual part of the def that is doing the work
    final_price = price - price * (discount/100)
    return(final_price)

# Various use cases of the one def
# technically while the return function is used to save the value for later use, since var = def(x,y) doesnt exisit nothing is being overwritten/stored
apply_discount(100,20)
apply_discount(200,50)
apply_discount(50,0)
apply_discount(1000,100)
apply_discount(74.5,20.0)