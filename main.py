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
        