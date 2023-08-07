from util import *
import numpy as np
import math
from sklearn.decomposition import TruncatedSVD
# Add your import statements here






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
		index = self.index
		# print(index['idf'])
		tfs = index['tf']
		idf = [list(index['idf'].values())]
		idf = np.array(idf)
		# idf = idf.transpose()
		IRDIC = index['tf']
		matrix = []
		for k in IRDIC.keys():
			matrix.append(list(IRDIC[k]))
		matrix = np.array(matrix,dtype='float')#term x doc matrix
		# print(matrix)
		# applying svd for choosing better words


		docIds = index['docIDs']
		allwords = index['allwords']
		doc_IDs_ordered = []
		Qtfs = []
		matrix = matrix.T
		# calculation term frequencies for the unique set of words already present in the corpus.
		for i in range(matrix.shape[0]):
			summ = len([x for x in matrix[i,:] if x!=0])
			if summ!=0:
				matrix[i,:] = (matrix[i,:]+1)/summ
			else :
				continue
		# print("here"+str(matrix))
		matrix = np.multiply(matrix,idf)
		# print(matrix.shape)
		componerts = int(len(allwords)*0.1)
		lsa_model = TruncatedSVD(n_components=componerts)
		lsa_vectors = lsa_model.fit_transform(matrix)
		# print(lsa_vectors)
		# Qmatrix = 
		ans = []

		for query in queries:
			qvector = [0]*len(allwords)
			for s in query:
				for w in s:
					if w in allwords:
						ind = allwords.index(w)
						qvector[ind]+=1
			qvector = np.array([qvector])
			qvector = lsa_model.transform(qvector)
			temp = np.multiply(lsa_vectors,qvector)
			# print("qvector"+str(qvector))
			# print("lsaVector"+str(lsa_vectors))
			cosine = []
			# docId = 0
			for i in range(temp.shape[0]):
				temp2 = np.sum(temp[i,:])
				temp3 = np.sum(np.multiply(lsa_vectors[i,:],lsa_vectors[i,:]))+np.sum(np.multiply(qvector,qvector))
				if(temp3==0):
					cosine.append([0,docIds[i]])
				# temp2 = temp2/
				else:
					cosine.append([temp2/temp3,docIds[i]])
			cosine = sorted(cosine, key=lambda x: x[0])
			#print(cosine)
			rankedList = [x[1] for x in cosine]
			rankedList = rankedList[::-1]
			#print(rankedList)

			ans.append(rankedList)

		return ans



    # for i in range(len(queries)):
	# 		query = queries[i]
	# 		temp = {}
	# 		for w in allwords:
	# 			temp[w]=0
	# 		for s in query:
	# 			for w1 in s:
	# 				if w1 in allwords:
	# 					temp[w1]+=1
	# 		Qtfs.append(list(temp.values()))
	# 	Qtfs = np.array(Qtfs)
	# 	Qtfs = Qtfs.transpose()
	# 	tfarray = []
	# 	for w in allwords:
	# 		tfarray.append(tfs[w])
	# 	tfarray = np.array(tfarray)
	# 	nq = len(queries)
	# 	nd = len(docIds)
	# 	for i in range(nd):
	# 		tfarray[:,i] = np.multiply(tfarray[:,i],idf)
	# 	for i in range(nq):
	# 		Qtfs[:,i]=np.multiply(Qtfs[:,i],idf)
	# 	orders = []
	# 	# getting cosine similarities for all the queries x documents
	# 	for i in range(nq):
	# 		temp = []
	# 		for j in range(nd):
	# 			q = Qtfs[:,i]
	# 			d = tfarray[:,j]
	# 			numerator = np.sum(np.multiply(q,d))
	# 			denominator = math.sqrt(np.sum(np.square(q))+np.sum(np.square(d)))
	# 			if denominator > 0 :
	# 				temp.append([docIds[j],numerator/denominator])
	# 			else :
	# 				temp.append([docIds[j],0])
			
	# 		temp.sort(key = lambda x: x[1])
	# 		# copying all the ranks
	# 		temp.reverse()
	# 		temp2 = []
	# 		for t1 in temp:
	# 			temp2.append(t1[0])

	# 		orders.append(temp2)