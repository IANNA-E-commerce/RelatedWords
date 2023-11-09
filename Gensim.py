# import gensim.downloader as api
# wv = api.load('word2vec-google-news-300')
# # wv = api.load("news_pt")
#
# pairs = [
#     'gear',
#     'reducers',
#     'engines',
#     'motors',
#     'panels',
#     'paints',
#     'pumps',
#     'energy',
#     'mobility',
#     'software',
#     'agro',
#     'cameras',
#     'controls',
#     'sensors',
#     'relays',
#     'switches',
#     'plugs'
# ]
#
# maxSimilarity = 0
# similarities = []
# for w1 in pairs:
#     print(w1)
#     for w2 in pairs:
#         if w1 is not w2:
#             if wv.similarity(w1, w2) > maxSimilarity:
#                 maxSimilarity = wv.similarity(w1, w2)
#             similarities.append([w1, w2, wv.similarity(w1, w2)])
#             print('%r\t%r\t%.2f' % (w1, w2, wv.similarity(w1, w2)))
#
# print(maxSimilarity)
# print(similarities)
from bert_serving.client import BertClient
from scipy import spatial

# Conecte-se ao serviço Bert-as-Service
bc = BertClient()

# Exemplo de palavras que você deseja comparar
word1 = "casa"
word2 = "hogar"

# Obtenha as incorporações de BERT para as palavras
embeddings1 = bc.encode([word1])
embeddings2 = bc.encode([word2])

# Calcule a similaridade entre as palavras
similarity = 1 - spatial.distance.cosine(embeddings1, embeddings2)

print(f"Similaridade entre '{word1}' e '{word2}': {similarity}")
