# python -m spacy download en_core_web_md
# python -m spacy download pt_core_news_md
# python -m spacy download es_core_news_md
import os

import spacy

from scripts.TreatData import TreatData

# nltk.download('punkt')
# nltk.download('stopwords')

# Carrega o modelo em português
nlp_pt = spacy.load('pt_core_news_md')
nlp_es = spacy.load('es_core_news_md')
nlp_en = spacy.load('en_core_web_md')

# Cria dois objetos Doc
# doc1 = TreatData.clean_and_refactoring_text("açAí caiu morrera chutou abraçará colhendo abrasivo mouse abraçar-te-ia",
#                                             "pt_BR", nlp_pt)
# doc2 = clean_text(Repository.products[1][0])
# print(type(doc1))
# print(doc2)

# Calcula a similaridade entre os dois objetos Doc
# similarity = doc1.similarity(doc2)
# print(Repository.products[0][0] + " ", Repository.products[1][0] + " ", similarity)
class SuggestProducts:

    def main(matrix):
        treat_data = TreatData.clean_and_refactoring_text(matrix[0], matrix[1], nlp_pt)
        print("treat_data: ", treat_data)
        words_classified = SuggestProducts.classifier_words(treat_data)
        print("words_classified: ", words_classified)
        products_ranked = SuggestProducts.products_ranked(words_classified)
        return products_ranked

    def classifier_words(array_words):
        name_products_weg = \
            ["motor", "bomba", "turbina", "partida", "suave", "subestação", "sensor"
             "câmera", "controle", "gerador", "hidrogerador", "wemob", "inversor",
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
        return words_classified

    def search_db():
        data_db = {}
        path = os.path.join('dict', 'data_db.csv')
        try:
            with open(path, "r", newline='') as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 2:
                        parts[0] = parts[0].replace('"', "")
                        parts[1] = parts[1].replace('"', "").lstrip()
                        translated_word, id_product = parts[1], parts[0]
                        data_db[translated_word] = id_product

            return data_db
        except FileNotFoundError:
            print(f"O arquivo '{path}' não foi encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def products_ranked(words_classified):
        data_db = SuggestProducts.search_db()
        products_db = []
        products_similarity = []
        products_not_duplicated = []

        for data in data_db.items():
            for item in words_classified[0]:
                if data[0].__contains__(item):
                    products_db.append(data)
                elif nlp_pt(item).similarity(nlp_pt(data[0])) > 0.57:
                    if not products_similarity.__contains__(data[0]):
                        products_similarity.append(data)
                print(nlp_pt(item), nlp_pt(data[0]))

        print("b.f products_db: ", products_db)

        for data in data_db.items():
            for item in words_classified[1]:
                if data[0].__contains__(item):
                    products_db.append(data)
                elif nlp_pt(item).similarity(nlp_pt(data[0])) > 0.57:
                    if not products_similarity.__contains__(data[0]):
                        products_similarity.append(data)

        print("products_db: ", products_db)

        products_db += products_similarity
        for elem in products_db:
            if elem not in products_not_duplicated:
                products_not_duplicated.append(elem)

        return products_not_duplicated


print(SuggestProducts.main(["controle whome", "pt_BR"]))
