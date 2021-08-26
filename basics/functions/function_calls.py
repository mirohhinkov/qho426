def art_box(word):
  top_left = "⌈"
  top_right = "⌉"
  bottom_left = "⌊"
  bottom_right = "⌋"
  top = "⎺"
  bottom = "⎯"
  middle_left = "⎢"
  middle_right = "⎟"
  length = len(word) + 6
  print()
  print(f"{top_left}{length * top}{top_right}")
  # print(f"{middle_left}{length * ' '}{middle_right}")
  print(f"{middle_left}{3 * ' '}{word}{3 * ' '}{middle_right}")
  # print(f"{middle_left}{length * ' '}{middle_right}")
  print(f"{bottom_left}{length * bottom}{bottom_right}")


def run():
  word = input("Please enter a word - ")
  option = input("""
  1) Display in a Box 
  2) Display Lower-case 
  3) Display Upper-case 
  4) Display Mirrored 
  5) Repeat
  ? """)
  if option == "1":
    art_box(word)
  elif option == "2":
    art_box(word.lower())
  elif option == "3":
    art_box(word.upper())
  elif option == "4":
    art_box(word[::-1])
  elif option == "5":
    # s = ""
    repeat = int(input("How many times do you want to repeat? "))
    # for i in range(repeat):
    #   s += word.lower() if i % 2 else word.upper()
    #   s += " "
    # s.strip()
    # art_box(s)
    s = [word] * repeat;
    s = [s[i].lower() if i%2 else s[i].upper() for i in range(repeat)]
    art_box(" ".join(s))
  else:
    print("Unknown command")


if __name__ == "__main__":
  run()