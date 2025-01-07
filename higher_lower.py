# Importing modules
import game_art
import game_database
import random

# Color constants
BRIGHT_BLUE = '\033[94m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_MAGENTA = '\033[95m'
RESET = '\033[0m'

# Game constants
GAME_TITLE = game_art.higher

# Function to format person info
def format_person_info(account):
    """Returns a formatted string with person's name, description, and country."""
    return f"{account['Name']}, a {account['Description']}, from {account['Country']}"

# Function to check answer
def check_answer(guess, account1, account2):
    """Returns True if the guess is correct, False otherwise."""
    follower_count1 = account1['Followers']
    follower_count2 = account2['Followers']

    if follower_count1 > follower_count2:
        return guess == 1
    else:
        return guess == 2

# Main game loop
def game_loop():
    print(f"{BRIGHT_MAGENTA}{GAME_TITLE}{RESET}")
    score = 0
    continue_flag = True
    account2 = random.choice(game_database.data)

    while continue_flag:
        account1 = account2
        account2 = random.choice(game_database.data)
        while account1==account2:
             account2 = random.choice(game_database.data)
        print(f"{BRIGHT_BLUE}Compare 1: {format_person_info(account1)}{RESET}")
        print(f"{BRIGHT_YELLOW}{game_art.vs}{RESET}")
        print(f"{BRIGHT_BLUE}Compare 2: {format_person_info(account2)}{RESET}\n")

        guess = int(input("Who has more followers? Type 1 or Type 2: "))
        is_correct = check_answer(guess, account1, account2)

        if is_correct:
            score += 1
            print(f"{BRIGHT_GREEN}Your score is {score}{RESET}\n")
        else:
            print(f"{BRIGHT_GREEN}You are wrong! Your final score is {score}{RESET}\n")
            continue_flag = False

# Run the game
game_loop()
