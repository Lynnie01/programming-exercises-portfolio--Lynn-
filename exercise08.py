###8.Simple Search

# Write the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Ask  for a name to search for
search_name = input( "Write the name you want to search for: ")

# Search for the user-specified name
if search_name in names:
    print(f"{search_name} is in the list!")
else:
    print(f"{search_name} is not in the list.")
        
