# user inputs
def run():
  rows = int(input("How many rows should I have? "))
  print()
  columns = int(input("How many columns should I have? "))
  print()

  smile = ":-)"

  print("\nHere I go:\n")
  for i in range(rows):
    for j in range(columns):
      print(smile, end=" ")
    print()

  # final message
  print("\nDone!")

if __name__ == "__main__":
  run()