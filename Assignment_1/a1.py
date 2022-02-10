import random as rand

num = rand.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
while(not(guess == num)):
    if(guess < 1 or guess > 100):
        print("\nInvalid number, try again!")
    else:
        if(guess < num):
            print("\nSorry, too low -- try a higher number")
        elif(guess > num):
            print("\nSorry, too high -- try a lower number")
    guess = int(input("\nGuess a number between 1 and 100: "))

print("\nYou got it!")
