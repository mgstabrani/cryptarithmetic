from function import *
import timeit
start = timeit.default_timer()
putLetters()
initNumber()
heapPermutation(10,list(range(10)))
stop = timeit.default_timer()
timeExecution = stop - start
print(21*" ","SOLUTION")
if(not found[0]):
    print("No solution")
else:
    displaySolution()
print(50*"=")
print(18*" ","TIME EXECUTION")
print("Time Execution =", timeExecution, "second")
print(50*"=")
print(20*" ","TOTAL TEST")
print("The total test =", countTest[0])