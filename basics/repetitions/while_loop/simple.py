# User inputs
def run():
  cables = int(input("How many cables should I remove? "))

  #setting counter
  counter = 0
  #the loop
  while counter < cables:
    print("Removed cable.")
    counter += 1

if __name__ == "__main__":
  run()