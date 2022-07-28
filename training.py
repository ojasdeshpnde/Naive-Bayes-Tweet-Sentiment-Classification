import numpy
import csv

class repVec:
    def __init__(self):
        self.d = {}
        df = open("dictionary2.txt","r")
        rl = df.readline()
        while(rl != ''):
            self.d[rl.split()[0]] = 0
            rl = df.readline()
        self.v = None
        self.prior ={0:0.23706055, 4:0.76293945}

    def getBOW(self, str):
        text = str.split()
        for s in text:
            if s in self.d and self.d[s] == 0:
                self.d[s] = 1
        self.updateVec()

    def updateVec(self):
        self.v = numpy.array(list(self.d.values()))





# temp = repVec()
#
# temp.getBOW("")
# print(temp.v)


posTotalMap = repVec()
posTotalMap.getBOW("")
negTotalMap = repVec()
negTotalMap.getBOW("")

posTotal = posTotalMap.v
negTotal = negTotalMap.v


reference = {}
referenceFile = open("dictionary2.txt","r")
rLine = referenceFile.readline()
counter = 0

while(rLine != ''):
    reference[rLine.strip()] = counter
    counter = counter + 1
    rLine = referenceFile.readline()
#print(reference)



negFile = open("negative.txt","r")
posFile = open("positive.txt","r")



counterN = 0
lineN = negFile.readline()
while(lineN != ''):
    temp = lineN.split()
    for word in temp:
        if word in reference:
            negTotal[reference[word]] = negTotal[reference[word]] + 1
    lineN = negFile.readline()
    counterN = counterN + 1

counterP = 0
lineP = posFile.readline()
while(lineP != ''):
    temp = lineP.split()
    for word in temp:
        if word in reference:
            posTotal[reference[word]] = posTotal[reference[word]] + 1
    lineP = posFile.readline()
    counterP = counterP + 1
posTotal = posTotal / counterP
negTotal = negTotal / counterN


print(posTotal)
print(negTotal)

numpy.savetxt('posData.out',posTotal)
numpy.savetxt('negData.out',negTotal)

# There are 800,000 cases of "0"
# There are 248,576 cases of "4"

# For training 700,000 will be 0s and 200,000 will be "4"
