'''
Name: Rayyan Aamir
Date: May 10, 2022
Program: Sorting and Searching Algorithms 
'''

# Modules
import os
import timeit

# Other files
import functions as f
import insertionSort as i
import linearSearch as lin
import binarySearch as bin

def main(): # Main function
  while True: # Program loop
    # Title
    print('Algorithms Assignment\n')
    
    # Create array
    test = f.randomArrayBetween(0, 100, 20)
    print(f'Original array: {test}')
  
    #----------------SORTING ALGORITHMS-----------------
  
    # Insertion test
    startTime = timeit.default_timer()
    i.insertionSort(test)
    print('\nInsertion sorted array:', test)
    print('\nInsertion time:', timeit.default_timer() - startTime)
  
    # Builtin test
    startTime = timeit.default_timer()
    test.sort()
    #testObjects.sort(key=lambda x: x.x) # Builtin sort objects
    print('\nBuiltin time:', timeit.default_timer() - startTime)
    
    #----------------DEFINE SEARCHING ALGORITHM---------
    
    print('\n')
    # Choose search method
    searchAlgorithm = ''
    while searchAlgorithm not in ['LINEAR', 'BINARY']:
      print('Do you want to run LINEAR or BINARY search algorithm?')
      searchAlgorithm = input().upper()
  
      print('\n')
    # Choose search process
    algorithmType = ''
    while algorithmType not in ['ITERATIVE', 'RECURSIVE']:
      print('Do you want to use the ITERATIVE or RECURSIVE method?')
      algorithmType = input().upper()
  
    print('\n')
    # Choose target value for search
    algorithmTarget = test[0] - 1
    # While target is outside of test's scope
    while algorithmTarget < test[0] or algorithmTarget > test[-1]:
      print(f'Select a target within the scope of the test array: [{test[0]}, {test[-1]}]')
      try:
        algorithmTarget = int(input())
      except (TypeError, ValueError):
        print('Enter a number.')
  
    #----------------RUN SEARCH ALGORITHM---------------
  
    # recursiveLinearSearch() causes StackOverflowError with data larger than 1 000 units.
    # recursiveBinarySearch() does not suffer this as it cuts the dataset in half, so to have it crash the data must be 10^304 units long.
    
    print('\n')
    startTime = timeit.default_timer() # Timer starts here
    
    if searchAlgorithm == 'LINEAR' and algorithmType == 'ITERATIVE': 
      lin.iterativeLinearSearch(test, algorithmTarget)
      print('Algorithm time:', timeit.default_timer() - startTime)
    elif searchAlgorithm == 'LINEAR' and algorithmType == 'RECURSIVE': 
      lin.recursiveLinearSearch(test, 0, len(test)-1, algorithmTarget)
      print('Algorithm time:', timeit.default_timer() - startTime)
    elif searchAlgorithm == 'BINARY' and algorithmType == 'ITERATIVE': 
      bin.iterativeBinarySearch(test, 0, len(test)-1, algorithmTarget)
      print('Algorithm time:', timeit.default_timer() - startTime)
    elif searchAlgorithm == 'BINARY' and algorithmType == 'RECURSIVE': 
      bin.recursiveBinarySearch(test, 0, len(test)-1, algorithmTarget)
      print('Algorithm time:', timeit.default_timer() - startTime)
    
    if f.reuse('SEARCH'): # Reuse SEARCH
      os.system('clear')
      continue
    else:
      os.system('clear')
      break

if __name__ == '__main__':
  main()