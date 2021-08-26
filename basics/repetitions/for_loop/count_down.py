# asking for distance

def run():
  dist = int(input("How far are we from the cave? "))

  # making steps
  for i in range(dist, 0, -1):
    print(f"{i} step{'s' if i > 1 else ''} remaining")

  # final message
  print("We have reached the cave!")

if __name__ == "__main__":
  run()