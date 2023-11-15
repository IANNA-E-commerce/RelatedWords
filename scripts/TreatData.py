import re

from nltk.corpus import stopwords
from spellchecker import SpellChecker
from deep_translator import GoogleTranslator


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

    def refactoring_data_db(matrix):
        matrix_translated = []
        try:
            for array in matrix:
                array_translated = []
                for sentence in array:
                    cleaned_word = re.sub(r"[()]", "", sentence)
                    text_row = ""
                    words = cleaned_word.split(" ")
                    for word in words:
                        text_row = f"{text_row} {TreatData.translation_words_db(word)}"
                    text_row = text_row.strip()
                    array_translated.append(text_row)
                matrix_translated.append(array_translated)
        except Exception as e:
            print("Exceção:", e)
        return matrix_translated

    def translation_words_db(word):
        spell = SpellChecker(language="pt")
        words_dont_translate \
            = ["whome", "interno", "francis", "-", "well", "painél", "gc", "gk", "go", "classifieredge", "iot",
               "relé", "relê", "inversor", "gd", "+", "weg", "home", "dimmer", "interruptor", "weghome",
               "software", "wegnology", "lackthane", "primer", "gnp", "pumpw", "diluente"]
        word_formatted = word.lower()
        if not words_dont_translate.__contains__(word_formatted):
            if not spell.unknown(word_formatted):
                try:
                    return GoogleTranslator(source="auto", target="pt").translate(word_formatted)
                except Exception:
                    return word_formatted
        return word_formatted
