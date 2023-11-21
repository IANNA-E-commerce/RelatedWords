# python -m spacy download en_core_web_md
# python -m spacy download pt_core_news_md
# python -m spacy download es_core_news_md
import array
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
        path = os.path.join('../dict', 'data_db.csv')
        try:
            with open(path, "r", newline='') as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 2:
                        parts[0] = parts[0].replace('"', "")
                        parts[1] = parts[1].replace('"', "").lstrip()
                        translated_word, id_product = parts[1], parts[0]
                        data_db[translated_word] = id_product

            product_attribute = []
            product_name = []

            for data in data_db.items():
                for item in words_classified[0]:
                    if data[0].__contains__(item):
                        product_attribute.append(data)
                for item in words_classified[1]:
                    if data[0].__contains__(item):
                        product_name.append(data)

            # for

            # Extrair apenas os nomes dos produtos para facilitar a comparação
            product_name_names = list(set(item for item in product_name))
            product_attribute_names = list(set(item for item in product_attribute))

            common_product_names = []
            different_products_names = product_attribute_names

            # Encontrar a  dos conjuntos
            for elem in product_attribute_names:
                if elem in product_name_names:
                    common_product_names.append(elem)
                    product_name_names.remove(elem)
                    different_products_names.remove(elem)

            different_products_names.append(product_name_names)
            common_product_names.append(different_products_names)

            # Exibir os itens comuns
            common_product_names_list = list(common_product_names)
            print("common_product_names_list - ", common_product_names_list)

            # print("product_name - ", product_name)
            # print("product_attribute - ", product_attribute)
            print("different_products_names - ", different_products_names)

        except FileNotFoundError:
            print(f"O arquivo '{path}' não foi encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")


SuggestProducts.search_db([["aberto", "tensão"], ["motor"]])
