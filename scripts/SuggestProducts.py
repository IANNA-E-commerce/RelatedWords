# python -m spacy download en_core_web_md
# python -m spacy download pt_core_news_md
# python -m spacy download es_core_news_md
import os

import spacy

from scripts.TreatData import TreatData

# nltk.download('punkt')
# nltk.download('stopwords')

# Carrega o modelo em português
nlp = spacy.load('pt_core_news_md')


# Cria dois objetos Doc
# doc1 = TreatData.clean_and_refactoring_text("açAí caiu morrera chutou abraçará colhendo abrasivo mouse abraçar-te-ia",
#                                             "pt_BR", nlp)
# doc2 = clean_text(Repository.products[1][0])
# print(doc1)
# print(doc2)

# Calcula a similaridade entre os dois objetos Doc
# similarity = doc1.similarity(doc2)
# print(Repository.products[0][0] + " ", Repository.products[1][0] + " ", similarity)
class SuggestProducts:
    def classifier_words(array_words):
        name_products_weg = \
            ["motor", "bomba", "turbina", "partida", "suave", "subestação", "sensor"
                                                                            "câmera", "controle", "gerador",
             "hidrogerador", "wemob", "inversor",
             "painél", "painel", "cubículo", "redutor", "plugue", "relé", "relê", "sensor",
             "software", "tinta", "tomada", "motorredutor", "transformador", "secionador",
             "turbogerador", "módulo", "regulador", "conversor", "verniz", "reator"]

        # na matriz: [[atributos][nomes produtos]]
        words_classified = [[], []]
        for word in array_words:
            if word in name_products_weg:
                words_classified[1].append(word)
            else:
                words_classified[0].append(word)
        SuggestProducts.search_db(words_classified)

    def search_db(words_classified):
        data_db = {}
        path = os.path.join('dict', 'data_db.csv')
        with open(path, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    word, translated_word = parts[0], parts[1]
                    data_db[word] = translated_word

        for word in words_classified:
            if data_db.__contains__(word[0]) or data_db.__contains__(word[1]):

        return data_db

# print(Repository.products)
