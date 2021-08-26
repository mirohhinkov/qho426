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

if __name__ == "__main__":
  human = Human()
  human.display()

