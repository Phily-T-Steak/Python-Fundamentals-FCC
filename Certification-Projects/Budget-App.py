#In this lab, you will build a simple budget app that tracks spending in different categories and can show the relative spending percentage on a graph.

# method order inside a class doesn't matter because the whole class is defined before it's used. python reads the class definition first, so any method can call another regardless of order
class Category:
    
    #the initalizing method that assigned each category class a name and a list
    def __init__ (self, name):
        self.name = name
        self.ledger = []

    #this method lets us update the list with an amount and an optional description in the given format
    def deposit(self, amount, description = ""):
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description = ""):
        #first we are calling the check_funds method to verify that the amount we are withdrawing works
        if self.check_funds(amount):
            #assuming this check returns true we can then add this to the ledger
            self.ledger.append({'amount': -1*amount, 'description': description})
            return True
        else:
            return False
        
    def get_balance(self):
        #setting up a placeholder variable to add up every value in the list
        total = 0
        #using a for loop to iterate through the list so we can extract the value
        for money in self.ledger:
            #then adding that value to our placeholder for each iteration done
            #Since we iterated with "money" across the ledger, and each "money" is a dictionary, we are then pulling the value from the associated key by using []
            total += money['amount']
        #this then returns the computed balance so other methods can use it
        return total
    
    def transfer(self, amount, destination):
        #first we are using the check_funds method to see if this is even possible
        if self.check_funds(amount):
            #then we call the withdraw method remove the money (it can take an amount and a description)
            self.withdraw(amount, f'Transfer to {destination.name}')
            #then we add the same amount to the destination category to complete the transfer (it can take an amount and a description)
            destination.deposit(amount, f'Transfer from {self.name}')
            #if this process is sucessful we get a True value
            return True
        else:
            #if this process is unsucessful we get a False value
            return False
        
    def check_funds(self, amount):
        #we are first comparing the stated amount to our current total balance by calling the get_balance method     
        if amount > self.get_balance():
            #if the amount is greater than the current balance
            return False
        else:
            #if the amount is less than or equal to the current balance
            return True
    
    #this is our default print format method since we are using a special method __str__     
    def __str__(self):
        #we are using this placeholder variable to start building out our printed ledger
        results = ""
        #formating for the title based on the class name and using .center to center the name and filling the remaining x out of 30 spaces with * + a new line break
        results += f"{self.name}".center(30, "*") + "\n"
        #to get the history we are iterating through the ledger and breaking out the key value pairs so that we can print these as well
        for item in self.ledger:
            #Since we iterated with item across the ledger, and each item is a dictionary, we are then pulling the value from the associated key by using []
            description = item["description"] 
            #after we get the discrption we are aligning it left in the 23 character space we provided
            #added in [:23] so that it slices the first 23 characters and presents only that rather than a whole description if its longer than 23 characters
            results += f"{description[:23]}".ljust(23)
            #Since we iterated with item across the ledger, and each item is a dictionary, we are then pulling the value from the associated key by using []
            amount = item["amount"]
            #after we get the amount we are aligning it right in the 7 character space we provided + a new line break
            #also using :.2f even though FCC didnt cover this. : means "here comes the formatting instructions", .2 means "show 2 decimal place", and f means "treat this as a fixed point number"
            results += f"{amount:.2f}".rjust(7) + "\n"
        #at the end of the printed ledger we are grabbing the total found using the get_balance method we made earlier
        #also added in the :.2f here to keep formating the same throughout
        results += f"Total: {self.get_balance():.2f}"
        #lastly we are using this return the fully formatted string so it prints when the object is printed
        return results

