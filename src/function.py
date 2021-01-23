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
    return (int(firstOperandAnswer) + int(secondOperandAnswer) == int(resultAnswer))