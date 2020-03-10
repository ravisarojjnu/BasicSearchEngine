from TDMCreator import TermDocumentMatrix
from preprocessing import processText
from documentSimilarity import calculateScore
from utility import readCranDocument
import timeit
import pickle
import os

def indexDocument(processedCorpus,savepath):
    t3=timeit.default_timer()
    #computing TDM
    tdm=TermDocumentMatrix()
    tdm.createFeatureAndTransform(processedCorpus)
    t4=timeit.default_timer()
    print("TDM Generation time: ",t4-t3)
    print("Corpus size: ",tdm.corpusSize)
    print("vocab size: ",len(tdm.vocab))

    #saving TDM
    with open(os.path.join(savepath,"tdm.pickle"),mode="wb") as file:
        pickle.dump(tdm,file)
    

def indexDocumentDriver(filename,filepath,savepath):
    #reading documents
    t1=timeit.default_timer()
    corpus,corpusIndextoDocNoMapping=readCranDocument(filename,filepath)
    t2=timeit.default_timer()
    print("corpus reading time: ",t2-t1)

    #Preprocessing
    processedCorpus=[]
    search=corpus[3]
    for docNo in corpusIndextoDocNoMapping:
        prcessedDoc=processText(corpus[docNo])
        processedCorpus.append(prcessedDoc)
    t3=timeit.default_timer()
    print("corpus preprocessing time: ",t3-t2)

    #saving documents
    with open(os.path.join(savepath,"corpus.pickle"),mode="wb") as file:
        pickle.dump(corpus,file)

    #saving corpus index to doc map
    with open(os.path.join(savepath,"corpusIndextoDocNoMapping.pickle"),mode="wb") as file:
        pickle.dump(corpusIndextoDocNoMapping,file)

    indexDocument(processedCorpus,savepath)

if __name__=="__main__":
    baseDir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    modelPath=os.path.join(baseDir,"indexModel")
    corpusPath=os.path.join(baseDir,"cran")
    corpusFilename="cran.all.1400"
    indexDocumentDriver(corpusFilename,corpusPath,modelPath)

