###10.Is it even?

def check_even_odd(number):
    # Checking  if the number is even or odd
    if number % 2 == 0:
        # sending a messge if the number is even 
        return "The number is even."
    else:
        #sending a message if the number is odd 
        return "The number is odd."

def main():
    # Telling the user to enter  a number 
    user_input = int(input("Enter a number: "))
    
    # checking the entered number to get the result
    result = check_even_odd(user_input)
    
    # Print the result given  check_even_odd
    print(result)
if __name__ == "__main__":
    main()
