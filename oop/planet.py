from robot import Robot
from human import Human

class Planet:
  def __init__(self):
    self.inhabitants = {
      'humans': [],
      'robots': []
    }
    self.name = 'Planet'
  

  def add_human(self, human):
    self.inhabitants['humans'].append(human)
    return self

  def remove_human(self, human):
    self.inhabitants['humans'].remove(human)
    return self

  def add_robot(self, robot):
    self.inhabitants['robots'].append(robot)
    return self

  def remove_robot(self, robot):
    self.inhabitants['robots'].remove(robot)
    return self

  def __repr__(self):
    return f'Planet (name = {self.name}, humans({[repr(h) for h in self.inhabitants["humans"]]}), robots({[repr(r) for r in self.inhabitants["robots"]]})'

  def __str__(self):
    return f'Planet: {self.name}\n\t{[repr(h) for h in self.inhabitants["humans"]]}\n\t{[repr(r) for r in self.inhabitants["robots"]]}'
  
if __name__ == '__main__':
  h1 = Human()
  h2 = Human()
  r1 = Robot()
  r2 = Robot()
  h1.name = 'Ivan'
  h2.name = 'John'
  r1.name = 'Robi'
  r2.name = 'Bobi'
  planet = Planet()
  planet.name = 'Earth'
  planet.add_human(h1).add_human(h2).add_robot(r1).add_robot(r2)
  print(planet.inha)
  print(repr(planet))
  print(planet)