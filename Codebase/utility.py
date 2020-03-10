import re
import os

def readCranDocument(filename,filepath):
    corpus={}
    corpusIndextoDocNoMapping=[]
    with open(os.path.join(filepath,filename),mode="r") as file:
        text=file.read()
        textlist=re.split(r"(.I \d+)",text)[1:]
    for i in range(0,len(textlist),2):
        docNo=int(textlist[i].split()[1])
        corpus[docNo]=re.split(r".W\n",textlist[i+1])[1]
        corpusIndextoDocNoMapping.append(docNo)
    return corpus,corpusIndextoDocNoMapping

def readCranTestResultFile(filename,filepath):
    testcaseResult={}
    with open(os.path.join(filepath,filename),mode="r") as file:
        lines=file.readlines()
    for row in lines:
        introw=list(map(int,row.split()))
        if not testcaseResult.get(introw[0]):
            testcaseResult[introw[0]]=[]
        if introw[2]>0:
            testcaseResult[introw[0]].append(introw[1])
    return testcaseResult

# filepath="E:\InformationExtraction\cran"
# filename="cran.all.1400"

# textlist=readCranDocument(filename,filepath)
# print(textlist[1])

