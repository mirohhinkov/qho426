# User inputs
def run():
  cables = int(input("How many live cables should I avoid? "))

  #setting counter
  counter = 0
  #the loop
  while counter < cables:
    print(f"Avoiding...Done! {counter + 1} live cables avoided.")
    counter += 1
  # Final message
  print("All live cables have been avoided.")

if __name__ == "__main__":
  run()