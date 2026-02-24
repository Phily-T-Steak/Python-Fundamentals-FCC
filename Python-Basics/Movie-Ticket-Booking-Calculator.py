# Building a "calculator" based on some various requirements with the use of if statments

# Here are some of the base variables
base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

# Check based on the age of the user to see if they can get a ticket in the first palce
if age > 17:
    print('User is eligible to book a ticket')
# Check to see if the user can see an "Evening" show
if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

# Adding in another layer to see if the user is a member and/or its the weekend
is_member = False
is_weekend = False

# Placeholder variable so that we can do math with it based on age of user
discount = 0
# "math" for applying the discount if the user is of proper age
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

# Placeholder variable so that we can do math with it based on when the ticket is booked
extra_charges = 0
# "math" for applying the discount if the user is buying at a certian time
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

# Final check to see if the user is eligible to see the movie
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')
    
    # Placeholder variable so that we can do math with it based on user seat type
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)  
    
    # Final calculation nested inside the if statment since this is the "last" line of code the program would read if true
    final_price = base_price - discount + extra_charges + service_charges
    print (f"Final price of the ticket: {final_price}")

# Assuming that the age restriction is false, ignore the rest and decline ticket purchase
else:
    print('Ticket booking failed due to restrictions')