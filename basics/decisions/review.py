energy_level = int(input("Beep what is your energy level: "))
sunny = True
solar_charging = True

if (energy_level == 5):
  print("You are OK")
elif (energy_level >= 3):
  if (sunny and solar_charging):
    print("You can go to the field for charging")
  else:
    print("You are OK for now, but you can plugin your charging cable fo a while")
else:
  print("You must plugin your chargibg cable")