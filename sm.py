import time
letters_guessed = []

print("Welcome to Spaceman, you will have 7 tries.")

# personalized feature to make the game better.
name = input("what is your name? ")

print("Hello, " + name, "Let's play!")
print("******************")
print("Guess the correct word and win the game. Relax, and Have fun!")
time.sleep(1)

input("Guess: ")

def load_word():

    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    #words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    guess  = 0
    while guess <= 7:
        secretLetters = list(secretWord)
        secretWordLen = len(secretLetters)
        letters_guessed.append(letter)

        print('Letters guessed so far: ', letters_guessed)

        if letter not in secretLetters:
            guess += 1

        while letter in secretLetters:
            secretLetters.remove(letter)
            
        if secretLetters == []:
            return True

    return False
