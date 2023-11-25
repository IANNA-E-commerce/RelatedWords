import re

import spacy
from nltk.corpus import stopwords
from spellchecker import SpellChecker
from deep_translator import GoogleTranslator
from unidecode import unidecode


class TreatData:

    words_dont_translate = ["whome", "interno", "francis", "-", "well", "painél", "gc", "gk", "go", "classifieredge", "iot",
           "relé", "relê", "inversor", "gd", "+", "weg", "home", "dimmer", "interruptor", "weghome",
           "software", "wegnology", "lackthane", "primer", "gnp", "pumpw", "diluente", "wpump"]

    # Returns a string array
    def clean_text(text):
        text_to_clean = text.lower()
        text_to_clean = unidecode(text_to_clean)
        # string = []:?
        string = re.sub("[^a-zA-Z0-9]+", " ", text_to_clean).rstrip().split(" ")
        return string

    def clean_and_refactoring_text(text, lan):
        text_cleaned = TreatData.clean_text(text)
        print(lan)
        words = []
        add_words = []

        if lan == "pt_BR":
            nlp_pt = spacy.load('pt_core_news_md')
            lan = "portuguese"
            add_words.extend(["não", "sem", "com", "entre", "sobre", "sob", "embaixo", "cima"])
            nlp = nlp_pt
        elif lan == "en_US":
            nlp_en = spacy.load('en_core_web_md')
            lan = "english"
            add_words.extend(
                ["not", "no", "non", "nor", "without", "with", "between", "above", "under", "on", "in", "at"])
            nlp = nlp_en
        else:
            nlp_es = spacy.load('es_core_news_md')
            lan = "spanish"
            add_words.extend(["no", "sin", "con", "entre", "sobre", "bajo", "en", "debajo", "abajo", "arriba"])
            nlp = nlp_es

        stop_words = set(stopwords.words(lan))

        for word in text_cleaned:
            if word in TreatData.words_dont_translate:
                words.append(word)
            else:
                if word in add_words or word not in stop_words:
                    lemma = nlp(word)[0].lemma_
                    words.append(lemma)
        return words

    def refactoring_data_db(matrix):
        matrix_translated = []
        try:
            for array in matrix:
                array_translated = []
                cleaned_word = re.sub(r"[()]", "", array[0])
                text_row = f"{array[1]}, "
                words = cleaned_word.split(" ")
                for word in words:
                    text_row += f" {TreatData.translation_words(word)}"
                text_row = text_row.strip()
                array_translated.append(text_row)
                matrix_translated.append(array_translated)
        except Exception as e:
            print("Exceção:", e)
        return matrix_translated

    def refactoring_data_input(array):
        # [INPUT, ORIGINAL_LANGUAGE]
        sentence_array = array[0].split(" ")
        sentence_translated_array = []
        for word in sentence_array:
            sentence_translated_array.append(TreatData.translation_words(word))
        return sentence_translated_array

    def translation_words(word, lang):
        try:
            if lang == "pt_BR":
                spell = SpellChecker(language="pt")
            elif lang == "en_US":
                spell = SpellChecker(language="en")
            else:
                spell = SpellChecker(language="es")

            word_formatted = word.lower()
            if not TreatData.words_dont_translate.__contains__(word_formatted):
                if not spell.unknown(word_formatted):
                    try:
                        return GoogleTranslator(source="auto", target="pt").translate(word_formatted)
                    except Exception:
                        return word_formatted
            return word_formatted
        except Exception:
            print("Error in Treat Data - translation_words: ", Exception)
            return word

