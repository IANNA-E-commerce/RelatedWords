# python -m spacy download en_core_web_md
# python -m spacy download pt_core_news_md
# python -m spacy download es_core_news_md

import spacy

from scripts.TreatData import TreatData

# nltk.download('punkt')
# nltk.download('stopwords')

# Carrega o modelo em português
nlp = spacy.load('pt_core_news_md')

def

# Cria dois objetos Doc
doc1 = TreatData.clean_and_refactoring_text("açAí caiu morrera chutou abraçará colhendo abrasivo mouse abraçar-te-ia",
                                            "pt_BR", nlp)
# doc2 = clean_text(Repository.products[1][0])
print(doc1)
# print(doc2)

# Calcula a similaridade entre os dois objetos Doc
# similarity = doc1.similarity(doc2)
# print(Repository.products[0][0] + " ", Repository.products[1][0] + " ", similarity)


# print(Repository.products)
