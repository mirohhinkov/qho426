# function definition

def listen():
  sound = input("What sound did I hear? ")
  print(f"That was a loud {sound}!")

#function call
def run():
  listen()

if __name__ == "__main__":
  run()