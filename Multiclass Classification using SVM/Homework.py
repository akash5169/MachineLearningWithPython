# IDS 575
# University of Illinois at Chicago
# Fall 2021
# quiz #06
#
# Do not rename/delete any functions or global variables provided in this template and write your solution
# in the specified sections. Use the main function to test your code when running it from a terminal.
# Avoid writing that code in the global scope; however, you should write additional functions/classes
# as needed in the global scope. These templates may also contain important information and/or examples
# in comments so please read them carefully. If you want to use external packages (not specified in
# the assignment) then you need prior approval from course staff.
# This part of the assignment will be graded automatically using Gradescope.
# =========================================================================================================


import numpy as np
from scipy.sparse import csr_matrix

#######################################################################
# you are allowed to add your code wherever inside this function
# must return X in type of <class 'scipy.sparse.csr.csr_matrix'> and y in type of <class 'numpy.ndarray'>
def readCsrData(filename):
  with open(filename) as datafile:
    
    for line in datafile:
      # Split your line into a list of words deliminated by the space.
      elements = line.split(' ')
      
      # Read the very first element and the remaining ones as strings.
      label, features = elements[0], elements[1:]
      
      

    return X,y

def main():
  # Load the data
  myX_train,myy_train=readCsrData('articles.train')
  myX_test, myy_test = readCsrData('articles.test')

  #load with existing function
  from sklearn.datasets import load_svmlight_file
  X_train, y_train = load_svmlight_file("articles.train")
  X_test, y_test = load_svmlight_file("articles.test")

  if np.array_equal(myX_train.todense(), X_train.todense()):
    print("Success!")



################ Do not make any changes below this line ################
if __name__ == '__main__':
	main()