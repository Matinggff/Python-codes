import random
# Generate a random number between 1 and 100
def guess_the_number():
    
    secret_number = random.randint(1, 100)
    
    attempts = 0
    
    print("Number guessing game!")
    print("I have chosen a number between 1 and 100. Take a guess.")
    
    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < secret_number:
                print("My number is bigger. Guess again.")
            elif guess > secret_number:
                print("My number is smaller. Guess again.")
            else:
                print(f"congratulations! You guessed the right number. {secret_number} was my real number.")
                print(f"Number of attempts: {attempts}")
                break
        except ValueError:
            print("Please enter an integer.")

if __name__ == "__main__":
    guess_the_number()
