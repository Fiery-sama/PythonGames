# importing the random module
import random

# defining the greetings() function
def greetings():
    # defining the username variable
    username = input("""
                    ==================================================
                    > Welcome to the Hangman Game! Enter your name:  <
                    """).capitalize()
    
    # using a decision making process to accept only alphabets as name
    if username.isalpha() == True:
        print("""
                >> Hello,""", username + """!""", """We are glad to have you here! <<
                You will be playing against the computer today. The computer will 
                randomly choose a word and you will try to guess the correct word
                You can always invite the friends for a fun time together
                ==================================================================
                Good Luck! Have fun playing
            """)
    
    else:
        print('Please enter a valid name using alphabets only')
        username = input('Enter a game name here:   ')
        print('Hello, ' + username + '! Please go through the rules of the game below:')

# defining the playAgain() function
def playAgain(): 
    """
    This function asks user/player if they wish to replay the hangman game
    """
    userResponse = input('Would you like to play again? Y or N: ').lower()

    # creating a decision making process
    if userResponse == 'y':
        gameRun()
    else:
        print('Hope you had fun playing this game. See you next time!')

# defining the getWord() function
def getWord():
    """
    This function produces the word the user will attempt guessing
    """
    listOfWords = ['Apple', 'Banana', 'Papaya', 'Mango', 'Kiwi', 'Orange', 'Pineapple', 'Grapes', 'Cherry', 'Watermelon']

    return random.choice(listOfWords).lower()

# defining the gameRun() function
def gameRun():
    # calling the greeting() function
    greetings()

    # defining the 'alphabet' variable
    alphabet = ('abcdefghijklmnopqrstuvwxyz')

    # getting a random word from the getWord() function
    randomWord = getWord()

    # initiating an empty list for guessed letter
    guessedLetters = []

    # initiating the 'attempts' variable for the number of attempts by the user
    attempts = 6

    # setting initial guess to False
    guess = False

    # empty line
    print()

    # printing a guess hint for the user for number of letters consisted in the word
    print('The Word consists of', len(randomWord), 'letters.')
    print(len(randomWord) * '_')

    while guess == False and attempts > 0:
        print('You have ' + str(attempts) + ' attempts')
        userGuess = input('Guess a letter in the word or enter the full word: ').lower()
        # user inputs a letter
        if len(userGuess) == 1:
            if userGuess not in alphabet:
                print('You are yet to enter a letter. Consider checking your entry and make sure you enter an alphabet not a number.')
            elif userGuess in guessedLetters:
                print('You have already guessed that letter before. Try again!')
            elif userGuess not in randomWord:
                print('Oops! that letter is not a part of a word.')
                guessedLetters.append(userGuess)
                attempts -= 1
            elif userGuess in randomWord:
                print('Awesome! This letter is present in the word!')
                guessedLetters.append(userGuess)
            else:
                print('Invalid Input! You might have entered the wrong entry.')
            
        # user inputs the full word
        elif len(userGuess) == len(randomWord):
            if userGuess == randomWord:
                print('Awesome! You guessed the word correctly!')
                guess = True
            else:
                print('Oops! that was not the word we were looking for.')
                attempts -= 1
        
        # user inputs letter and it is not equal to the total
        # number of letters in the word to guess
        else:
            print('The length of the guess is not the same as the length of the word.')
            attempts -= 1

        the_status = ''
        if guess == False:
            for letter in randomWord:
                if letter in guessedLetters:
                    the_status += letter
                else:
                    the_status += '_'
            print(the_status)

        if the_status == randomWord:
            print('Awesome! You guessed the word correctly!')
            guess = True
        elif attempts == 0:
            print('Unfortunately! You ran out of guesses and you couldn\'t guessed the word.')
    
    # initiating the playAgain() function if user wishes to continue
    playAgain()

# executing the program
gameRun()