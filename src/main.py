#Import all function
from function import *

#Import time library to count time execution
import timeit
start = timeit.default_timer()

#ALGORITMA
putLetters()    #Put all letters used in letterUsed array
initNumber()    #Initialize all element in letterUsed with 0
heapPermutation(10,list(range(10))) #Generate the combination and check the answer

#Counting time execution
stop = timeit.default_timer()
timeExecution = stop - start

#Display the solution
print(21*" ","SOLUTION")
if(not found[0]):
    print("No solution")
else:
    displaySolution()

#Show the time execution
print(50*"=")
print(18*" ","TIME EXECUTION")
print("Time Execution =", timeExecution, "second")

#Show total test
print(50*"=")
print(20*" ","TOTAL TEST")
print("The total test =", countTest[0])