# User inputs
def run():
  phrase = input("Please enter a phrase: ")

  #setting counter
  counter = 0
  #the loop
  while counter < len(phrase):
    print("Boop", end=" ")
    counter += 1
  print("")

if __name__ == "__main__":
  run()