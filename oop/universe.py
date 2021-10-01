from robot import Robot
from human import Human
from planet import Planet

from random import randint
import matplotlib.pyplot as plt


class Universe:
  def __init__(self):
    self.planets = []

  def generate(self):
    planet = Planet()
    for i in range(randint(0, 11)):
      planet.add_human(Human())
    for i in range(randint(0, 11)):
      planet.add_robot(Robot())
    self.planets.append(planet)
    return self

  def show_populations(self):
    x = []
    y = []
    # Generates x and y lists
    for i, planet in enumerate(self.planets):
      x.extend([f"H{i+1}", f"R{i+1}", i * ' '])
      y.extend([len(planet.inhabitants['humans']), len(planet.inhabitants['robots']), 0])

    #Labels
    plt.title("Universe planets")
    plt.xlabel("Humans and Robots for each planets")
    plt.ylabel("Number of inhabitants")

    barlist = plt.bar(x, y)
    # set red color for each human bar (defauls blue for robot bars)
    for i in range(len(self.planets)):
      barlist[3*i].set_color('r')
    plt.savefig('./bar.png') # for replit.com 
    # plt.show()
    # input("")
    # plt.close(barlist)

  def __str__(self):
    res = [repr(planet) for planet in self.planets]
    return '\n'.join(res)

if __name__ == '__main__':
  uni = Universe()
  uni.generate().generate().generate().generate().generate().generate().show_populations()