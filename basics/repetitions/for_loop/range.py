# asking for distance
brigh = int(input("What level of brightness is required? "))
print()
# adjust britness
for i in range(2, brigh + 1, 2):
  print(f"Beep's brightness level: {i * '*'}")
  print(f"Bop's brightness level:  {i * '*'}")

# final message
print("\nAdjustments complete!")