#In this workshop, you are going to build an Email Simulator that simulates sending, receiving, and managing emails between different users.
#the User class owns an ibox and can send emails, the Inbox class stores Email objects and retrieves them by index, the Email class holds data (sender, subject, ect.) knows how to display itself and knows if its been read
#we are creating objects, storing objects, and calling methods on those objects

#importing a time library so that we can add time stamps
import datetime

# Represents a single email message.
# This class stores all data related to an email (sender, receiver, subject, body, timestamp)
# and also defines behaviors (methods) for interacting with that email (mark as read, display)
# Each Email object is independent. Even though all emails use the same class blueprint, each instance has its own unique data (sender, subject, timestamp, etc.)
class Email:
    
    # Constructor: runs when a new Email object is created. This stores all relevant data for that specific email instance
    # Each Email object represents one unique message
    # sender and receiver are User objects, not just names. This allows us to access their attributes (like .name) and behavior
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.datetime.now()
        self.read = False
    
    # method that marks the email as read by updating its internal state
    def mark_as_read(self):
        self.read = True

    #this method both changes state (read=True) and outputs formatted information (full context of the email)
    def display_full_email(self):
        self.mark_as_read()
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    #method defines how the Email object is represented as a string (Provides a short summary view instead of full details)
    #Automatically used when printing the object (e.g., inside list_emails) due to it being a __str__
    def __str__(self):
        status = 'Read' if self.read else 'Unread'
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

#second class created to cover the functions of the inbox
#the Inbox does not create Email objects. It only stores and manages Email objects created elsewhere (by User)
class Inbox:
    
    #used to initalize an empty inbox in the form of a list (stores Email objects in this list format)
    #self.emails will store Email objects as they are received
    def __init__(self):
        self.emails = []

    #method used to recive emails
    def receive_email(self, email):
        self.emails.append(email)

    #method used to check your inbox 
    def list_emails(self):
        #check if email list is empty
        if not self.emails:
            print('Your inbox is empty.\n')
            return
        print('\nYour Emails:')
        #used to generate a list of emails with an index tied to each one for reference later on
        for i, email in enumerate(self.emails, start=1):
            #printing the email object automatically calls its __str__ method
            print(f'{i}. {email}')

    #method used to read emails
    def read_email(self, index):
        #checking to see if the inbox is empty
        if not self.emails:
            print('Inbox is empty.\n')
            return
        #this converts "user-friendly" index (starting at 1) to Python list index (starting at 0)
        actual_index = index - 1
        #checking to see if the index exisits within our email list
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        # assuming it passes all tests then we can use the read email method to call the display method from the email class and "read" the email
        # Accesses a specific Email object from the list and calls its method. This works because each item in self.emails is an Email object
        self.emails[actual_index].display_full_email()

    #method used to delete emails
    def delete_email(self, index):
        #check if inbox is empty again
        if not self.emails:
            print('Inbox is empty.\n')
            return
        #converting the actual index back to a 0 based count again
        actual_index = index - 1
        #checking to see if the index exisits within our email list
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        #assuming all test pass then we delete the email of the current index reference
        del self.emails[actual_index]
        #added a print to verify that the delete actually happened
        print('Email deleted.\n')
        
#third class created to cover user creation as well as user interactions with the inbox/emails
class User:
    #inital method used to create the object for the user class
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()

    #method to send an email
    def send_email(self, receiver, subject, body):
        # Creates a new Email object representing the message being sent
        # 'self' becomes the sender, and the receiver is passed in. This is how objects interact: by passing references to each other
        #the 'email' variable holds a reference to the Email object. This same object is passed to the receiver's inbox (not copied)
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        # receiver... is what is actually "delivers" the email to the receiver's inbox
        # "Sending" the email means adding it to the receiver's inbox. No real networking happens (we are just passing the Email object)
        # we pass the Email object to the receiver's inbox, which stores it for later access
        receiver.inbox.receive_email(email)
        #added a print to verify that the email was sent
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    #method to check the user's inbox
    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    #method to read a given email in the users inbox based on the given index
    def read_email(self, index):
        self.inbox.read_email(index)

    #method used to delete a given email from the users inbox based on the given index
    def delete_email(self, index):
        self.inbox.delete_email(index)

#main function we are using to call the classes and use the structure that we built
def main():
    #creating our user objects
    tory = User('Tory')
    ramy = User('Ramy')        

    # Calling methods on User objects to simulate sending emails between users (in the formate of object.method)
    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')
    
    #in the formate of object.method we are able to perform a "inbox check" of check, read, delete, re-check
    ramy.check_inbox()
    ramy.read_email(1)
    ramy.delete_email(1)
    ramy.check_inbox()

# Ensures main() only runs when this file is executed directly, not when it is imported as a module
if __name__ == '__main__':
    main()