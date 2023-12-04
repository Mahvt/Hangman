import random
fruits=["apple","kiwi","grapes","banana","orange"]
word_list=fruits
print(word_list)
word=random.choice(word_list)
print(word)
guess=input("")
if len(guess)==1 and guess.isalpha():
  print("Good guess!")
else:
  ("Oops! That is not a valid input.")