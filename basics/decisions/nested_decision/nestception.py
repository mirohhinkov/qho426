# User input for direction
direction = input('Where should I look? ')

#chech cases
if (direction == 'in the bedroom'):
  details = input('Where in the bedroom should I look? ')
  if(details == 'under the bed'):
    print('Found some shoes but no battery')
  else:
    print('Found some mess but no battery.')
elif (direction == 'in the bathroom'):
  details = input('Where in the bathroom should I look? ')
  if (details == 'in the bathtub'):
    print('Found a rubber duck but no battery.')
  else:
    print('Found a wet surface but no battery.')
elif (direction == 'in the lab'):
  details = input('Where in the lab should I look? ')
  if (details == 'on the table'):
    print('Yes! I found my battery!')
  else:
    print('Found some tools but no battery.')
else:
  print('I do not know where that is but I will keep looking.')