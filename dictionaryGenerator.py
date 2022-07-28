

dictFile = open("AFINN-111.txt","r")
newDictFile = open("dictionary.txt","w")


line = dictFile.readline()
while line != '':
    temp = line.split()
    print(temp[0])
    newDictFile.write(temp[0] + "\n")
    line = dictFile.readline()

