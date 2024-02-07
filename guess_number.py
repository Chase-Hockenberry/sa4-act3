number = '10'

print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")

def guess_num(guess):
    if guess == number:
        print("Congratulations! You guessed the right number.")
    else:
        guess = input(f"Sorry! try again (Enter 'q' to exit): ")
        if guess == 'q':
            print(f"The number was {number}.")
        else:
            guess_num(guess)

guess_num(guess)