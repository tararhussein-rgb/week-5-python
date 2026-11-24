# guess_game.py

# Choose a secret number between 1 and 20
secret_number = 14  
attempts = 0

print("--- Welcome to the Guessing Game! ---")
print("I have chosen a number between 1 and 20. Try to guess it!")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You got it in {attempts} tries!")
            break
    except ValueError:
        print("Please enter a valid integer.")