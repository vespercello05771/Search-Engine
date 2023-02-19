from util import *
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import TreebankWordTokenizer
import re
# Add your import statements here




class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = []
		ans = []
		for sen in text:
			temp = word_tokenize(sen.lower())
			ans.append(temp)

		for sen in ans:
			t = []
			for w in sen:
				w = re.sub(r'[^\w\s]','',w)
				if w!='':
					t.append(w)
			tokenizedText.append(t)

		#Fill in code here

		return tokenizedText


		



	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizer = TreebankWordTokenizer()
		tokenizedText = []
		ans = []
		for sen in text:
			temp = tokenizer.tokenize(sen)
			ans.append(temp) 
		for sen in ans:
			t = []
			for w in sen:
				w = re.sub(r'[^\w\s]','',w)
				if w!='':
					t.append(w)
			tokenizedText.append(t)

		#Fill in code here

		return tokenizedText