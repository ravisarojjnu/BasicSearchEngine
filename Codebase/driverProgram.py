from TDMCreator import TermDocumentMatrix
from preprocessing import processText
from documentSimilarity import calculateScore,findTopN
from utility import readCranDocument
import timeit 

if __name__=="__main__":
    # corpus=["Text analysis is fun",
    # "I like doing text analysis",
    # "I like puppies, they are fun",
    # "I like like this blog post",]
    # processedCorpus=[]
    # search=corpus[3]
    # for doc in corpus:
    #     prcessedDoc=processText(doc)
    #     processedCorpus.append(prcessedDoc)
    # tdm=TermDocumentMatrix()
    # tdm.createFeatureAndTransform(processedCorpus)
    # queryVector=tdm.transform(processText(search))
    # print(calculateScore(tdm.TDM,queryVector))

    filepath="E:\InformationExtraction\cran"
    filename="cran.all.1400"
    t1=timeit.default_timer()
    corpus,corpusIndextoDocNoMapping=readCranDocument(filename,filepath)
    t2=timeit.default_timer()
    print("corpus reading time: ",t2-t1)

    processedCorpus=[]
    search=corpus[3]
    for docNo in corpusIndextoDocNoMapping:
        prcessedDoc=processText(corpus[docNo])
        processedCorpus.append(prcessedDoc)
    t3=timeit.default_timer()
    print("corpus preprocessing time: ",t3-t2)

    tdm=TermDocumentMatrix()
    tdm.createFeatureAndTransform(processedCorpus)
    t4=timeit.default_timer()
    print("TDM Generation time: ",t4-t3)
    print("vocab size: ",len(tdm.vocab))

    #calculate score
    search="what are the structural and aeroelastic problems associated with flight of high speed aircraft ."
    queryVector=tdm.transform(processText(search))
    score=calculateScore(tdm.TDM,queryVector)
    t5=timeit.default_timer()
    print("query time: ",t5-t4)
    topN=findTopN(score,3)
    for index,score in topN:
        print(corpus[corpusIndextoDocNoMapping[index]])

