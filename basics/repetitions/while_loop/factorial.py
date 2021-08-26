#user input - number 
def run():
  num = int(input("Please enter a number: "))
  #setting counter
  counter = 1
  #setting initial factorial
  f0 = 1
  #the loop
  while counter < num + 1:
    f0 *= counter
    counter += 1
  #final outpur
  print(f"The factorial is {f0}")

if __name__ == "__main__":
  run()