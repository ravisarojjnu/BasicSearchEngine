from utility import readCranTestResultFile,readCranDocument
import pandas as pd
#read Test queries
def readTestCases(filename,filepath,resultFilepath):
    quries,indexToQueryNo=readCranDocument(filename,filepath)
    testcaseResult=readCranTestResultFile(resultFilepath,filepath)
    return quries,indexToQueryNo,testcaseResult

def prepare(filename,filepath,resultFilepath):
    dic={}
    dic["text"]=[]
    dic["result"]=[]
    dic["queryID"]=[]

    quries,indexToQueryNo,testcaseResult=readTestCases(filename,filepath,resultFilepath)
    for queryID,results in testcaseResult.items():
        if queryID in indexToQueryNo:
            dic["text"].append(quries[queryID])
            dic["queryID"].append(queryID)
            dic["result"].append("|".join([str(ele) for ele in results]))
    pd.DataFrame(dic).to_csv("testcase.csv",index=False)


filename="cran.qry"
filepath="E:\InformationExtraction\cran"
resultFilepath="cranqrel"

prepare(filename,filepath,resultFilepath)