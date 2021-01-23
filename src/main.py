from function import *
import timeit
start = timeit.default_timer()
putLetters()
initNumber()
heapPermutation(10,list(range(10)))
stop = timeit.default_timer()
timeExecution = stop - start
displaySolution()
print("Time Execution =", timeExecution, "second")