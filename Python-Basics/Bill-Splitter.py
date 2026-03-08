#In this workshop, you will practice working with numbers and mathematical operations to build a bill splitter
#this will be our variable that we keep adding to
running_total = 0

#a variable we will use later on for sliptting the check
num_of_friends = 4

#variables created to represent the price of various items on the bill
appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

#here we are updating the orginal variable with the use of +=. this now has a new value
running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

#creating a new variable to calcuated tip based off the update value of the orginal variable
tip = running_total * 0.25
print('Tip amount:', tip)

#adding in the new variable to the orginal variable with the use of the += again
running_total += tip
print('Total with tip:', running_total)

#here we are splitting the final calculated bill up amomgst all of the people at the table and storing that as a new variable
final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

#due to the numbers being stored in binary we need to use the round() function to bring it back to 2 decimal places
each_pays = round(final_bill,2)
print("Each person pays:",each_pays)