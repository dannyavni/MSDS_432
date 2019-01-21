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

