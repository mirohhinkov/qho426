lives = int(input('Please enter the number of lives.\n'))
energy = int(input('Please enter the energy level.\n'))
shield = int(input('Please enter the shield level.\n'))
heart = '\u2764'
print(f"Lifes: {lives * heart}")
print(f"Energy: {energy * '♦'}")
print(f"Shield: {shield * '♦'}")
