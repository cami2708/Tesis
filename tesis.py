
#####Importing libraries#####
import nltk
import numpy as np
import matplotlib.pyplot as plt
import json

from nltk.stem import WordNetLemmatizer
from sklearn.decomposition import TruncatedSVD
from pprint import pprint

#Uploading Twitter data
json_data = open('DB/00test.json').read()
data=json.loads(json_data)

# with open('DB/00test.json') as data_file:
#     data_item = json.load(data_file)
# pprint(data_item)

#I care about: 
# text
# in_reply_to_status_id
# in_reply_to_status_id_str
# in_reply_to_user_id
# in_reply_to_user_id_str
# in_reply_to_screen_name
# user[lang]
# country_code

#This is for practice how to call the DB
#print data["id"][12]

print "Hola"

wordNetLemmatizer = WordNetLemmatizer()

#titles = [line.rstrip() for line in open('all_book_titles.txt')]

stopWords = set(w.rstrip() for w in open('stopwords.txt'))
stopWords = stopWords.union({
	'introduction', 'edition', 'series', 'application',
	'approach', 'card', 'access', 'package', 'plus', 'etext',
	'brief', 'vol', 'fundamental', 'guide', 'essential', 'printed',
	'third', 'second', 'fourth',
	})


#####Data preparation to remove stop words#######
#Defining function to remove stop words
def tokenizer(s):
	#All word to lowercase
	s = s.lower()
	tokens = nltk.tokenize.word_tokenize(s)
	tokens = [t for t in tokens if len(t) > 2]
	tokens = [wordNetLemmatizer.lemmatize(t) for t in tokens]
	tokens = [t for t in tokens if t not in stopWords]
	tokens = [t for t in tokens if not any(c.isdigit() for c in t)]
	return tokens

wordIndexMap = {}
currentIndex = 0
allTokens = []
allTitles = []
indexWordMap = []

# for title in titles:
#     try:
#         title = title.encode('ascii', 'ignore') # this will throw exception if bad characters
#         allTitles.append(title)
#         tokens = tokenizer(title)
#         allTokens.append(tokens)
#         for token in tokens:
#             if token not in wordIndexMap:
#                 wordIndexMap[token] = currentIndex
#                 currentIndex += 1
#                 indexWordMap.append(token)
#     except:
#         pass











