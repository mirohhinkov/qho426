class Robot:

  # class variables
  MAX_ENERGY = 100

  # construcror
  def __init__(self):
    self.name = "Robot"
    self.age = 0
    self.energy = 0

  #instance methods
  def display(self):
    print(f"I am {self.name}")
    return self


#tests
if __name__ == "__main__":
  robot = Robot()
  robot.display() 