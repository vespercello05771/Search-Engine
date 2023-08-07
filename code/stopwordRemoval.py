from util import *
import nltk
from nltk.corpus import stopwords
# Add your import statements here




class StopwordRemoval():

	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""

		stopwordRemovedText = None
		stop_words = set(stopwords.words('english'))
		ans = []
		for i in text:
			temp = []
			for j in i:
				if j.lower() not in stop_words:
					temp.append(j.lower())
			ans.append(temp)

		return ans




	