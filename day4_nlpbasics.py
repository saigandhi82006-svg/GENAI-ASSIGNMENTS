#Sentence Tokenization
# from nltk import sent_tokenize
# import nltk
# nltk.download('punkt_tab')
#text="Artificial Intelligence is transforming industries. NLP is a key part of AI. Tokenization is the first NLP step."
# sentences=sent_tokenize(text)
# print(sentences)

#Word Tokenization
# from nltk import word_tokenize
# words=word_tokenize(text)
# print(words)

#Stemming Using Porter Stemmer
from nltk.stem import PorterStemmer
st=PorterStemmer()
# list1=["playing", "played", "plays", "happily", "studies"]
# for i in list1:
#     print("OriginalWord ",i)
#     print("Stem ",st.stem(i))

#Lemmatization With wordnet
from nltk.stem import WordNetLemmatizer
# import nltk
# nltk.download('wordnet')
wd=WordNetLemmatizer()
# list2=["running", "cars", "better", "children", "feet"]
# for i in list2:
#     print("Original Word ",i)
#     print("Lemma ",wd.lemmatize(i,pos='n'))

#Stemming VS Lemmatization
list3=["playing","whispering","children","Gandhi","dhurandhar"]
for i in list3:
    print(f"word:{i} | Stem:{st.stem(i)} | Lemma:{wd.lemmatize(i,pos="n")}")









