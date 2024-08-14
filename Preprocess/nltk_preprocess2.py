import regex as re
import string
import nltk
from nltk.stem import WordNetLemmatizer

# removing stop words
stops = nltk.corpus.stopwords.words('english')

# this function pre-processes our text
def preProcessText(text):
	processed = []
	for doc in range(len(text)):
		doc = re.sub(r"\\n", "", doc)
		doc = re.sub(r"\W", " ", doc) #remove non words char
		doc = re.sub(r"\d"," ", doc) #remove digits char
		doc = re.sub(r'\s+[a-z]\s+', "", doc) # remove a single char
		doc = re.sub(r'^[a-z]\s+', "", doc) #remove a single character at the start of a document
		doc = re.sub(r'\s+', " ", doc)  #replace an extra space with a single space
		doc = re.sub(r'^\s', "", doc) # remove space at the start of a doc
		doc = re.sub(r'\s$', "", doc) # remove space at the end of a document
		processed.append(doc.lower())
	return processed

def tokenize(text):
	tokens = re.split('W+',text)
	return tokens

def removeStopWords(text):
	text = [word for word in text if word not in stops]
	return text


# lemmatization of text
wnl = WordNetLemmatizer()

def lemmatize(text):
	lemm_text = [wnl.lemmatize(word) for word in text]
	return lemm_text

def process(text):
	text = list(map(preProcessText, text))
	text = list(map(tokenize, text))
	text = list(map(removeStopWords, text))
	text = list(map(lemmatize, text))
	return text
