import numpy

def bowVector(str,reference):
    retValue = numpy.zeros((20000,), dtype=int)
    text = str.split()
    for word in text:
        if word in reference and retValue[reference[word]] == 0:
            retValue[reference[word]] = 1
    return retValue



posData = numpy.loadtxt('posData.out') # loads trained data
negData = numpy.loadtxt('negData.out')


reference = {} # generates the reference dictionary
referenceFile = open("dictionary2.txt","r")
rLine = referenceFile.readline()
counter = 0

while(rLine != ''):
    reference[rLine.strip()] = counter
    counter = counter + 1
    rLine = referenceFile.readline()

negTestDataFile = open("negativeTest.txt","r")
posTestDataFile = open("positiveTest.txt","r")
lineN = negTestDataFile.readline()


prior = {"pos": 0.23706055, "neg": 0.76293945}


counterCorrect = 0
counterTotal = 0
while lineN != '':
    counterTotal += 1
    probMap = {"neg":0,"pos":0}
    vec = bowVector(lineN, reference)
    probMap["neg"] += numpy.log(prior["neg"])
    probMap["pos"] += numpy.log(prior["pos"])
    for i in range(len(vec)):
        if vec[i] == 1:
            probMap["neg"] += numpy.log(negData[i])
            probMap["pos"] += numpy.log(posData[i])
        else:
            probMap["neg"] += numpy.log(1-negData[i])
            probMap["pos"] += numpy.log(1-posData[i])
    if probMap["neg"] > probMap["pos"]:
        counterCorrect += 1
    lineN = negTestDataFile.readline()


lineP = posTestDataFile.readline()

while lineP != '':
    counterTotal += 1
    probMap = {"neg":0,"pos":0}
    vec = bowVector(lineP, reference)
    probMap["neg"] += numpy.log(prior["neg"])
    probMap["pos"] += numpy.log(prior["pos"])
    for i in range(len(vec)):
        if vec[i] == 1:
            probMap["neg"] += numpy.log(negData[i])
            probMap["pos"] += numpy.log(posData[i])
        else:
            probMap["neg"] += numpy.log(1-negData[i])
            probMap["pos"] += numpy.log(1-posData[i])
    if probMap["pos"] > probMap["neg"]:
        counterCorrect += 1
    lineP = negTestDataFile.readline()


print("Percentage Correct:")