def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return min(likelihoods), max(likelihoods)

def run():
  print(f"Minimum likelihood of falling: {likelihood()[0]}%")
  print(f"Maximum likelihood of falling: {likelihood()[1]}%")

if __name__ == "__main__":
  run()