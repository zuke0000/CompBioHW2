import math
sequences = []

# add strings from fasta file that don't contain 'seq'
with open('dotplot-example.fa') as file:
    lines = file.readlines()
    for line in lines:
        if (line.find('seq') != 1):
            sequences.append(line)    

#PARAMTERS
gapPenalty = 1
mismatchPenality = 1
matchPenality = 1

firstSequence = sequences[0]
secondSequence = + sequences[1]
row, col = (len(firstSequence)), (len(secondSequence))

matrix = [[0 for x in range(col)] for y in range(row)] 


for i in range(len(firstSequence)):
    for j in range(len(secondSequence)):
        matrix[i][j] = max(topleft, top, left)

#for i in range(len(firstSequence ) - 1):
#    print(matrix[i])