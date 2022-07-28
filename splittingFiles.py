import csv


counter = 0
counterP = 0
negativeFile = open("negative.txt","w")
negativeTestFile = open("negativeTest.txt","w")
positiveFile = open("positive.txt","w")
positiveTestFile = open("positiveTest.txt","w")
with open("training.1600000.processed.noemoticon.csv", "r") as csvfile:
    csvReader = csv.reader(csvfile)
    for line in csvReader:
        # print(row[1]) # text element of the dataset
        if counter < 799000:
            negativeFile.write(line[1] + "\n")
            counter = counter + 1
        elif counter >= 799000 and line[0] == '0':
            negativeTestFile.write(line[1] + "\n")
        elif counterP < 248076 and line[0] == '4':
            positiveFile.write(line[1] + "\n")
            counterP = counterP + 1
        else:
            positiveTestFile.write(line[1] + "\n")

