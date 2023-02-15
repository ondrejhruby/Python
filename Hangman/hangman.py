import random

# List of words to choose from
word_list = ["python", "java", "javascript", "ruby", "perl"]
wordCount = []

# Function to display the hangman
def display_hangman(num_incorrect):
    hangman = [
        " _________     \n" +
        "|         |    \n" +
        "|              \n" +
        "|              \n" +
        "|              \n" +
        "|              \n" +
        "|              \n",
        " _________     \n" +
        "|         |    \n" +
        "|         0    \n" +
        "|              \n" +
        "|              \n" +
        "|              \n" +
        "|              \n",
        " _________     \n" +
        "|         |    \n" +
        "|         0    \n" +
        "|         |    \n" +
        "|              \n" +
        "|              \n" +
        "|              \n",
        " _________     \n" +
        "|         |    \n" +
        "|         0    \n" +
        "|        /|    \n" +
        "|              \n" +
        "|              \n" +
        "|              \n",
        " _________     \n" +
        "|         |    \n" +
        "|         0    \n" +
        "|        /|\   \n" +
        "|              \n" +
        "|              \n" +
        "|              \n",
        " _________     \n" +
        "|         |    \n" +
        "|         0    \n" +
        "|        /|\   \n" +
        "|        /     \n" +
        "|              \n" +
        "|              \n",
        " _________     \n" +
        "|         |    \n" +
        "|         0    \n" +
        "|        /|\   \n" +
        "|        / \   \n" +
        "|              \n" +
        "|              \n"
    ]
    print(hangman[num_incorrect])

# Function to display the word with underscores for unguessed letters
def display_word(word, guesses):
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter + " "
        else:
            display += "_ "
    return display

# Function to play the game
def play_game():
    pickedWord = random.choice(word_list)
    guesses = []
    num_incorrect = 0
    max_incorrect = 6
    while num_incorrect < max_incorrect and "_" in display_word(pickedWord, guesses):
        display_hangman(num_incorrect)
        display_word(pickedWord, guesses)
        guess = input("Guess a letter: ").lower()

#play the game
play_game()