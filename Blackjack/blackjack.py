import random

# Function to get a new card
def get_card():
    card = random.randint(1, 11)
    return card

# Function to display the sum of the cards
def display_sum(player, sum):
    print("Player " + str(player) + " sum: " + str(sum))

# Function to play one round for a player
def play_round(player):
    sum = 0
    choice = "y"
    while choice == "y":
        card = get_card()
        sum += card
        display_sum(player, sum)
        if sum > 21:
            print("Bust!")
            break
        choice = input("Player " + str(player) + ", do you want another card (y/n)? ")
    return sum

# Function to play the game
def play_game():
    player1_sum = play_round(1)
    player2_sum = play_round(2)
    if player1_sum > 21:
        if player2_sum > 21:
            print("Both players bust. Tie.")
        else:
            print("Player 2 wins.")
    elif player2_sum > 21:
        print("Player 1 wins.")
    elif player1_sum > player2_sum:
        print("Player 1 wins.")
    elif player2_sum > player1_sum:
        print("Player 2 wins.")
    else:
        print("Tie.")

# Call the function to start the game
play_game()
