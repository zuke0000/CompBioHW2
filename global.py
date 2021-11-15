import math
sequences = []

# add strings from fasta file that don't contain 'seq'
with open('dotplot-example2.fa') as file:
    lines = file.readlines()
    for line in lines:
        if (line.find('seq') != 1):
            sequences.append(line)    

# +1 for match
# -1 for: mismatches or a gap



# both strings start with 0
#
# boxes (most of the time) point to the one to the top left of it
# Number of empty spaces is the longest sequence - shortest
# review i-1 length stuff

firstSequence = sequences[0]
secondSequence = "0" + sequences[1]
row, col = (len(firstSequence)), (len(secondSequence))


matrix = [[0 for x in range(col)] for y in range(row)] 
print (firstSequence)
gapPenalty = 6
#longestLength = max(len(sequences[0]), len(sequences[1]))
#print('longest length is', longestLength)

## setup the initial negative values on the bound areas
for i in range(len(firstSequence)):
    for j in range(len(secondSequence)):
        if (i == 0 or j == 0):
            matrix[i][j] = 0 + (-6 * max(j,i))

for i in range(len(firstSequence)):
    for j in range(len(secondSequence)):
        if (i != 0 and j != 0): # Make sure its not a bound area
            doesMatch = (firstSequence[i] == secondSequence[j])
            print('does match?', doesMatch)
            topLeft = matrix[i-1][j-1] # get value of top left box relative to this one
            topLeft = topLeft + 5 if (doesMatch == True) else topLeft -2 
            top = matrix[i-1][j] - 6
            left = matrix[i][j-1] - 6
            matrix[i][j] = max(topLeft, top, left)
                

for i in range(len(firstSequence)):
    print(matrix[i])
#print(matrix)
#for i, j in zip(sequences[0], sequences[1]):
#    for iterator in i:
#        print(i)
    # if (i == j):
    #     matches += 1
    # else:
    #     if (i == '-' or j == '-' ):
    #         gaps += 1
    #     else:
    #         mismatches += 1
#score = matches - mismatches - gaps
# print('The score is', score)
# print('matches are', matches)

# need to lookup dynamic programming matrix are this point