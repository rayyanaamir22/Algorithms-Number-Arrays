# INSERTION SORT

def insertionSort(array):
  
  # Linear loop
  for i in range(len(array)):
    # Store current element for comparison with adjacent one
    temp = array[i]
    j = i - 1
    
    # Quadratic loop
    # WHILE adjacent element is greater than temp
    while j >= 0 and temp < array[j]:
      # Move adjacent element forward
      array[j+1] = array[j]
      j -= 1

    # Move current element ahead
    array[j+1] = temp