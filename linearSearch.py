# LINEAR SEARCH ALGORITHMS 
# O(n) time complexity

# Iterative
def iterativeLinearSearch(array, target): # Works
  for i in range(0, len(array)):
    # If target is found
    if array[i] == target:
      print("Target is present at index", i) # Return index
      break
    elif array[i] != array[-1]: # If still being looped
      continue # Keep going
    else: 
      print('Target is absent')


# Recursive
def recursiveLinearSearch(array, f, l, target): # Works
  # f and l denote first and last index of the array
  if l < f:
    print("Target is absent")
  elif array[f] == target:
    print("Target is present at index ", f)
  elif array[l] == target:
    print("Target is present at index ", l)
  else:
    return recursiveLinearSearch(array, f+1, l-1, target)
  
  
