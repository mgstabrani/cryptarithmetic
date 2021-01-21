#Input and read file
inputFile = input("Masukkan file: ")
inputFile = open(inputFile, "r")
firstOperand = inputFile.readline()
secondOperand = inputFile.readline()
line = inputFile.readline()
result = inputFile.readline()

#Delete new line and + from operand and result
firstOperand = firstOperand[:len(firstOperand)-1]
secondOperand = secondOperand[:len(secondOperand)-2]
result = result[:len(result)]