limit = 5
number = '10'

print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")

for i in range(limit):
    if guess == 'q':
            print(f"The number was {number}.")
            break
    if guess != number:
        if int(guess) > int(number):
            guess = input(f"Too high! You have {limit - i} more guesses (Enter 'q' to exit): ")
            continue
        if int(guess) < int(number):
            guess = input(f"Too low! You have {limit - i} more guesses (Enter 'q' to exit): ")  
            continue
    if guess == number:
            print("Congratulations! You guessed the right number.")
            break