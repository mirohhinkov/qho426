# user inputs
def run():
  print("Program Started!")
  code = int(input("Please enter an ASCII code: "))

  #program output
  if code >31 and code <128:
    print(f"The character represented by the ASCII code  {code} is: {chr(code)}")
  else: 
    print("This is not a standard ascii charachter")
  print("Program Ended!")

if __name__ == "__main__":
  run()