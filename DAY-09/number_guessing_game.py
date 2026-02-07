import random

secret = random.randint(1 ,10)

guess = 0 


while guess != secret:
    guess = int(input("guess the number (1-10): \n"))
    if guess < secret:
        print("too low! , TRY AGAIN\n")
    elif guess > secret :
        print("too high! , TRY AGAIN \n")
    else:
        print("congrats! you learned it righgt bitch \n")

