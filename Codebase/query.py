from preprocessing import processText
from IndexLoader import loadResourceDriver,Resource
from documentSimilarity import calculateScore,findTopN
import timeit
loadResourceDriver()

def query(text,topN=5):
    t4=timeit.default_timer()
    searchQuery=processText(text)
    queryVector=Resource.tdm.transform(searchQuery)
    score=calculateScore(Resource.tdm.TDM,queryVector)
    t5=timeit.default_timer()
    #print("query time: ",t5-t4)
    topN=findTopN(score,topN)
    return topN


