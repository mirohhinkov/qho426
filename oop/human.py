class Human:
  # class variables
  MAX_ENERGY = 100
  # construcror
  def __init__(self):
    self.name =  "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

  #instance methods
  def display(self):
    print(f"I am {self.name}")
    return self

  def grow(self):
    self.age += 1
    return self

  def eat(self, amount):
    self.energy += amount
    self.energy = 100 if self.energy > Human.MAX_ENERGY else self.energy
    return self

  def move(self, distance):
    self.energy -= distance
    self.energy = 0 if self.energy < 0 else self.energy
    return self

  

  # dunders
  def __repr__(self):
    return f"human(name={self.name}, age={self.age})"

  def __str__(self):
    return f"Human {self.name} is {self.age} years old."

if __name__ == "__main__":
  human = Human()
  human.display()

