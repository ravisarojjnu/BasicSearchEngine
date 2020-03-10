from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
from nltk import word_tokenize
import re
stopwordSet=stopwords.words("english")
lemmatizer = WordNetLemmatizer()
#regular expression for html tags
htmlClean = re.compile('<.*?>')

#regular expression for email
emailRE = re.compile(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+")

def processText(text):
    """ preprocess pipeline"""
    text=str(text)
    text=text.lower()
    text=removeHtmlTags(text)
    text=replaceNumber(text,"NUMBER")
    text=replaceEmail(text,"EMAIL")
    text=replaceCurrencySign(text,"CURRENCY")
    text=replaceLink(text,"LINK")
    text=retainOnlyLanguageSigns(text)
    text=removeNewLine(text)
    text=removeTab(text)
    text=removeSpace(text)
    filteredToken=removeStopwards(text)
    filteredToken=lemmatize(filteredToken)
    return filteredToken

def removeHtmlTags(text):
    """Remove html tags from a string"""
    return re.sub(htmlClean,'', text)

def replaceEmail(text,tag):
    """ replace emails to given tag """
    return re.sub(emailRE,tag,text)

def replaceNumber(text,tag):
    """ remove number """
    return re.sub(r"[0-9]+",tag+" ",text)

def replaceLink(text,tag):
    return re.sub(r"(http|https)://[^\s]*", tag+" ", text)

def replaceCurrencySign(text,tag):
    """replace currency sign"""
    return re.sub(r"[$]+",tag+" ", text)

def retainOnlyLanguageSigns(text):
    """retain only english alphabet"""
    return re.sub(r"[^a-zA-Z0-9]",' ',text)

def removeSpace(text):
    """remove mulitple spaces"""
    return re.sub(r" +",' ',text)

def removeNewLine(text):
    """remove mulitple New line"""
    return re.sub(r"\n+",' ',text)

def removeTab(text):
    """remove mulitple tabs"""
    return re.sub(r"\t+",' ',text)

def removeStopwards(text):
    """remove stopwords"""
    tokenList=word_tokenize(text)
    filteredTokens=[word for word in tokenList if word not in stopwordSet]
    return filteredTokens

def lemmatize(tokens):
    lemmatizeTokens=[lemmatizer.lemmatize(word) for word in tokens]
    return lemmatizeTokens

#test code
if __name__=="__main__":
    text="<div >Embedding code in Medium is pretty easy.    send mail to ravisarojjnu@gmail.com and 2000 $ to 19199191292.</div>"
    print(processText(text))
    
