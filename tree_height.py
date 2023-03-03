# python3

import sys
import threading
import numpy

washere = []
size = []

def compute_height(n, parents, shit):
  if(washere[n]==1):
    return size[n]
  else:
    washere[n]=1
    if(parents!=-1):
      max_height = 1+compute_height(parents, shit[parents],shit)
      size[n] = max_height
    else:
      max_height = 1
      size[n] = 1
    return max_height
    

          
    
    # Write this function
    # Your code here
    


def main():
    wait = input()
    littleshit = False
    if("I" in wait) :
        number = int(input())
        shit = [int(j) for j in input().split()]
        littleshit = True

    if("F" in wait):
        name = "test/" + input()
        if not("a" in name):
            littleshit = True
            with open(name) as file:
                number = int(next(file))
                for line in file:
                    shit=[int(j) for j in line.split()]
    if littleshit:
        for j in range(0, number, 1):
            washere.append(0)
            size.append(0)
        min=0
        for j in range(0, number, 1):
          max = compute_height(1, shit[j], shit)
          if(min<max):
            min=max

    print(max)

    # implement input form keyboard and from files
    
            

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    # pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# main()
# print(numpy.array([1,2,3]))