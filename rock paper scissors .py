import random
from colorama import init, Fore, Style

init(autoreset=True)

def color_choice(choice):
    """Return colored text for the given choice"""
    if choice == "rock":
        return Fore.RED + choice + Style.RESET_ALL
    elif choice == "paper":
        return Fore.BLUE + choice + Style.RESET_ALL
    elif choice == "scissors":
        return Fore.YELLOW + choice + Style.RESET_ALL
    else:
        return choice

def play():
    print(Fore.CYAN + "🎮 Welcome to Rock–Paper–Scissors!" + Style.RESET_ALL)
    choices = ["rock", "paper", "scissors"]

    while True:
        user = input("Choose rock, paper, or scissors: ").lower()
        if user not in choices:
            print("Invalid choice! Try again.")
            continue

        ai = random.choice(choices)
        print(f"\nYou chose {color_choice(user)}")
        print(f"Computer chose {color_choice(ai)}\n")

        if user == ai:
            print(Fore.MAGENTA + "It's a tie!" + Style.RESET_ALL)
        elif (user == "rock" and ai == "scissors") or \
             (user == "paper" and ai == "rock") or \
             (user == "scissors" and ai == "paper"):
            print(Fore.GREEN + "🎉 You win!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "😢 You lose!" + Style.RESET_ALL)

        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print(Fore.CYAN + "Thanks for playing! 👋" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    play()