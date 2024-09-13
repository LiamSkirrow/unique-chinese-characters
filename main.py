# reading in an input file, generate an output file containing only unique characters

chSet = set()
numUniqueChars = 0
totalNumChars  = 0

with open('hsk1-word-vocab.txt') as file:
    while(True):
        ch = file.read(1)
        # we've reached the end
        if not ch:
            print('Reached end of file')
            break
        if ch != '\n' and ch != ' ':
            # print('Found character: ' + ch)
            chSet.add(ch)
        totalNumChars += 1

# create an output file
outputFile = open('hsk1-word-vocab-OUTPUT.txt', 'w')

# print out the elements in the set
for item in chSet:
    print('Found unique character: ' + item)
    numUniqueChars += 1
    outputFile.write(item + '\n')

outputFile.close()
print('Found ' + str(numUniqueChars) + ' unique characters out of ' + str(totalNumChars) + ' total')
