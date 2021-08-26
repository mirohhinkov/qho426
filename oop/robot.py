class Robot:

  # class variables
  MAX_ENERGY = 100

  # construcror
  def __init__(self):
    self.name = "Robot"
    self.age = 0
    self.energy = 0

  # instance methods
  def display(self):
    print(f"I am {self.name}")
    return self

  # dunders
  def __repr__(self):
    return f"robot(name={self.name}, age={self.age})"

  def __str__(self):
    return f"Robot {self.name} is {self.age} years old."


#tests
if __name__ == "__main__":
  robot = Robot()
  robot.display() 