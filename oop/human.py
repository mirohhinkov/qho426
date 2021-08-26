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

  # dunders
  def __repr__(self):
    return f"human(name={self.name}, age={self.age})"

  def __str__(self):
    return f"Human {self.name} is {self.age} years old."

if __name__ == "__main__":
  human = Human()
  human.display()

