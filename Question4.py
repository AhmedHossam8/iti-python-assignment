import random
import sys


def helper():
    choice = input("Play again? (yes/no): ")
    if choice.lower() == "yes":
        main()
    elif choice.lower() == "no":
        sys.exit(0)
    else:
        print("Invalid choice")

print("Welcome to Number Guessing Game! \nI'm thinking of a number between 1 and 100. \nYou have 7 attempts.")
def main():
    num = random.randint(1, 100)
    print(num)
    guessed = 1
    while guessed <= 7:
        attempt = int(input(f"Attempt {guessed} - Your guess: "))
        if attempt < 0 or attempt > 100:
            print("Enter number between 1 and 100")
            continue
        
        if num - attempt > 0:
            print("Too low! Try again.")
            guessed += 1
        
        elif num - attempt < 0:
            print("Too high! Try again.")
            guessed += 1
        
        else:
            print(f"Congratulations! You guessed it in {guessed} attempts!")
            helper()
            
    print("Game Over")
    helper()
main()