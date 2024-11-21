###4.Primitive Quiz

# Ask the user a question 
answer = input("What is the capital of France? ")

# Look at the answer and add feedback
if answer.lower() == "paris":
    print("Correct! Paris is the capital of France.")
else:
    print("Wrong answer. The correct answer is Paris.")

# List of the questions and the correct answers
questions = [
    ("What is the capital of Italy?", "Rome"),
    ("What is the capital of Greece?", "Athens"),
    ("What is the capital of Poland?", "Warsaw"),
    ("What is the capital of Portugal?", "Lisbon"),
    ("What is the capital of Turkey?", "Ankara"),
    ("What is the capital of Spain?", "Madrid"),
    ("What is the capital of Norway?", "Oslo"),
    ("What is the capital of the UK?", "London"),
    ("What is the capital of Finland?", "Helsinki"),
    ("What is the capital of Germany?", "Berlin")
]

# Adding a loop to ask each question
for question, correct_answer in questions:
    answer = input(question + " ")

    # Ignoring capitalization and checking the answer
    if answer.lower() == correct_answer.lower():
        print("Correct!")
    else:
        print(f"Wrong. The correct answer is {correct_answer}.")
