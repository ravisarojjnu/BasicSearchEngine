import heapq

def calculateScore(TDM,queryVector):
    score=[0 for _ in range(len(TDM))]
    for i,row in enumerate(TDM):
        score[i]=vectorDot(row,queryVector)
    return score

def vectorDot(u,v):
    sum=0
    for i,ele in enumerate(u):
        sum=sum+ele*v[i]
    return sum

def findTopN(score,top):
    scoreWithIndex=zip(range(len(score)),score)
    topScore=heapq.nlargest(top,scoreWithIndex,key=lambda x:x[1])
    return topScore






