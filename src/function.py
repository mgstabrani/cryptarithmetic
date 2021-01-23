from input import operand,result,letterUsed

def isSingleLetter(x):
    found = 0
    for letter in operand:
        if(x == letter):
            found += 1
    if(found > 1):
        return False
    else:
        return True

def initNumber():
    for i in range(len(letterUsed)):
        letterUsed[i] += "0"

def changeNumber(letter, number):
    letter = list(letter)
    letter[1] = str(number)
    return letter[0]+letter[1]

def putLetters():
    for element in operand+[result]:
        for letter in element:
            isUnique = True
            for j in range(len(letterUsed)):
                if(letter == letterUsed[j]):
                    isUnique = False
            if(isUnique and letter != " "):
                letterUsed.append(letter)

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

    sum = 0
    for number in operandAnswer:
        sum += int(number)
    return (sum == int(resultAnswer) and isValid)

def putNumbers(a):
    for i in range(len(letterUsed)):
        letterUsed[i] = changeNumber(letterUsed[i],a[i])
    if(checkAnswer(letterUsed)):
        for answer in letterUsed:
            print(answer[0], "=", answer[1])
 
def heapPermutation(n,A):
    c = [0 for i in range(n)]
    found = False
    countTest = 0
    i = 0
    while(i < n and not found):
        if(c[i] < i):
            if (i % 2 == 0):
                A[0],A[i] = A[i],A[0]
            else:
                A[c[i]],A[i] = A[i],A[c[i]]
            if(A[0] != 0):
                for k in range(len(letterUsed)):
                    letterUsed[k] = changeNumber(letterUsed[k],A[k])  
                countTest += 1                 
                if(checkAnswer(letterUsed)):
                    for answer in letterUsed:
                        print(answer[0], "=", answer[1])
                    found = True
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    if(not found):
        print("No solution")
    print("The total test =", countTest)

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
    print(len(result)*"-")    
    for letter in result:
        for number in letterUsed:
            if(letter == number[0]):
                print(number[1],end="")
    print()