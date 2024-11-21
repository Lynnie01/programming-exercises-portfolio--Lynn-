###3.Biography

# Ask the user for their name, hometown, and age 
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")

# Handling invalid age input
try:
    # Try to convert input to integer
    age = int(input("Enter your age (in numbers): "))  
except ValueError:
    # Notify user of invalid input
    print("Please enter a valid number for age!")  
    # Set age to None if it's not a number
    age = None  

# Store the information in the dictionary 
client_info = {"name": name, "hometown": hometown, "age": age}

# Print the values on separate lines 
print(f"Name: {client_info['name']}\nHometown: {client_info['hometown']}\nAge: {client_info['age'] if age is not None else 'N/A'}")
