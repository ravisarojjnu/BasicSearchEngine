from utility import readCranDocument,readCranTestResultFile
from query import query,Resource
import pandas as pd 
import os

#read Test queries
def readTestCases(filename,filepath):
    df=pd.read_csv(os.path.join(filepath,filename))
    return df

def compare(topNDocs,resultDocNums):
    count=0
    for docidx,score in topNDocs:
        if Resource.corpusIndextoDocNoMapping[docidx] in resultDocNums:
            count=count+1
    return count

def runTestCases( filename,filepath):
    filename,filepath
    df=readTestCases(filename,filepath)
    matched=0
    missed=0
    for i,row in df.iterrows():
        similarDocs=list(map(int,row["result"].split("|")))
        topN=len(similarDocs)+10
        topNDocs=query(row["text"],topN=topN)
        match=compare(topNDocs,similarDocs,)
        matched=matched+match
        missed=missed+topN-match
    return matched,missed



filename="testcase.csv"
filepath="E:\InformationExtraction\TestCase"
print(runTestCases(filename,filepath))

