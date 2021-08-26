def generate_sts():
  name = input("What is the name?\n")
  grade = int(input("What is the grade?\n"))
  dog = input("Does this student have a doggo? (Type YES or NO\n")
  if dog.upper() == "YES":
    dog = True
  else:
    dog = False
  return name,grade,dog

def all_sts():
  database = []
  while True:
    database.append(generate_sts())
    x = input("To stop, type 0. Otherwise type anything\n")
    if x == '0':
      break
  return database

def remove(lista = []):
  to_remove = input("Type the name of student to be removed:\n")
  for tuplex in lista:
    if tuplex[0] == to_remove:
      lista.remove(tuplex) 
  return lista

def print_sts(lista = []):
  for tuplex in lista:
    print (tuplex [0], "earned", tuplex[1], "grade this semester!")

def keep_sts(lista = [], mark = 100):
  for tuplex in lista:
    if tuplex[1] < mark:
      lista.remove(tuplex)
  return lista

def average(lista = []):
  suma=0
  for tuplex in lista:
    suma = suma + tuplex[1]
  return suma/len(lista)

def run():
  dtbs = all_sts()
  while True:
    print("Choose one of the following options:\n1-Retrieve all students\n2-Calculate the average\n3-Remove a student\n4-Remove all students below a grade\n5-Exit")
    opt = int(input())
    if opt == 1:
      print_sts(dtbs)
    elif opt == 2:
      print(f" The average mark of all students is {average(dtbs):.2f}")
    elif opt == 3:
      remove(dtbs)
    elif opt == 4:
      dtbs = keep_sts(dtbs, int(input("What is the benchmark (0-100):")))
      print(dtbs)
    elif opt == 5:
      print("Goodbye - I will miss you!")
      break
    else:
      print("Visit Specsavers mate, no such option exists")

run()