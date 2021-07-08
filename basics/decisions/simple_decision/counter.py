#User input
n1 = int(input('Please enter the first integer number: '))
n2 = int(input('Please enter the second integer number: '))
n3 = int(input('Please enter the third integer number: '))

#Calculation
count = n1 % 2 + n2 % 2 + n3 % 2

#Output
print(f"There were {3 - count} even and {count} odd numbers.")
