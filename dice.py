import random
import matplotlib.pyplot as plt

### Changeable Variables ###

tot_dice = 10
sides = 6
rerolls = 5
iterations = 1000000

### Code Begins ###

average = sum(range(1, sides + 1)) / sides

'''
Singular iteration. Rolls an arbitrary number of arbitrary sided dice and returns the sum after rerolling a specified number of times.
Rerolling is determined by only rerolling a number if the number is lower than the average of the sides of one die, and constraining
the rerolls to a hard-coded number of times.
'''
def roll():
  rolls = random.choices(range(1, sides + 1), k = tot_dice)
  rolls.sort()

  remaining = rerolls
  for i in range(len(rolls)):
    roll = rolls[i]
    if (roll < average and remaining > 0):
      rolls[i] = random.choice(range(1, sides + 1))
      remaining -= 1
    else:
      break

  return sum(rolls)

'''
Performs the rolling functionality a specified number of times and returns the results in a dictionary.
'''
def generate(n: int):
  results = {}
  for _ in range(n):
    result = roll()
    if (result in results.keys()):
      results[result] += 1
    else:
      results[result] = 1
  
  return results

'''
Plots the results in a bar graph and prints additional data.
'''
def display_results(raw_data: dict):
  data = sort_dict(raw_data)
  keys = list(data.keys())
  values = list(data.values())

  print(f"Average Sum: { sum(keys) / len(keys) }")

  plt.bar(range(len(data)), values)
  plt.xticks(range(len(data)), keys, rotation='vertical')
  plt.title(f"Results After { iterations } Iterations")
  plt.xlabel("Totals")
  plt.ylabel("Number of times rolled")
  # comment one of these out depending on if you just want to display or want to save it
  plt.show()
  # plt.savefig("sums.png")

'''
Sorts a dictionary based on keys.
'''
def sort_dict(dict: dict):
  keys = list(dict.keys())
  keys.sort()
  return { key: dict[key] for key in keys}

### Run the Code ###

results = generate(iterations)
display_results(results)