import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

def get_user_choice():
    while True:
        try:
            user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
            if user_choice in [0, 1, 2]:
                return user_choice
            else:
                print("Invalid input! Please type 0, 1, or 2.")
        except ValueError:
            print("Invalid input! Please type a number.")

# Тоглоомын үр дүнг шалгах
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        return "You win!"
    else:
        return "You lose!"

# Тоглоом эхлүүлэх
def play_game():
    user_choice = get_user_choice()
    computer_choice = random.randint(0, 2)  # Компьютерийн санамсаргүй сонголт
    print(f"\nYou chose:\n{game_images[user_choice]}")
    print(f"Computer chose:\n{game_images[computer_choice]}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Тоглоомыг ажиллуулах
play_game()
