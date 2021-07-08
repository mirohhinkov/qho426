# User input route
route = input('What type of adventure should I have? ')

#chech types
if (route == 'scary' or route == 'short'):
  print('Entering the dark forest!')
elif (route == 'safe' or route == 'long'):
  print('Taking the safe route!')
else:
  print('Not sure which route to take.')