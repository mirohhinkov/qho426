# function definition
def  cross_bridge(distance):
  for i in range(distance):
    print("Crossed step")
  if distance > 5:
    print("The bridge is collapsing!")
  else:
    print("we must keep going!")    


#function calls
def run():
  cross_bridge(3)
  cross_bridge(6)

if __name__ == "__main__":
  run()