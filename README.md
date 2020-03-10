# BasicSearchEngine
Basic Search Engine (An Information Retrieval System) from scratch Using python:

<h1>1.	Introduction:</h1>
<h3>a.	Motivation:</h3>
<p>The general objective of search engine is to minimize the overhead of user to locating the needed information. There can be various types of overheads like, time to spend in search of the document containing the needed information. Since currently approximately 180 quadrillion web pages are there in the World Wide Web so it is impossible to get the needed information by looking at it. Some popular search engines: 1. Google 2. Bing 3. Yahoo 4. Baidu 4. Yandex.ru 5.DuckDuckGo 6.Ask.com 7.AOL.com.<p>

<h3>b.	Definition: </h3>
<p>Information retrieval is finding material (usually documents) of an unstructured nature (usually text, image, and video) that satisfies an information need from within large collections (usually stored on computers).</p>

<h2>2.	Process of information retrieval:</h2>
<h3>a.	Composition:</h3>
Motivation:
For small number of text document it is possible create a full text search engine to directly scan the contents of each document with a query using a strategy called Serial Scanning. This is some tools such as grep, do when searching in Linux.
However, when the number of documents to search is potentially large, or the quantity of search queries to perform is substantial, the above method is not optimal so the problem of full-text search is often divided into two tasks: indexing and searching. 

<h4>i.	Text indexing (Document Indexing)</h4>
The indexing stage will scan the text of all the documents and build a list of search terms often called an index, but more correctly named a concordance(an alphabetical list of the words (especially the important ones) present in a text or texts)

<h4>ii.	Searching (consist of query and document ranking)</h4>
The indexing stage will scan the text of all the documents and build a list of search terms often called an index, but more correctly named a concordance(an alphabetical list of the words (especially the important ones) present in a text

<b>overall process flow</b>
![Image of process flow](https://github.com/ravisarojjnu/BasicSearchEngine/blob/master/images/Untitled-4.jpg)

<b>Indexing<b>
![Image of process flow of indexing](https://github.com/ravisarojjnu/BasicSearchEngine/blob/master/images/Indexing.jpg)

<b>Searching<b>
![Image of process flow of Searching](https://github.com/ravisarojjnu/BasicSearchEngine/blob/master/images/searching.jpg)
