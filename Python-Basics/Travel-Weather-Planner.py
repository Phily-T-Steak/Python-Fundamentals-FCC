# For this lab, you will use conditional statements to determine whether commuting is possible based on the weather, the distance to travel, and the availability of a vehicle.

# predefined variables used to determine what triggers in the if statment
distance_mi = 4.31
is_raining = True
has_bike = True
has_car = False
has_ride_share_app = True

#The lab had me use just true or false but for my own testing we are having it use phrases
if isinstance(distance_mi,bool) or distance_mi <= 0:
    print("This is a 'falsy' value, can not be used")
elif distance_mi <= 1 and is_raining == False:
    print("You can safely walk this distance")
elif distance_mi <= 1 and is_raining == True:
    print("I wouldnt advise walking in the rain")
elif distance_mi > 1 and distance_mi <= 6 and has_bike == True and is_raining == False:
    print("This is a good distance to ride you bike in")
elif distance_mi > 1 and distance_mi <= 6 and (has_bike == False or is_raining == True):
    print("I wouldnt ride you bike this distance because its raining")
elif distance_mi > 6 and (has_car == True or has_ride_share_app == True):
    print("I would recomend traveling in a vehicle for this distance")
else:
    print("Looks like you cant get there")