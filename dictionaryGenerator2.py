import csv


totalDict = {}



def freqAnalysis(totalDict):
    i = 0
    with open("training.1600000.processed.noemoticon.csv","r") as csvfile:
        csvReader = csv.reader(csvfile)
        for line in csvReader:
            #print(row[1]) # text element of the dataset
            strArray = line[1].split()
            for word in strArray:
                if word in totalDict:
                    totalDict[word] = totalDict[word] + 1
                else:
                    totalDict[word] = 1


freqAnalysis(totalDict)
new_list = sorted(totalDict.items(), key=lambda x:x[1], reverse=True)
fin_list = []
for i in range(20000):
    fin_list.append(new_list[i])
sort_values = dict(fin_list)
dictVec = open("dictionary2.txt","w")
for i in range(len(fin_list)):
    dictVec.write(fin_list[i][0] + "\n")
