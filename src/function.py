#Import variables from input.py
from input import operand,result,letterUsed,countTest,found

#Put all letter used in file to letterUsed array
def putLetters():
    for element in operand+[result]:
        for letter in element:
            isUnique = True
            for j in range(len(letterUsed)):
                if(letter == letterUsed[j]):
                    isUnique = False
            if(isUnique and letter != " "):
                letterUsed.append(letter)

#Add each element at letterUsed array with 0
def initNumber():
    for i in range(len(letterUsed)):
        letterUsed[i] += "0"

#Change a number in letterUsed element with particular number
def changeNumber(letter, number):
    letter = list(letter)
    letter[1] = str(number)
    return letter[0]+letter[1]

#Check the solution by seeing letterUsed array
def checkAnswer(letterUsed):
    operandAnswer = ["" for i in range(len(operand))]
    resultAnswer = ""
    for i in range(len(operand)):
        for j in range(len(operand[i])):
            for usedLetter in letterUsed:
                if(operand[i][j] == usedLetter[0]):
                    operandAnswer[i] += usedLetter[1]
    for i in range(len(result)):
        for usedLetter in letterUsed:
            if(result[i] == usedLetter[0]):
                resultAnswer += usedLetter[1]
    isValid = True
    for answer in operandAnswer:
        if(answer[0] == "0"):
            isValid = False
    if(resultAnswer[0] == "0"):
        isValid = False
    if(not isValid):
        countTest[0] -= 1
    sum = 0
    for number in operandAnswer:
        sum += int(number)
    return (sum == int(resultAnswer) and isValid)

#Using heap permutation to generate permutation of possibility
def heapPermutation(n,A):
    c = [0 for i in range(n)]
    i = 0
    while(i < n and not found[0]):
        if(c[i] < i):
            if (i % 2 == 0):
                A[0],A[i] = A[i],A[0]
            else:
                A[c[i]],A[i] = A[i],A[c[i]]
            if(A[0] != 0):
                for k in range(len(letterUsed)):
                    letterUsed[k] = changeNumber(letterUsed[k],A[k])  
                countTest[0] += 1                 
                if(checkAnswer(letterUsed)):
                    found[0] = True
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1

#Display the solution
def displaySolution():
    for operands in operand[:len(operand)-1]:
        for letter in operands:
            for number in letterUsed:
                if(number[0] == letter):
                    print(number[1], end="")
            if(letter == " "):
                print(" ",end="")
        print()
    for letter in operand[len(operand)-1]:
        for number in letterUsed:
            if(number[0] == letter):
                print(number[1], end="")
        if(letter == " "):
            print(" ", end="")
    print("+")
    print((len(result)+1)*"-")    
    for letter in result:
        for number in letterUsed:
            if(letter == number[0]):
                print(number[1],end="")
    print()