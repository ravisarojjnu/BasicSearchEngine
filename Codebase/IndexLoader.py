import os 
import pickle
from preprocessing import processText

class Resource:
    tdm=None
    corpus=None
    corpusIndextoDocNoMapping=None

def loadIndex(modelPath):
    #loading TDM
    with open(os.path.join(modelPath,"tdm.pickle"),mode="rb") as file:
        Resource.tdm=pickle.load(file)
    

def loadCorpus(docPath):
    #loading documents
    with open(os.path.join(docPath,"corpus.pickle"),mode="rb") as file:
        Resource.corpus=pickle.load(file)

    #loading corpus index to doc map
    with open(os.path.join(docPath,"corpusIndextoDocNoMapping.pickle"),mode="rb") as file:
        Resource.corpusIndextoDocNoMapping=pickle.load(file)

def loadResourceDriver():
    baseDir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    modelPath=os.path.join(baseDir,"indexModel")
    loadCorpus(modelPath)
    loadIndex(modelPath)