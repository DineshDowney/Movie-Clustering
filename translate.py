from googletrans import Translator
import nltk
trans = Translator()
arr = [(i,trans.translate(i,dest="hi").text) for i in nltk.corpus.stopwords.words('english')]
print(arr)