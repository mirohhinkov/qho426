# function definition
def  display_ladder(steps):
  step="| |\n***\n"
  bottom = "| |\n"
  print(f"{steps * step}{bottom}")
  
def create_ladder():
  steps = int(input("How many steps remain "))
  display_ladder(steps)   


#function calls
def run(): 
  create_ladder()

if __name__ == "__main__":
  run()