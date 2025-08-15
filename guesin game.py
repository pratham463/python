import random
upper_bounds= 10
lower_bounds= 1
max_attempts= 12
random_number =random.randint(lower_bounds,upper_bounds)
def get_guess():
    while True:
        guess = int(input("guese a number between 1 to 10:"))
        if lower_bounds <= guess <= upper_bounds:

          return guess

        else:

          print("Invalid input. Please enter a number within the specified range.")

def check_guess(guess, random_number):

  if guess == random_number:

   return "Correct"

  elif guess < random_number:

   return "Too low"

  else:

   return "Too high"
def play_game():
 attempt = 0
 won = False
 while attempt < max_attempts:
       attempt +=1
       guess = get_guess()
       result = check_guess(guess, random_number)
       if result == "Correct":
          print(f"correct congragulatios you guesed the secret number{result}in{attempt}attempts")
          won = True
          break
       else:
           print(f"{result} try again")
 if not won:
    print("sorry you ran out of attempts")
if __name__ == "__main__":
    print ("welcome to number guesing game")
    play_game()