from util import *
from nltk.tokenize import sent_tokenize
import re
# Add your import statements here




class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""

		op_list = list()
		string = ""
		for i in text :
		 if(i == '.') :
				string+=i
				op_list.append(string)
				string = ""
		 elif i == '!' :
				string+=i
				op_list.append(string)
				string = ""
		 elif i == '?' :
				string+=i
				op_list.append(string)
				string = ""
		 else :
				string+=i

		segmentedText = op_list

		#Fill in code here

		return segmentedText





	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""

		
		segmentedText = None
		segmentedText = sent_tokenize(text)

		#Fill in code here

		return segmentedText