from util import *
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
# Add your import statements here




class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""

		reducedText = None
		ans = []

		#Fill in code here
		stemmer = PorterStemmer()
		for sen in text:
			t = []
			for w in sen:
				temp = stemmer.stem(w)
				t.append(temp)
			ans.append(t)
		reducedText=[]
		lemmatizer = WordNetLemmatizer()
		for sen in ans:
			t = []
			for w in sen:
				temp = lemmatizer.lemmatize(w)
				t.append(temp)
			reducedText.append(t)
		return reducedText

