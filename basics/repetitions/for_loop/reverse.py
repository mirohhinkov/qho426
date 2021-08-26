# user phrase
def run():
  phrase = input("What phrase do you see? ")

  print("\nReversing...\n")
  print(phrase[::-1])
  for i in range(len(phrase),0,-1):
    print(phrase[i-1], end="")

  print("\nReversing...\n")
  for i in range(len(phrase)):
    print(phrase[-i-1], end="")

  # final message
  print("\n\nDone!")

if __name__ == "__main__":
  run()