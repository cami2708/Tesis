# Data pre-process

#####Importing libraries#####
import nltk
import numpy as np
import matplotlib.pyplot as plt
import json
import codecs
import urllib2
import io

from nltk.stem import WordNetLemmatizer
from sklearn.decomposition import TruncatedSVD
from pprint import pprint


#Uploading Twitter data
json_data = open('DB/01.json').read()
data = json.loads(json_data)
#I care about: 
# text
# in_reply_to_status_id
# in_reply_to_status_id_str
# in_reply_to_user_id
# in_reply_to_user_id_str
# in_reply_to_screen_name
# user[lang]
# country_code

# Uncoment for python 3
# with open('DB/01.json') as data_file:
#     data_item = json.load(data_file)
# pprint(data_item)


#English data
enData = []


for i in range(0,len(data)):
	if data[i]["lang"] == "en":
		singleEnData = [data[i]]
		enData.append(singleEnData)

# Get the number of tweet in English
# print len(enData)

# Get a single text from twitterText DB
# print enData["Text"][1][0]

#Save the data
with io.open('DB/enData.json', 'w', encoding='utf-8') as f:
	f.write(json.dumps(enData, ensure_ascii=False))




