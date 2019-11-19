import random
randomNumber= random.randint(0,101)
correctGuess= False
while correctGuess==False:
    str_guess= input("Guess a number 1-100")
    guess=int(str_guess)
    if guess==randomNumber:
        correctGuess=True
        print("Great guess! Correct guess")
    elif guess>randomNumber:
        print("Guess is too high")
    elif guess<randomNumber:
        print("Guess is too low")