sequences = []

# add strings from fasta file that don't contain 'seq'
with open('scoregiven_example.fa') as file:
    lines = file.readlines()
    for line in lines:
        if (line.find('seq') != 1):
            sequences.append(line)    

# +1 for match
# -1 for: mismatches or a gap

score = 0
matches = 0
mismatches = 0
gaps = 0

test = enumerate(sequences[0])

for i, j in zip(sequences[0], sequences[1]):
    if (i == j):
        matches += 1
    else:
        if (i == '-' or j == '-' ):
            gaps += 1
        else:
            mismatches += 1
score = matches - mismatches - gaps
print('The score is', score, '(', matches, 'matches,', mismatches, 'mismatches', gaps, 'gaps')
