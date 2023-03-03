# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    return max_height


def main():
    # implement input form keyboard and from files
    lshit = []
    wait = input()
    littleshit = False
    if("I" in wait) :
        number = input()
        shit = [int(j) for j in input.split()]
        littleshit = True

    if("F" in wait):
        name = "test/" + input() + ".txt"
        if not("a" in name):
            littleshit = True
            number = input()
            len = [int(j) for j in input.split()]
            with open(name) as file:
                number = int(next(file))
                for line in file:
                    shit=[int(j) for j in next(file).split()]
    
    if littleshit:
        return
            

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))