import random

# Define a dictionary with country-capital pairs and hints
flash_cards = {
    "France": {"answer": "Paris", "hint": "It's known as the City of Love"},
    "Germany": {"answer": "Berlin", "hint": "It rhymes with Merlin"},
    "Italy": {"answer": "Rome", "hint": "It's home to the Colosseum"},
    "Spain": {"answer": "Madrid", "hint": "It has a famous football team"},
    "United Kingdom": {"answer": "London", "hint": "It has the Big Ben"}
}

# Convert the dictionary items to a list and shuffle it
flash_cards_items = list(flash_cards.items())
random.shuffle(flash_cards_items)

# Initialize the score counter
score = 0

# Iterate over the shuffled flash cards
for country, details in flash_cards_items:
    # Display the prompt and ask the user to input their response
    user_answer = input(f"What is the capital of {country}? ")
    
    # If the user's answer is incorrect, provide a hint and ask again
    if user_answer.strip().title() != details["answer"]:
        print("Hint:", details["hint"])
        user_answer = input(f"Try again. What is the capital of {country}? ")
    
    # Check if the user's answer is correct after the hint
    if user_answer.strip().title() == details["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {details['answer']}.\n")

# Calculate the total number of flash cards
total_flash_cards = len(flash_cards_items)

# Calculate the percentage of correct answers
percentage_correct = (score / total_flash_cards) * 100

# Display the final score and percentage
print(f"You got {score} out of {total_flash_cards} correct ({percentage_correct:.2f}%).")