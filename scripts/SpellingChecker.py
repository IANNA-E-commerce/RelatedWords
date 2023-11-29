from scripts.TreatData import TreatData
from scripts.TreatDictionaries import TreatDictionaries

class SpellingChecker():

    enchant_dict = None
    chosen_language = ""
    custom_corrections = []
    index_word = 1
    corrected_words = []

    # Find the misspelled words
    def find_errors(text):
        misspelled = []
        for word in text:
            if not SpellingChecker.enchant_dict.check(word):
                misspelled.append(word)
        return misspelled
    
    
    # Separate a word in two parts
    def separate_word(word, index):
        return [word[:index], word[index:]]
    
    
    def return_custom_corrections(word):
        if word in SpellingChecker.custom_corrections:
            return SpellingChecker.custom_corrections[word]
    
    
    def return_enchant_corrections(word):
        corrected_word = word
        if len(SpellingChecker.find_errors([word])) == 0:
            return word
        if len(SpellingChecker.enchant_dict.suggest(word)) > 0:
            corrected_word = SpellingChecker.enchant_dict.suggest(word)[0]
        if corrected_word != word:
            return corrected_word
    
    
    def try_correction(words):
        if SpellingChecker.SpellingChecker.return_custom_corrections(words[0]) and SpellingChecker.return_custom_corrections(words[1]):
            SpellingChecker.corrected_words.extend([SpellingChecker.return_custom_corrections(words[0]), SpellingChecker.return_custom_corrections(words[1])])
            return True
        elif SpellingChecker.return_custom_corrections(words[0]) and SpellingChecker.return_enchant_corrections(words[1]):
            SpellingChecker.corrected_words.extend([SpellingChecker.return_custom_corrections(words[0]), SpellingChecker.return_enchant_corrections(words[1])])
            return True
        elif SpellingChecker.return_enchant_corrections(words[0]) and SpellingChecker.return_custom_corrections(words[1]):
            SpellingChecker.corrected_words.extend([SpellingChecker.return_enchant_corrections(words[0]), SpellingChecker.return_custom_corrections(words[1])])
            return True
        elif SpellingChecker.return_enchant_corrections(words[0]) and SpellingChecker.return_enchant_corrections(words[1]):
            SpellingChecker.corrected_words.extend([SpellingChecker.return_enchant_corrections(words[0]), SpellingChecker.return_enchant_corrections(words[1])])
            return True
        return False
    
    
    def find_words(word):
        corrected_words = []
    
        for index in range(len(word)):
            separate_words = SpellingChecker.separate_word(word, (index + 1))
            errors = SpellingChecker.find_errors(separate_words)
            if len(errors) == 0:
                corrected_words.extend(separate_words)
                return True
            elif SpellingChecker.try_correction(separate_words):
                return True
    
        print("Nenhuma correção encontrada.")
        return False
    
    
    def verification_correction(array_info):
    
        results = TreatDictionaries.define_language(array_info[1])
        SpellingChecker.enchant_dict = results[0]
        array = TreatData.clean_text(array_info[0])
        wrong_words = SpellingChecker.find_errors(array)
    
        if SpellingChecker.index_word == -1:
            return SpellingChecker.corrected_words
    
        for word in array:
            if word in wrong_words:
                # Give preference for words in our dictionary
                if not SpellingChecker.return_custom_corrections(word):
                    # Uses Enchant to suggest a correction
                    if not SpellingChecker.return_enchant_corrections(word):
                        if not SpellingChecker.find_words(word):
                            print("Não descobriu uma palavra")
                    else:
                        SpellingChecker.corrected_words.append(SpellingChecker.return_enchant_corrections(word))
                else:
                    SpellingChecker.corrected_words.append(SpellingChecker.return_custom_corrections(word))
            else:
                SpellingChecker.corrected_words.append(word)
    
    
    def custom_spell_check(array_info):
        SpellingChecker.verification_correction(array_info)
        corrected_text = ""
        # Returns the text with the elements removed before
        if SpellingChecker.corrected_words is not None:
            for word in SpellingChecker.corrected_words:
                if word.isnumeric() or word.isalpha():
                    corrected_text += " " + str(word)
                else:
                    corrected_text += word

        return corrected_text