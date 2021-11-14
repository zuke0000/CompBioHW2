sequences = []

# add strings from fasta file that don't contain 'seq'
with open('dotplot-example2.fa') as file:
    lines = file.readlines()
    for line in lines:
        if (line.find('seq') != 1):
            sequences.append(line)    

# +1 for match
# -1 for: mismatches or a gap

row, col = (len(sequences[0]) - 1), (len(sequences[1]) - 1)


matrix = [[0 for x in range(row)] for y in range(col)] 

icounter = 0
jcounter = 0

# both strings start with 0
#
# boxes (most of the time) point to the one to the top left of it
# Number of empty spaces is the longest sequence - shortest
# review i-1 length stuff


for i in sequences[0]:
    score = 0
    matches = 0
    mismatches = 0
    gaps = 0
    for j in sequences[1]:
        if (icounter < row and jcounter < col):
            matrix[icounter][jcounter] = 1
            jcounter += 1
            icounter += 1

print(matrix)
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