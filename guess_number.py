number = '10'

print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")

def guess_num(guess):
    if guess == number:
        print("Congratulations! You guessed the right number.")
    else:
        if int(guess) > int(number):
            guess = input(f"Too high! try again (Enter 'q' to exit): ")
        if int(guess) < int(number):
            guess = input(f"Too low! try again (Enter 'q' to exit): ")
        if guess == 'q':
            print(f"The number was {number}.")
        else:
            guess_num(guess)

guess_num(guess)