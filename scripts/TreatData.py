import re

import spacy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob


class TreatData:
    # Returns a string array
    def clean_text(text):
        text = text.lower()
        string = re.findall(r"\b\w+\b|[,.)('\"\[\];><:\\/@!#$%¨&*_+=]", text, re.UNICODE)
        return string

    def clean_and_refactoring_text(text, lan, nlp):
        text = TreatData.clean_text(text)
        words = []
        add_words = []

        if lan == "pt_BR":
            lan = "portuguese"
            add_words.extend(["não", "sem", "com", "entre", "sobre", "sob", "embaixo", "cima"])
        elif lan == "en_US":
            lan = "english"
            add_words.extend(
                ["not", "no", "non", "nor", "without", "with", "between", "above", "under", "on", "in", "at"])
        else:
            lan = "spanish"
            add_words.extend(["no", "sin", "con", "entre", "sobre", "bajo", "en", "debajo", "abajo", "arriba"])

        stop_words = set(stopwords.words(lan))

        for word in text:
            if word in add_words or word not in stop_words:
                lemma = nlp(word)[0].lemma_
                words.append(lemma)
        return words

    def refactoring_data_bd(matrix):
        nlp = spacy.load('pt_core_news_md')
        matrix_translated = []
        for array in matrix:
            array_translated = []
            for word in array:
                text_row = ""
                lemma = nlp(word)
                for token in lemma:
                    print(token.lemma_)
                    blob = TextBlob(token.lemma_)
                    # if blob.detect_language() != "en":
                    blob.translate("pt")
                    text_row += token.lemma_ + " "
                text_row = text_row.rstrip()
                array_translated.append(text_row)
            matrix_translated.append(array_translated)
        print(matrix_translated)


TreatData.refactoring_data_bd([["motor mining", "agro"], ["ClassifierEdge no-code", "energias"]])
