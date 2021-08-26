# User inputs
def run():
  cables = int(input("How many bars should be charged? "))

  #setting counter
  counter = 0
  #the loop
  while counter < cables:
    print(f"Charging: {(counter + 1) * '█'}")
    counter += 1
  # Final message
  print("The battery is fully charged.")

if __name__ == "__main__":
  run()