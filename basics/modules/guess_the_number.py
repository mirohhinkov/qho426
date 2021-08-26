from random import randrange

def play_guess_the_number():
  # User input for range limit
  while True:
    min_limit = int(input("Please enter the minimum value: "))
    print()
    max_limit = int(input("Please enter the maximum value: "))
    print()

    if max_limit - min_limit < 2:
      print("Too small range")
      continue
    break
  
  #generate number into user range
  rand_numb = randrange(min_limit, max_limit)

  #getting user guess
  print(f"I am thinking of a number between {min_limit} and {max_limit}. Can you guess what it is?", end = " ")
  while True:
    guest_number = int(input())

    if guest_number == rand_numb:
      print("\nCongratulations! You guessed my number!")
      break
    
    print("\nYour guess is too low.\n" if guest_number < rand_numb else "\nYour guess is too high.\n")
    print("Try again:", end = " ")



play_guess_the_number()