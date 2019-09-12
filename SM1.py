import random
letters_guessed = list()
import time

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''


    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''

#Decide whether all letters in secret word are guessed. Checks if game is "over."
    for key in secret_word:
        if key not in letters_guessed:
            return False
    return True

    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed √

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet √
    # Keeps tracks of letters. Prevents duplicates.
    already_guessed = []
    for key in secret_word:
        if key in letters_guessed:
            already_guessed.append(key)
        else:
            already_guessed.append("_") # Appends an underscore as placeholder for every letter not guessed in word yet.
    return already_guessed

def is_guess_in_word(attempt, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word. √
    if attempt in secret_word:
        return True
        print('Correct! You guessed right. Guess again!')
    else:
        return False
        print('Sorry your guess was incorrect. Try again.')

def play_again():
    end_of_game = input("Would you like to play again? Y or N: ")
    if end_of_game == "Y" or end_of_game == "y":
        print("\n\nOk Good luck!\n")
        return True
    elif end_of_game == "N" or end_of_game == "n":
        print("\n\nOk! :)\n")
        return False
    else:
        print("\n\nPlease type in either Y or N.\n")

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''

    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    counter = 7
    letter_bank = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    print("You will have 7 tries.")
    # print(secret_word) prints out secret word for test purposes

    while counter >= 0:

        attempt = input("Guess: ")

        if len(attempt) != 1:
            print("Please type one letter.")

        if attempt not in letter_bank:
            print("You have already used this letter.")
            print(''.join(get_guessed_word(secret_word, letters_guessed)))
            continue

        if attempt in letter_bank:
            letter_bank.remove(attempt)

        if is_guess_in_word(attempt, secret_word) == True:
            letters_guessed.append(attempt)
            print("\nGOOD GUESS! Your guess was in the word.")
            print("Your word guessed so far: " + ''.join(get_guessed_word(secret_word,letters_guessed)))
            if is_word_guessed(secret_word, letters_guessed):
                print(f"\nYOU WIN!\nSecret word = [ {secret_word} ]\n")
                break

            print("Letters available: " + ''.join(str(c) for c in letter_bank))
            print("-----------\n")

        else:
            if counter == 0:
                print(f"\n\nYOU LOST\nThe secret word was [ {secret_word} ]\n")
                break

            else:
                counter -= 1
                print(f"\nYour guess was not in the word!\nYou have {counter + 1} attempts left.")
                print(''.join(get_guessed_word(secret_word, letters_guessed)))
                print("These letters are available: " + ''.join(str(c) for c in letter_bank))
                print("-----------\n")
    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost
print("Welcome to Spaceman")
            # personalized feature to make the game better.
name = input("what is your name? ")
print("Hello, " + name, "Let's play!")
print("******************")
print("Guess the correct word and win the game. Relax, and Have fun!")
time.sleep(1)

is_running = True
while is_running == True:
    secret_word = load_word()
    spaceman(secret_word)
    is_running = play_again()

#These function calls that will start the game
