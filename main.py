# Create the function for reading passwords
def read():
    # Open the passwords.txt document as "r" to read it
    with open ("passwords.txt", "r") as file:
        
        # Assign the contents of the file into a variable called "content"
        content = file.read()
        
        # Print the content variable
        print (content)


# Create the function for adding passwords
def create():
    
    # Ask the user for the password info
    pwd = input("Please list the password and service it is used for. ")
    
    # Open or create the passwords.txt document to store the passwords
    with open ("passwords.txt", "a") as file:
        
        # Write the variable to the file on a new line
        file.write (pwd + "\n")
        
# Create the function for printing the intro
def print_intro():
    print ("Welcome to password manager! ")
    print ("When adding passwords, first add the service it is used for then the password its self. ")
    
# Create the example function
def example():
    print ("Example: ")
    print ("randomwebsite.com | Randompassword1! ")

# Use the "example" and "print_intro functions"
print_intro
example

# Create a while loop
while True:
    
    # Ask the user if they would like to read or create passwords
    choice = input ("Would you like to add a new password, or view passwords? If you would like to quit press Q. (add, view) ")
    
    # Quit the app if user chose "q"
    if choice == "q":
        break
    
    # Run the create function if user has decided to add passwords
    elif choice == "add":
        create()
        
    # Run the read function if user has decided to vuiw passwords
    elif choice == "view":
        read()
    
    # Break the loop if the user gives a invalid input    
    else:
        print ("Invalin Input: Please Retry. ")