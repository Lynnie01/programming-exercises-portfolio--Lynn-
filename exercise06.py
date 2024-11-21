###6.Brute Force Attack

# Define the correct password
correct_password = "12345"

# put the  the maximum number of attempts
max_attempts = 5
attempts = 0

# Use a while loop to repeatedly ask the user for the password
while attempts < max_attempts:
    password = input("Enter the password: ")
    
    if password == correct_password:
        print("Welcome back!")
        break  # Exit the loop if the password is correct
    else:
        attempts += 1 
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        else:
            print("Maximum attempts reached. Authorities have been alerted.")
