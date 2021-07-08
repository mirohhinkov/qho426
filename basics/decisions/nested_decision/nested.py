# User input for book type
book_type = input('What type of cover does the book have? ')

#chech if it is soft
if (book_type == 'soft'):
  bound = input('Is the book perfect-bound? ')
  if(bound == 'yes'):
    print('Soft cover, perfect bound books are very popular!')
  else:
    print('Soft covers with coils or stitches are great for short books')
else:
  print('Books with hard covers can be more expensive!')