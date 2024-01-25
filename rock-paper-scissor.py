import random

def rock_paper_scissors():
    rock = '''
            _______
        ---'   ____)
                (_____)
                (_____)
                (____)
            ---.__(___)
        '''

    paper = '''
            _______
        ---'   ____)____
                    ______)
                    _______)
                    _______)
            ---.__________)
        '''

    scissors = '''
            _______
        ---'   ____)____
                    ______)
                __________)
                (____)
            ---.__(___)
        '''

    x = 0  # rock
    y = 1  # paper
    z = 2  # scissors

    computer_game = random.randint(x, z)

    user_game = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))

    if 0 <= user_game <= 2:
        print(f"Computer chose:\n {eval(['rock', 'paper', 'scissors'][computer_game])}")

        if user_game == computer_game:
            print("Tie game")
        elif (user_game == 0 and computer_game == 2) or (user_game == 1 and computer_game == 0) or (
                user_game == 2 and computer_game == 1):
            print("You win!")
        else:
            print("You lose!")
    else:
        print("You typed an invalid number, please choose 0, 1, or 2.")

# Call the function
rock_paper_scissors()



#This function encapsulates the rock-paper-scissors game logic, and you can call it whenever you want to play the game. 
# The use of `eval` is used to dynamically select the corresponding ASCII art based on the computer's choice. 
# The function checks for valid input and prints the results of the game.