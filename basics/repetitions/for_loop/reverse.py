# user phrase
phrase = input("What phrase do you see? ")

print("\nReversing...\n")
for i in range(len(phrase),0,-1):
  print(phrase[i-1], end="")

print("\nReversing...\n")
for i in range(len(phrase)):
  print(phrase[-i-1], end="")

# final message
print("\n\nDone!")