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
![Image of process flow](https://github.com/ravisarojjnu/BasicSearchEngine/blob/master/images/Untitled-1.jpg)

<b>Indexing<b>
![Image of process flow of indexing](https://github.com/ravisarojjnu/BasicSearchEngine/blob/master/images/Indexing.jpg)

<b>Searching<b>
![Image of process flow of Searching](https://github.com/ravisarojjnu/BasicSearchEngine/blob/master/images/searching.jpg)

<h2>3. Results</h2>
<i>query="what are the structural and aeroelastic problems associated with flight of high speed aircraft ."</i>
<h4>Some top Results</h4>
<h5>Result1.</h5> 
<p>some structural and aerelastic considerations of high speed flight . the dominating factors in structural design of high-speed aircraft are thermal and aeroelastic in origin . the subject matter is concerned largely with a discussion of these factors and their interrelation with one another . a summary is presented of some of the analytical and experimental tools available to aeronautical engineers to meet the demands of high-speed flight upon aircraft structures . the state of the art with respect to heat transfer from the boundary layer into the structure, modes of failure under combined load as well as thermal inputs and acrothermoelasticity is discussed . methods of attacking and alleviating structural and aeroelastic problems of high-speed flight are summarized . finally, some avenues of fundamental research are suggested.</p>
<h5>Result2.</h5> 
<p>theory of aircraft structural models subjected to aerodynamic heating and external loads .the problem of investigating the simultaneous effects of transient aerodynamic heating and external loads on aircraft structures for the purpose of determining the ability of the structure to withstand flight to supersonic speeds is studied . by dimensional analyses it is shown that . constructed of the same materials as the aircraft will be thermally similar to the aircraft with respect to the flow of heat through the structure will be similar to those of the aircraft when the structural model is constructed at the same temperature as the aircraft . external loads will be similar to those of the aircraft . subjected to heating and cooling that correctly simulate the aerodynamic heating of the aircraft, except with respect to angular velocities and angular accelerations, without requiring determination of the heat flux at each point on the surface and its variation with time . acting on the aerodynamically heated structural model to those acting on the aircraft is determined for the case of zero angular velocity and zero angular acceleration, so that the structural model may be subjected to the external loads required for simultaneous simulation of stresses and deformations due to external loads .</p>

<h4>As you can see the results are pretty relevant to the query.</h4>

<h2>4. Conclusion</h2>
<p>Since In the implementation I have used pure python data structures and operations. There are many optimizations are left such as I have used list of list in-place of sparse matrix to represent the term document matrix (since document vector is sparse in nature). In the next blog I will optimize the performance of the search engine using right data structures and linear algebra libraries. Currently the search query time is 1.5 second with 1400 documents and 6000 vocab size which is very high as for the given data set.</p>

<h3>5. References</h3><p>
i. Speech and Language Processing (3rd ed. draft) Dan Jurafsky and James H. Martin<br>
ii. https://en.wikipedia.org/wiki/Dot_product<br>
iii. https://en.wikipedia.org/wiki/Cosine_similarity<br>
iv. https://en.wikipedia.org/wiki/Document-term_matrix<br>
v. https://www.sciencedirect.com/topics/computer-science/information-retrieval-systems<br>
vi. https://medium.com/@ravisarojjnu/basic-search-engine-an-information-retrieval-system-from-scratch-using-python-153c9bead8e1
<p>
  


  
