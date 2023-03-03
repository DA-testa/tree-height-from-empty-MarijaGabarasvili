# python3

import sys
import threading
import numpy


def compute_height(n, parents, shit):
    max_height = 0
    if(parents == -1):
        max_height = 1
    else:
        parent2 = shit[parents]
        max_height = 1 + compute_height(parents, parent2, shit)
    return max_height
    # Write this function
    # Your code here
    


def main():
    # implement input form keyboard and from files
    shit = []
    wait = input()
    littleshit = False
    if("I" in wait) :
        number = int(input())
        shit = [int(j) for j in input.split()]
        littleshit = True

    if("F" in wait):
        name = "test/" + input() + ".txt"
        if not("a" in name):
            littleshit = True
            with open(name) as file:
                number = int(next(file))
                for line in file:
                        shit=[int(j) for j in next(file).split()]
    if littleshit:
        for j in range(0, number, 1):
            max = compute_height(1, shit[j], shit)
            min=0
            if(min<max):
                min = max
        print(min)
            

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
main()
# print(numpy.array([1,2,3]))