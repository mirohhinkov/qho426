def movements():
  return ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]

def run():
  print("Moving...")
  path = movements()
  for i in range(len(path)//2):
    print(f"{path[2 * i]} for {path[2 * i + 1]} steps")

if __name__ == "__main__":
  run()