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
        