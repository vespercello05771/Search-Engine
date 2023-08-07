from util import *
import math
# Add your import statements here




class Evaluation():

	def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The precision value as a number between 0 and 1
		"""

		precision = -1

		#Fill in code here
		precision = 0.0
		predicted_docs = query_doc_IDs_ordered[:k]
		common = list(set(predicted_docs)&set(true_doc_IDs))

		precision = len(common)/k

		return precision


	def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean precision value as a number between 0 and 1
		"""

		meanPrecision = -1

		#Fill in code here
		total_precision = 0.0
		# Iterate over the queries
		
		for i, query_id in enumerate(query_ids):
			relevant_docs = []
			for j in qrels :
				if int(j["query_num"]) == query_id :
					relevant_docs.append(int(j["id"]))
		
			total_precision += self.queryPrecision(doc_IDs_ordered[i],query_id,relevant_docs,k)
		
		meanPrecision = total_precision / len(query_ids)
		
		
		return meanPrecision

	
	def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""

		recall = -1

		#Fill in code here

		predicted_docs = query_doc_IDs_ordered[:k]
		common = list(set(predicted_docs) & set(true_doc_IDs))
		recall = len(common)/len(true_doc_IDs)
		return recall


	def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean recall value as a number between 0 and 1
		"""

		meanRecall = -1

		#Fill in code here
		totalRecall = 0.0

	
		for i,query_id in enumerate(query_ids):
			relevant_docs = []
			for j in qrels :
				if int(j["query_num"]) == query_id :
					relevant_docs.append(int(j["id"]))
		

			totalRecall+=self.queryRecall(doc_IDs_ordered[i],query_id,relevant_docs,k)

		meanRecall = totalRecall/len(query_ids)
	

		return meanRecall


	def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The fscore value as a number between 0 and 1
		"""

		fscore = -1

		#Fill in code here
		fscore = 0.0
		precision = self.queryPrecision(query_doc_IDs_ordered,query_id,true_doc_IDs,k)
		recall = self.queryRecall(query_doc_IDs_ordered,query_id,true_doc_IDs,k)
		if(precision == 0 or recall ==0 ):
			fscore = 0
		else :
			fscore = 2*precision*recall
			fscore = fscore/(precision+recall)
		return fscore


	def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value
		
		Returns
		-------
		float
			The mean fscore value as a number between 0 and 1
		"""

		meanFscore = -1

		#Fill in code here
		totalFscore = 0.0
		for i,query_id in enumerate(query_ids) :
			relevant_docs = []
			for j in qrels :
				if int(j["query_num"]) == query_id :
					relevant_docs.append(int(j["id"]))

			
			totalFscore+=self.queryFscore(doc_IDs_ordered[i],query_id,relevant_docs,k)

		meanFscore = totalFscore/len(query_ids)
		

		return meanFscore
	

	def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs,relevance, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : list
			The relevance values corresponding to true_doc_IDs
		arg5 : int
			The k value
		

		Returns
		-------
		float
			The nDCG value as a number between 0 and 1
		"""

		nDCG = -1
		
		#Fill in code here
		predicted_doc_relevance = list()
		query_doc_IDs_ordered 
		for i in query_doc_IDs_ordered :
			if i in true_doc_IDs :
				ind = true_doc_IDs.index(i)
				predicted_doc_relevance.append([i,relevance[ind]])
			else :
				predicted_doc_relevance.append([i,0])

		actual_DCG = 0.0
		for i in range(k):
			actual_DCG+=predicted_doc_relevance[i][1]/math.log2(i+2)

		ideal_DCG = 0.0
		predicted_doc_relevance = predicted_doc_relevance[:k]
		predicted_doc_relevance.sort(key = lambda x:x[1])
		predicted_doc_relevance.reverse()	
		for i in range(k) :
			ideal_DCG+=predicted_doc_relevance[i][1]/math.log2(i+2)	

		nDCG=0.0
		if ideal_DCG > 0  :
			nDCG = actual_DCG / ideal_DCG  
		
		return nDCG


	def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean nDCG value as a number between 0 and 1
		"""

		meanNDCG = -1

		#Fill in code here
		
		totalndcg = 0.0
		for i,query_id in enumerate(query_ids) :
			relevant_docs = []
			relevance = []
			for j in qrels :
				if int(j["query_num"]) == query_id :
					relevant_docs.append(int(j["id"]))
					relevance.append(5-j["position"])
			
			totalndcg+=self.queryNDCG(doc_IDs_ordered[i],query_id,relevant_docs,relevance,k)

		meanNDCG = totalndcg/len(query_ids)


		return meanNDCG


	def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precision@i
		values for i such that the ith document is truly relevant)

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The average precision value as a number between 0 and 1
		"""

		avgPrecision = -1

		#Fill in code here
		
		precision_sum = 0.0
		num_true_docs_seen = 0
		for i in range(k):
			if query_doc_IDs_ordered[i] in true_doc_IDs:
				num_true_docs_seen += 1
				precision_sum+= num_true_docs_seen/(i+1)
		if num_true_docs_seen==0:
			return 0.0
		
		avgPrecision = precision_sum / num_true_docs_seen

		return avgPrecision


	def meanAveragePrecision(self, doc_IDs_ordered, query_ids, q_rels, k):
		"""
		Computation of MAP of the Information Retrieval System
		at given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The MAP value as a number between 0 and 1
		"""

		meanAveragePrecision = -1

		#Fill in code here
		totalAveragePrecision = 0
		for i,query_id in enumerate(query_ids) :
			relevant_docs = []
			for j in q_rels :
				if int(j["query_num"]) == query_id :
					relevant_docs.append(int(j["id"]))
		
			totalAveragePrecision+=self.queryAveragePrecision(doc_IDs_ordered[i],query_id,relevant_docs,k)

		meanAveragePrecision = totalAveragePrecision/len(query_ids)

	
		return meanAveragePrecision

