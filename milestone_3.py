import random
word_list = ["apple","kiwi","grapes","banana","orange"]
word = random.choice(word_list)
def check_guess(guess):
    if guess in word:
        print('Good guess! {guess} is in the word.'.format(guess = guess))
    else:
        print('Sorry, {guess} is not in the word. Try again'.format(guess = guess))
def ask_for_input():
    guess = str(input('Enter single letter: '))
    guess = guess.lower()
    if len(guess) == 1 and guess.isalpha():
        check_guess(guess)
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')
while True:
    ask_for_input()