# TextBlob
# URL https://textblob.readthedocs.io/en/dev/advanced_usage.html#sentiment-analyzers
# This is an example of what can you do with this lib

# Sentiment analyzer train onto movies reviews
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
blob = TextBlob("I love this library", analyzer=NaiveBayesAnalyzer())
blob.sentiment

# Tokenizer
from nltk.tokenize import TabTokenizer
tokenizer = TabTokenizer()
blob = TextBlob("This is\ta rather tabby\tblob.", tokenizer=tokenizer)
blob.tokens

#This is an alternative way
tokenizer = BlanklineTokenizer()
blob = TextBlob("A token\n\nof appreciation")
blob.tokenize(tokenizer)

# Noun phrase chunkers
from textblob.np_extractors import ConllExtractor
extractor = ConllExtractor()
blob = TextBlob("Python is a high-level programming language.", np_extractor=extractor)
blob.noun_phrases

# POS taggers
from textblob.taggers import NLTKTagger
nltk_tagger = NLTKTagger()
blob = TextBlob("Tag! You're It!", pos_tagger=nltk_tagger)
blob.pos_tags

# Parser
from textblob.parsers import PatternParser
blob = TextBlob("Parsing is fun.", parser=PatternParser())
blob.parse()

# TextBlob that share same model
rom textblob.taggers import NLTKTagger
tb = Blobber(pos_tagger=NLTKTagger())
blob1 = tb("This is a blob.")
blob2 = tb("This is another blob.")
blob1.pos_tagger is blob2.pos_tagger
