
sequences = []

# add strings from fasta file that don't contain 'seq'
with open('dotplot-example.fa') as file:
    lines = file.readlines()
    for line in lines:
        if (line.find('seq') != 1):
            sequences.append(line)        
# print(sequences)

# first sequence x (i) +
# second sequence y (j) +
# match ('.') else (' ') +
# matching is not case sensitive +
letterLength = max(len(sequences[0]), len(sequences[1])) - 1
stringPrint = [" " for x in range(letterLength)]

print('  ',sequences[0])
for i, c in enumerate(sequences[1]): 
    for j, l in enumerate(sequences[0]):
        if (c.lower() == l.lower()):
            stringPrint[j] = '.'
    finalprint = ''.join(stringPrint)
    print (c, '', finalprint)
    stringPrint = [" " for x in range(letterLength)]
