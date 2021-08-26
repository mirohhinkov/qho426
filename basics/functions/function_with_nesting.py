# function definition
def identify():
  seen = input("What do you see before us ")
  if seen == "a large boulder":
    print("It's time to run!")
  else:
    print("We will be fine.")

#function call
def run():
  identify()

if __name__ == "__main__":
  run()