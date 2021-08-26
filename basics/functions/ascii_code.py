# user inputs
def run():
  print("Program Started!")
  letter = input("Please enter a letter: ")

  #program output
  print(f"The ASCII code for {letter} is: {ord(letter)}")
  print("Program Ended!")

if __name__ == "__main__":
  run()