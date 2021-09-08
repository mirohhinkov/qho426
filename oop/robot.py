class Robot:

  # class variables
  MAX_ENERGY = 100

  # construcror
  def __init__(self):
    self.name = "Robot"
    self.age = 0
    self.energy = 0
  

  @property
  def energy(self):
      return self.__energy

  @energy.setter
  def energy(self, x):
      if x < 0:
          self.__energy = 0
      elif x > Robot.MAX_ENERGY:
          self.__energy = Robot.MAX_ENERGY
      else:
          self.__energy = x

  # instance methods
  def display(self):
    print(f"I am {self.name}")
    return self

  def grow(self):
    self.age += 1
    return self

  def eat(self, amount):
    self.energy += amount
    return self

  def move(self, distance):
    self.energy -= distance
    return self

  # dunders
  def __repr__(self):
    return f"robot(name={self.name}, age={self.age}, energy={self.energy})"

  def __str__(self):
    return f"Robot {self.name} is {self.age} years old.\nEnergy: {self.energy}"


#tests
if __name__ == "__main__":
  robot = Robot()
  robot.display() 
  robot.name = 'Robi'
  print(robot)
  robot.eat(90).move(20).eat(50)
  print(robot)