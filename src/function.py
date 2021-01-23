from input import operand,result,letterUsed,countTest

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
            for j in range(len(letterUsed)-1):
                if(letter == letterUsed[j]):
                    isUnique = False
            if(isUnique and letter != " "):
                letterUsed.append(letter)

def checkAnswer(letterUsed):
    operandAnswer = ["" for i in range(len(operand))]
    resultAnswer = ""
    for i in range(len(operandAnswer)):
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

def displayTest():
    print("The total test =", countTest)