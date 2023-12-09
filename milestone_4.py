import random
fruits=["apple","kiwi","grapes","banana","orange"]
word_list=fruits

class Hangman():
    def __init__(self,word,word_guessed,num_letters,num_lives,word_list,list_of_guesses)
        self.word = word
        self.word_list = word_list
        self.word_guessed = word_guessed
        self.num_letters = num_letters
        self.num_lives = num_lives
        self.list_of_guesses = list_of_guesses

def check_guess(self.guess):
    guess=guess.lower()
    if guess in self.word:
        print("Good guess! {guess} is in the word.")

def ask_for_input(self,guess):
    guess=input()
    while TRUE:
        if guess.isalpha() and len(guess) != 1
            print("Invalid letter. Please, enter a single alphabetical character.")
            continue
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
            continue
        else:
            self.list_of_guesses.append(guess)
            break


            




