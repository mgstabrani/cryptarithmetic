from input import firstOperand,secondOperand,result,letterUsed

def isSingleLetter(x):
    found = 0
    for letter in firstOperand,secondOperand,result:
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
    for letter in (firstOperand+secondOperand+result):
        isUnique = True
        for j in range(len(letterUsed)-1):
            if(letter == letterUsed[j]):
                isUnique = False
        if(isUnique and letter != " "):
            letterUsed.append(letter)

def checkAnswer(letterUsed):
    firstOperandAnswer = ""
    secondOperandAnswer = ""
    resultAnswer = ""
    for i in range(len(firstOperand)):
        for usedLetter in letterUsed:
            if(firstOperand[i] == usedLetter[0]):
                firstOperandAnswer += usedLetter[1]
            elif(firstOperand[i] == " "):
                firstOperandAnswer += " "
    for i in range(len(secondOperand)):
        for usedLetter in letterUsed:
            if(secondOperand[i] == usedLetter[0]):
                secondOperandAnswer += usedLetter[1]
    for i in range(len(result)):
        for usedLetter in letterUsed:
            if(result[i] == usedLetter[0]):
                resultAnswer += usedLetter[1]
    isValid = True
    if(firstOperandAnswer[0] == "0" or secondOperandAnswer[0] == "0" or resultAnswer[0] == "0"):
        isValid = False
    return (int(firstOperandAnswer) + int(secondOperandAnswer) == int(resultAnswer) and isValid)

def putNumbers(a, n):
    for i in range(len(letterUsed)):
        letterUsed[i] = changeNumber(letterUsed[i],a[i])
    if(checkAnswer(letterUsed)):
        for answer in letterUsed:
            print(answer[0], "=", answer[1])
 
def heapPermutation(a, size, n):
    if (size == 1):
        putNumbers(a, n)
        return
 
    for i in range(size):
        heapPermutation(a, size-1, n)
        if size & 1:
            a[0], a[size-1] = a[size-1], a[0]
        else:
            a[i], a[size-1] = a[size-1], a[i]