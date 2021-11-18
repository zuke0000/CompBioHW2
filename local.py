import math
sequences = []

# add strings from fasta file that don't contain 'seq'
with open('videxample.fa') as file:
    lines = file.readlines()
    for line in lines:
        if (line.find('seq') != 1):
            sequences.append(line)    

#PARAMTERS
gapPenalty = 1
mismatchPenality = 1
matchPenality = 1

firstSequence =  '*' + sequences[0]
secondSequence = '*' + sequences[1]
row, col = (len(firstSequence)), (len(secondSequence))

matrix = [[0 for x in range(col)] for y in range(row)] 


## setup the initial negative values on the bound areas
for i in range(len(firstSequence)):
    for j in range(len(secondSequence)):
        if (i == 0 or j == 0):
            matrix[i][j] = 0

for i in range(len(firstSequence)):
    for j in range(len(secondSequence)):
        if (i != 0 and j != 0): # Make sure its not a bound area
            if (firstSequence[i] == secondSequence[j]):
                topleft = matrix[i-1][j-1] + matchPenality
            else: 
                topleft = matrix[i-1][j-1] - mismatchPenality
            top = matrix[i-1][j] - gapPenalty
            left = matrix[i][j-1] - gapPenalty
            matrix[i][j] = max(topleft, top, left)
del matrix[len(firstSequence) - 1]

print('The score is', matrix[len(firstSequence)-2][len(secondSequence)-1])
for i in range(len(firstSequence ) - 1):
    print(matrix[i])