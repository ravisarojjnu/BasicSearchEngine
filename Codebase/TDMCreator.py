from collections import Counter
import math
class TermDocumentMatrix:

    def createFeatureAndTransform(self,corpus):
        """ input the processed corpus 
        driver function to compute the Term frequency and inverse document frequency
        """
        self.corpus=corpus
        self.corpusSize=len(corpus)
        self._createTokenToIndex()
        self._createTDM()
        self._calculateIDF()
        self._calculateTFIDF()
        self._normalize()

    def transform(self,doc):
        """Transform the processed doc to query vector"""
        vector=self._docToVector(doc)
        vectorNorm=self._vectorNorm(vector)
        for i,ele in enumerate(vector):
             vector[i]=ele/(vectorNorm+1)
        return vector

    def _docToVector(self,doc):
        """Transform the processed doc to query vector"""
        vector=[0 for i in range(len(self.vocab))]
        tokenCountDic=Counter(doc)
        for word,count in tokenCountDic.items():
            if self.tokenToIndex.get(word):
                #computing the tfidf
                vector[self.tokenToIndex[word]]=math.log10(count+1)*self.idf[self.tokenToIndex[word]]
        return vector

    def _createTokenToIndex(self):
        """ Function to compute vocab and create token to index dictionary"""
        self.vocab=set()
        self.tokenToIndex={}
        #finding unique tokens
        for doc in self.corpus:
            for token in doc:
                self.vocab.add(token)
        #creating dictionary of terms with index
        for i,token in enumerate(self.vocab):
            self.tokenToIndex[token]=i
    
    def _createTDM(self):
        """ function to create count TDM """
        self.TDM=[[0 for i in range(len(self.vocab))] for _ in range(len(self.corpus))]
        for i,doc in enumerate(self.corpus):
            #counting frequency of each token in the document
            countDic=Counter(doc)
            for word,count in countDic.items():
                self.TDM[i][self.tokenToIndex[word]]=count

    def _calculateIDF(self):
        """calculating the inverse document frequency"""
        self.idf=[0 for i in range(len(self.vocab))]
        #finding docuemnt frequency
        for row in self.TDM:
            for i,ele in enumerate(row):
                if ele>0:
                    self.idf[i]=self.idf[i]+1
        #computing the inverse docuemnt frequency
        for i,ele in enumerate(self.idf):
            self.idf[i]=math.log10((self.corpusSize/self.idf[i])+1)

    def _calculateTFIDF(self):
        """function to compute term frequenct inverse document frequency"""
        for i,row in enumerate(self.TDM):
            for j,ele in enumerate(row):
                #computing normalized document frequency inverse document frequency
                self.TDM[i][j]=math.log10(self.TDM[i][j]+1)*self.idf[j]
    
    def _normalize(self):
        """for normalizing the TDM"""
        for i,row in enumerate(self.TDM):
            vectorNorm=self._vectorNorm(row)
            for j,ele in enumerate(row):
                self.TDM[i][j]=ele/(vectorNorm+1)

    def _vectorNorm(self,vector):
        sum=0
        for ele in vector:
            sum=sum+ele**2
        return math.sqrt(sum)

if __name__=="__main__":
    from preprocessing import processText
    corpus=["Text analysis is fun",
    "I like doing text analysis",
    "I like puppies, they are fun",
    "I like like this blog post",]
    processedCorpus=[]
    search=corpus[3]
    for doc in corpus:
        prcessedDoc=processText(doc)
        processedCorpus.append(prcessedDoc)
    tdm=TermDocumentMatrix()
    tdm.createFeatureAndTransform(processedCorpus)
    print(tdm.transform(processText(search)))




    
        
        





        