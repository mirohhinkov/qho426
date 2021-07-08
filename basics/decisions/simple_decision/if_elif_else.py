#User input for direction
direction = input('Which direction have I got to paint? (up, down, left or right): ')

#Check and print appropriate message
if (direction == 'up'):
  print('I am painting upward!')
elif (direction == 'down'):
  print('I am painting downward!')
elif (direction == 'left'):
  print('I am painting leftward!')
elif (direction == 'right'):
  print('I am painting rightward!')
else:
  print('Unknown direction!')