#creating a def/function to build out a visual representation of the data in a bar graph format
def create_spend_chart(categories):
    
    #adding in my placeholder text that we will be building off of
    graph = ""
    #adding in the title to the graph
    graph += "Percentage spent by category" + "\n"

    #first loop is being used to extract the total cost per category
    #we are creating a plceholder list so that we can store the cost spent per category
    spent = []
    #using this to iterate through the categories given in the def
    for category in categories:
        #using a placeholder value so we can add up all the withdraws
        total = 0
        #iterating for the specific category and pulling out the key:value pairs found in the given categories ledger
        for item in category.ledger:
            #since the ledger is a lsit of dictionaries, we are pulling the value from the associated key with []
            if item['amount'] < 0:
                #this is what is adding the value to the placeholder value (we are grabbing withdraws aka negative value so *-1 to get "real values")
                total += item["amount"] * -1
        #with this we are updating our placeholder list with the updated total value for the given category
        spent.append(total)
    
    #we are summing the list to get the total spent across all categories which will help with the math later on
    sum_total = sum(spent)

    #second loop is being used to calculate the % of the cost of a given category realive to the total cost across all categories
    #creating a placeholder list so that we can store all our calcs
    percentage = []
    #using this to iterate through our updated spent list created from the previous set of for loops
    for category in spent:
        #using the cost found in spent to a % (x/y)*100, we then use floor division // to divid and drop everything after the decimal, then *10 to bring it back to x/100
        cost = (int((category/sum_total)*100)//10)*10
        #updating the list with the finished calcs
        percentage.append(cost)

    #third set of for loops to help build out the displays of the graph
    #using range() to generate the numbers 100, 90, 80... 0 without needing a list. Using -1 instead of 0 beacue range stops before the end value
    for row_vaule in range(100, -1, -10):
        #adding in a new line on the graph with the row value and a |
        graph += f"{row_vaule}".rjust(3) + "| "
        for percent in percentage:
            if percent >= row_vaule:
                graph += "o  "
            else:
                graph += "   "
        #adding in a new line regardless, once per row, after all categories are done
        graph += "\n"
    
    #using f"" to help format the break bar in the graph axis
    # 4 spaces to align with row labels, then dashes spanning each category (3 chars wide) plus 1 extra
    graph += f"".rjust(4) + "-" * (len(categories) * 3 + 1) + "\n"

    #calcuated max length of any given category for the fourth for loop
    max_len = max(len(category.name) for category in categories)

    #due to FCC wanting the formating a certian way I had to introduce this placeholder list for the fourth for loop
    #we are using this to collecting rows into a list so we can join them with "\n".join() which adds newlines between rows but not after the last one (happens at end of this last for loop)
    name_rows = []
    
    #fourth set of for loops to build out the vertical naming of the graphs x axis
    #looping through each row from 0 to the max length based on category name size
    for index in range(max_len):
        #creating a placeholder variable to store the formating of the for loop
        row=""
        # at the start of the index added in this right side adjustment before we start updating the graph for formating
        row += f"".rjust(5)
        #looping through each category for each row since this is nested inside the first for loop
        for category in categories:
            #comparing the current itteration of the index to the length of the category name
            if index < len(category.name):
                #if that index is less than the name length than we can slice out the letter at that index and add it to the graph
                row += category.name[index] + "  "
            else:
                #if the index is greater than or equal to the name length than we can add in spacing as a placeholder
                row += "   "
        #due to FCC formating we are then appending this row result to the name_rows placeholder list we made at the end of the current index
        name_rows.append(row)
    
    #Here we are adding the new list FCC required for formating to the end of the graph to complete this lab and get us the desired vertical text formating
    # "\n".join() combines all rows with newlines between them but no trailing newline at the end, which is required for FCC formating
    graph += "\n".join(name_rows)
    
    #return graph at the very end so we can get the full picture
    return(graph)


#test of the class    
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(10.69, "testing a shirt")
auto = Category("Auto")
food.transfer(100, auto)
auto.withdraw(42.35, "gas money")
print(food)
print(clothing)
print(auto)

#test of the graph
#this needs to be in a list because we are looking for 1 input to iterate through rather than a bunch of indiviual objects so we make a list of objects
print(create_spend_chart([food, clothing, auto]))