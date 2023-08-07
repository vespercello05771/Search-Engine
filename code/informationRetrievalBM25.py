import math
from rank_bm25 import BM25Okapi

def merge(input_nestedlist) :
	resultList = []

	# Traversing in till the length of the input list of lists
	for m in range(len(input_nestedlist)):

	# using nested for loop, traversing the inner lists
	
		for n in range(len(input_nestedlist[m])):
			# Add each element to the result list
			resultList.append(input_nestedlist[m][n])
	
	return resultList


class InformationRetrieval():

	def init(self):
		self.index = None

	def buildIndex(self, docs, docIDs):
		"""
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""

		index = None
		# code here
		docDic = {}
		
		IRdic = {}
		
		allwords = []
		# creating dictionary with set of unique words in the corpus.
		for d in range(len(docs)):
			doc = docs[d]
			for s in doc:
				for w in s:
					if w not in allwords:
						allwords.append(w)
						IRdic[w]=[0]*len(docIDs)
						IRdic[w][d]+=1
					else:
						IRdic[w][d]+=1

		IDFdic = {}
		# calculating IDF values for the set of unique words in the corpus
		for w in allwords:
			l=IRdic[w]
			temp = 0
			for t in l:
				if(t!=0):
					temp+=1
			IDFdic[w]=math.log10(len(docIDs)/temp)
		
		index = {}
		# copying all info
		index['tf']=IRdic
		index['idf']=IDFdic
		index['docIDs']=docIDs
		index['allwords']=allwords
		index['docs']=docs
		self.index = index
		

	def rank(self, queries):
		"""
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""
		tokenized_corpus = []
		# reduce lists to merge sentences of each doc
		for lists in self.index['docs'] :
			tokenized_corpus.append(merge(lists))


		
		bm25 = BM25Okapi(tokenized_corpus)
		ans = []
		for query in queries:
			tokenizer_query = []
			for s in query:
				for w in s:
					tokenizer_query.append(w)
			doc_scores = bm25.get_scores(tokenizer_query)
			ranked_list = bm25.get_top_n(tokenizer_query,self.index['docIDs'], n=1400)
			ans.append(ranked_list)
		return ans