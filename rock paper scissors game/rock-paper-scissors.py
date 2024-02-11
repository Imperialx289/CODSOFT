import random

def get_user_choice():
    while True:
        user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!", 0
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!", 1
    else:
        return "Computer wins!", -1

def play_game():
    user_score = 0
    computer_score = 0
    print("Let's play Rock-Paper-Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}, computer chose {computer_choice}.")
        result, score = determine_winner(user_choice, computer_choice)
        print(result)
        if score == 1:
            user_score += 1
        elif score == -1:
            computer_score += 1
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

play_game()
