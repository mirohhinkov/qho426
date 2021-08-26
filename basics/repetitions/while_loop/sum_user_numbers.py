#user input - number of numbers
def run():
  nums = int(input("How many numbers should I sum up? "))
  #setting counter
  counter = 0
  #setting initial sum
  sum = 0
  #the loop
  while counter < nums:
    num = float(input(f"Please enter your {counter + 1} number "))
    sum += num
    counter += 1
  #final outpur
  print(f"The answer is {sum}")

if __name__ == "__main__":
  run()