print("""
Please select an option

1. Nice message
2. Area of rectangle
3. Area of triangle
4. Multiplication table

[Enter 1-4]: """, end='')

option = int(input())
if option == 1:
  print('You look nice today')
elif option == 2:
  length = float(input('Enter the length of the rectangle: '))
  width = float(input('Enter the width of the rectangle: '))
  print(f"Area of {length} by {width} rectangle is: {length*width}")
elif option == 3:
  base = float(input('Enter the base of the triangle: '))
  height = float(input('Enter the height of the triangle: '))
  print(f"Area of triangle with base {base} and height {height} is: {height*base/2}")
elif option == 4:
  number = int(input('Enter the number: '))
  for i in range(1, 10):
    print(f"{i} x {number} = {i*number}")
else:
  print('Unrecognized instruction')