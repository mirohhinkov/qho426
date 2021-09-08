class Human:
  # class variables
  MAX_ENERGY = 100
  # construcror
  def __init__(self):
    self.name =  "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY


  @property
  def energy(self):
      return self.__energy

  @energy.setter
  def energy(self, x):
      if x < 0:
          self.__energy = 0
      elif x > Human.MAX_ENERGY:
          self.__energy = Human.MAX_ENERGY
      else:
          self.__energy = x


  #instance methods
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
    return f"human(name={self.name}, age={self.age})"

  def __str__(self):
    return f"Human {self.name} is {self.age} years old.\nEnergy: {self.energy}"

if __name__ == "__main__":
  human = Human()
  human.display()
  human.name = "Miro"
  human.age = 20
  human.move(10).eat(5).grow().eat(50)
  print(human)

