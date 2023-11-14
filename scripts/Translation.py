from textblob import TextBlob


class Translation:

    def find_language(word):
        blob_word = TextBlob(word)
        return blob_word.detect_language()


    def translation_words_from_bd():
