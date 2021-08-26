# function definition
def  climb_ladder(to_do, done):
  if to_do > done:
    print("Still some way to go!")
  else:
    print("We are almost there!")    


#function calls
def run():
  climb_ladder(5, 2)
  climb_ladder(2, 5)

if __name__ == "__main__":
  run()