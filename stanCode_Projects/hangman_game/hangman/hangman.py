"""
File: hangman.py
Name: Jael Lin
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays hangman game.
    Users sees a dashed word, trying to
    correctly figure the un-dashed word out
    by inputting one character each round.
    If the user input is correct, show the
    updated word on console. Players have N_TURNS
    chances to try and win this game.
    """
    word = random_word()
    print('The word looks like: ', end="")
    n = len(word)
    for i in range(n):
        print('-', end="")
    print("")
    print('You have ' + str(N_TURNS) + ' guesses left.')
    guess = input('Your guess: ')
    guess = guess.upper()
    turn = N_TURNS
    count = 0
    show = ""
    correct = ""
    while True:
        ans = ""
        n = len(word)
        if guess.isalpha():
            if len(guess) >= 2:
                print('illegal format.')
            else:
                if word.find(guess) != -1:
                    print('You are correct!')
                    for i in range(n):
                        if guess == word[i]:
                            if correct.find(guess) == -1:
                                count += 1
                    correct += guess
                    if count == n:
                        print('You win!!')
                        print('The word was: ' + word)
                        break
                else:
                    if word.find(guess) == -1:
                        turn -= 1
                    print('There is no ' + guess + '\'s in the word.')
                    if turn == 0:
                        print('You are completely hung :(')
                        print('The word was: ' + word)
                        break
                if len(show) > 0:
                    for i in range(n):
                        if guess == word[i]:
                            ans += guess
                        else:
                            ans += show[i]
                else:
                    for i in range(n):
                        if guess == word[i]:
                            ans += guess
                        else:
                            ans += "-"
                show = ans
                print('The word looks like: ' + show)
                print('You have ' + str(turn) + ' guesses left.')
        else:
            print('illegal format.')
        guess = input('Your guess: ')
        guess = guess.upper()


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
