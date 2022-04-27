#Input and read file
inputFile = input("Input file: ")
inputFile = open(inputFile, "r")
operand = []

#Print input problem
print(50*"=")
print(21*" ","PROBLEM")
read = inputFile.readline()
print(read,end="")
while read[0] != "-":
    operand.append(read)
    read = inputFile.readline()
    print(read,end="")
result = inputFile.readline()
print(result)
print(50*"=")

#Delete new line and + from operand and result
for i in range(len(operand)-1):
    operand[i] = operand[i][:len(operand[i])-1]
operand[len(operand)-1] = operand[len(operand)-1][:len(operand[len(operand)-2])]

#Initial variable
letterUsed = [] #For storing all the letter used
countTest = [0] #For counting total combination checked
found = [False] #For determining weather there is solution
