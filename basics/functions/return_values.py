# function definition
def sum_weights(w_beep, w_bop):
  return w_beep + w_bop
def calc_avg_weight(w_beep, w_bop):
  return (w_beep + w_bop) / 2

def func_factory(f):
  return lambda x, y: x + y if f == "sum" else (x + y) / 2

#execution point  
def run1():
  w_beep = float(input("What is the weight of Beep? "))
  print()
  w_bop = float(input("What is the weight of Boop? "))
  action = input("What would you like to calculate (sum or average)? ")

  if action == "sum":
    print(f"The sum of Beep and Bop's weight is {sum_weights(w_beep, w_bop)}.")
  elif action == "average":
    print(f"The average weight of Beep and Bop's weight is {calc_avg_weight(w_beep, w_bop)}.")
  else:
    print("Unknown command!")

def run():
  w_beep = float(input("What is the weight of Beep? "))
  print()
  w_bop = float(input("What is the weight of Boop? "))
  action = input("What would you like to calculate (sum or average)? ")

  if action == "sum":
    print(f"The sum of Beep and Bop's weight is {func_factory(action)(w_beep, w_bop)}.")
  elif action == "average":
    print(f"The average weight of Beep and Bop's weight is {func_factory(action)(w_beep, w_bop)}.")
  else:
    print("Unknown command!")


#function call

if __name__ == "__main__":
  run()