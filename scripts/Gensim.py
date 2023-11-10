# python -m spacy download en_core_web_md
# python -m spacy download pt_core_news_md
# python -m spacy download es_core_news_md

import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from data import Repository
import nltk
import re

nltk.download('punkt')
nltk.download('stopwords')

# Carrega o modelo em português
nlp = spacy.load('pt_core_news_md')


def cleanText(text):
    text = text.lower()
    string = re.findall(r"\b[a-zA-Z0-9]+\b|[,.)('\"\[\];><:\\/@!#$%¨&*_+=]", text)
    words = word_tokenize(text)
    stop_words = set(stopwords.words('portuguese'))
    words = [word for word in text if word not in stop_words]
    return words


# Cria dois objetos Doc
doc1 = cleanText(nlp(Repository.products[0][0]))
doc2 = cleanText(nlp(Repository.products[1][0]))
# Calcula a similaridade entre os dois objetos Doc
similarity = doc1.similarity(doc2)
print(Repository.products[0][0] + " ", Repository.products[1][0] + " ", similarity)


# print(Repository.products)
