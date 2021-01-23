#Input and read file
inputFile = input("Masukkan file: ")
inputFile = open(inputFile, "r")
operand = []
read = inputFile.readline()
while(read[0] != "-"):
    operand.append(read)
    read = inputFile.readline()
result = inputFile.readline()

#Delete new line and + from operand and result
for i in range(len(operand)-1):
    operand[i] = operand[i][:len(operand[i])-1]
operand[len(operand)-1] = operand[len(operand)-1][:len(operand[len(operand)-2])]

#The letters that used in the expression
letterUsed = []
countTest = 0