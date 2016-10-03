import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer

def sentence_tokenization():
	text = "Mr. Obama is the president of the United States. He was elected in 2008."

	sentences = nltk.sent_tokenize(text)
	print sentences

def word_tokenization():
	text = "Mr. Obama is the president of the United States."

	words = nltk.word_tokenize(text)
	print words

def parts_of_speech():
	text = "Mr. Obama is the president of the United States."

	words = nltk.word_tokenize(text)
	tagged_words = nltk.pos_tag(words)
	print tagged_words
	#print nltk.help.upenn_tagset("NNP") # what a tag means

def stemming(): # base or root of a word
	words = ["saying", "crying", "octopus", "cement"]

	# two different implementation of stemmers
	porter_stemmer = PorterStemmer()
	lancaster_stemmer = LancasterStemmer()
	for w in words:
		print porter_stemmer.stem(w), lancaster_stemmer.stem(w)

def chunking():
	text = "the little yellow dog barked at the cat"

	# the regular expression being used only works with determiners, adjectives, and nouns
	words = nltk.word_tokenize(text)
	tagged = nltk.pos_tag(words)
	chunker = nltk.RegexpParser("NP: {<DT>?<JJ>*<NN>}") # determiner, adjectives, noun
	result = chunker.parse(tagged)
	print result
	#result.draw() # draws the tree

def named_entity():
	text = "Barack Obama is the president of the United States of America"

	words = nltk.word_tokenize(text)
	tagged = nltk.pos_tag(words)
	entities = []
	parse_tree = nltk.ne_chunk(tagged, binary=True)
	for tree in parse_tree.subtrees():
	    if tree.label() == 'NE':
	    	entity = ""
	    	for t in tree:
	        	entity += " " + t[0]
	        entities.append(entity[1:])
	print entities

sentence_tokenization()