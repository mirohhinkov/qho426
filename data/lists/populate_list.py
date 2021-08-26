from simple_list import directions

dirs = directions()

def menu():
  for i in range(len(dirs)):
    print(f"{i}: {dirs[i]}")
  while True:
    try:
      choice = int(input("Please select a direction: "))
      if choice in range(len(dirs)):
        return choice
      raise Exception("Out of range")
    except:
      print(f"Please, choose a number from 0 to {len(dirs) - 1}")
  return choice


def run():
  print("Working out escape route...\n")
  route = [dirs[menu()] for i in range(5)]
  print(f"Escape route: {route}")

if __name__ == "__main__":
  run()