# For organization

# Modules
import random

def randomArrayBetween(min, max, size):
  # Create a random array between the min and max (included)
  
  # Final length must be greater than 1
  if size <= 1:
    raise ValueError

  randomArray = []  
  # Make random values
  while len(randomArray) < size:
    randomArray.append(random.randint(min, max))
  
  return randomArray

def reuse(thisCode):
  while True:
    print(f'\nDo you want to reuse {thisCode}?')
    re = input()
    if re.lower().startswith('y'):
      return True
    elif re.lower().startswith('n'):
      return False
    else:
      print('Invalid input')
