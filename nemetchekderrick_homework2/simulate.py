import math
import random
import sys
import matplotlib.pyplot as plt


def scoreFunction(L1, L2):
    if (L1 == L2):
        return 4
    if (((L1 == 'A' or L2 == 'A') and (L1 =='G' or L2 == 'G')) or ((L1 == 'T' or L2 == 'T') and (L1 =='C' or L2 == 'C')) ):
         return -1
    else: 
        return -5
# Takes array of 2 sequences, returns score and length in an array
def findScore(sequences):
        
    firstSequence =  '*' + sequences[0]
    secondSequence = '*' + sequences[1]
    row, col = (len(firstSequence)), (len(secondSequence))

    matrix = [[0 for x in range(col)] for y in range(row)] 


    ## setup the initial negative values on the bound areas
    for i in range(len(firstSequence)):
        for j in range(len(secondSequence)):
            if (i == 0 or j == 0):
                matrix[i][j] = 0
    highestScore = 0
    pos = [0, 0]
    for i in range(len(firstSequence)):
        for j in range(len(secondSequence)):
            if (i != 0 and j != 0): # Make sure its not a bound area
                score = scoreFunction(firstSequence[i], secondSequence[j])
                topleft = max(matrix[i-1][j-1] + score, 0)
                top = max(matrix[i-1][j] - 5, 0)
                left = max(matrix[i][j-1] - 5, 0)
                localHighestScore = max(topleft, top, left)
                matrix[i][j] = localHighestScore
                if ((i != (len(firstSequence) - 1)) and localHighestScore > highestScore):
                    highestScore = localHighestScore
                    pos = [i, j]
                    
    # Backtrack from highest score position to find the length
    lengthFound = False
    lengthCounter = 0
    iPos = pos[0]
    jPos = pos[1]
    while ((lengthFound == False) and (jPos > 0) and (iPos > 0) ):
        score = scoreFunction(firstSequence[i], secondSequence[j])
        topleft = (matrix[iPos-1][jPos-1] - score)
        top = (matrix[i-1][j] + 5)
        left = (matrix[i][j-1] + 5)
        boxBefore = min(topleft, top, left)
        lengthCounter += 1
        if (boxBefore == topleft):
            iPos -= 1
            jPos -= 1
        elif (boxBefore ==  top):
            iPos -= 1
        elif (boxBefore == left):
            jPos -= 1
        if (boxBefore == 0):
            lengthFound = True


    # print(highestScore)
    # print (pos)
    # print(counter)
    # print("The score is", highestScore)
    # print("The length is", lengthCounter - 1 )

    del matrix[len(firstSequence) - 1]

    #print('The score is', highestScore)
    #for i in range(len(firstSequence ) - 1):
    #   print(matrix[i])
    return([highestScore, lengthCounter - 1])

def generateSequences():
    letters = ["A", "G", "C", "T"]
    sequence1 = ''
    sequence2 = ''
    for i in range(100):
        sequence1 += random.choice(letters)
        sequence2 += random.choice(letters)
    return([sequence1, sequence2])

if __name__ == "__main__":
    # generateSequences()
    # NOTE: DO NOT uncomment sourcefile lines unless you need to write them to the file
    #sourceFile = open('scores.txt', 'w')
    print("Data that would be printed to file, second value (Sequence length) is not needed for this assignment")
    for i in range(10):
        sequences = generateSequences()
        print( findScore(sequences)) #file = sourceFile)
    #sourceFile.close()

        