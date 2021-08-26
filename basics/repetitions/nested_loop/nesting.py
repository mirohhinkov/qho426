# user inputs
def run():
  seq =input("Please enter a sequence: ")
  # print()
  marker = input("Please enter the character for the marker ")
  result = 0
  if seq.count(marker) > 1:
    first = 0
    for i in range(len(seq)):
      if seq[i] == marker:
        if not first:
          first = i + 1
        else:
          result = i - first
          break

  # final message
  print(f"The distance between the markers is {result}.")

  for i in range(len(seq)):
    if seq[i] == marker:
      for j in range(i+1, len(seq)):
        if seq[j] == marker:
          result = j - i - 1
          break
      break

  # final message
  print(f"The distance between the markers is {result}.")

if __name__ == "__main__":
  run()