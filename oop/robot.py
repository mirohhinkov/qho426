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

  def grow(self):
    self.age += 1
    return self

  def eat(self, amount):
    self.energy += amount
    self.energy = 100 if self.energy > Robot.MAX_ENERGY else self.energy
    return self

  def move(self, distance):
    self.energy -= distance
    self.energy = 0 if self.energy < 0 else self.energy
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