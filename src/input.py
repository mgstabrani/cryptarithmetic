#Input and read file
inputFile = input("Input file: ")
inputFile = open(inputFile, "r")
operand = []
print(50*"=")
print(21*" ","PROBLEM")
read = inputFile.readline()
print(read,end="")
while(read[0] != "-"):
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

#The letters that used in the expression
letterUsed = []
countTest = [0]
found = [False]