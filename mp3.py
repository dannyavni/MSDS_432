#import required packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
import random

# recursuve facorial implemntation adapted retrieved from:
# https://github.com/egonSchiele/grokking_algorithms/blob/master/02_selection_sort/python/01_selection_sort.py

def recursive_fact(x):
  if x == 1:
    return 1
  else:
    return x * recusive_fact(x-1)
	
# iterative factorial solution u

def iterative_fact(x):
  fact = 1
  for i in range(1,x+1):
    fact = fact * i
  return fact

#utility function to generate and array of uniformly distributed data array with persistent seed across calls 
def generate_random_array(item_count, low, high):
    np.random.seed(666)
    
    return np.random.randint(low, high, item_count).tolist()

#prepare an array of all the desired data lengths
random_ints = np.sort(generate_random_array(10, 100, 500)).tolist()

#prepare an empty data frame with the desired column names
test_data_col_names = ['number', 'factorial', 'iterative_ms', 'recursive_ms']
test_data = pd.DataFrame(columns = test_data_col_names) 

#iterate over the possible lens, create test data for each length, and compture runtime length in milliseconds
for random_int in random_ints:
    start   = time.time()
    fact1   = iterative_fact(random_int)
    iterative_ms = (time.time() - start) * 1000

    start   = time.time()
    fact2    = recursive_fact(random_int)
    recursive_ms = (time.time() - start) * 1000
    
    if fact1 != fact2:
        raise Exception('This should never have happened. The two methods should concur!')
    
    #insert the results into a new dataframe record 
    #need to cast the factorial into a string to prevent a pandas float or int overflow
    test_data.loc[len(test_data)] = [random_int, str(fact1), iterative_ms, recursive_ms]
	
#plain text data dump of the test results
test_data
