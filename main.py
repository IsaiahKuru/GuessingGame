import random

numberofGuesses = 0
number = random.randint(1,10000)

name = input("Hello! What is your name? ")

print(name + ", I am thinking of a whole number between 1 and 10000. Can you guess what it is?")

while numberofGuesses < 12:
  guess = input("Take a guess. ")
  guess = int(guess)

  numberofGuesses = numberofGuesses + 1;
  guessesLeft = 12 - numberofGuesses;

  if guess < number:
    guessesLeft=str(guessesLeft)
    print("Your guess is too low. You have " + guessesLeft + " guesses left.")

  if guess > number:
    guessesLeft=str(guessesLeft)
    print("Your guess is too high. You have " + guessesLeft + " guesses left.")

  if guess==number:
    break

if guess==number:
  numberofGuesses=str(numberofGuesses)
  print("Good job! You guessed the number in " + numberofGuesses +  "tries.")

if guess!=number:
  number=str(number)
  print("Sorry. The number I was thinking of was " + number )