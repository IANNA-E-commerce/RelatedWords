import enchant

from scripts.TreatData import TreatData
from scripts.TreatDictionaries import TreatDictionaries

enchant_dict = None
chosen_language = ""
custom_corrections = []
index_word = 1
corrected_words = []


# Find the misspelled words
def find_errors(text):
    global enchant_dict
    misspelled = []
    for word in text:
        if not enchant_dict.check(word):
            misspelled.append(word)
    return misspelled


# Separate a word in two parts
def separate_word(word, index):
    return [word[:index], word[index:]]


def return_custom_corrections(word):
    if word in custom_corrections:
        return custom_corrections[word]


def return_enchant_corrections(word):
    corrected_word = word
    if len(find_errors([word])) == 0:
        return word
    if len(enchant_dict.suggest(word)) > 0:
        corrected_word = enchant_dict.suggest(word)[0]
    if corrected_word != word:
        return corrected_word


def try_correction(words):
    if return_custom_corrections(words[0]) and return_custom_corrections(words[1]):
        corrected_words.extend([return_custom_corrections(words[0]), return_custom_corrections(words[1])])
        return True
    elif return_custom_corrections(words[0]) and return_enchant_corrections(words[1]):
        corrected_words.extend([return_custom_corrections(words[0]), return_enchant_corrections(words[1])])
        return True
    elif return_enchant_corrections(words[0]) and return_custom_corrections(words[1]):
        corrected_words.extend([return_enchant_corrections(words[0]), return_custom_corrections(words[1])])
        return True
    elif return_enchant_corrections(words[0]) and return_enchant_corrections(words[1]):
        corrected_words.extend([return_enchant_corrections(words[0]), return_enchant_corrections(words[1])])
        return True
    return False


def find_words(word):
    corrected_words = []

    for index in range(len(word)):
        separate_words = separate_word(word, (index + 1))
        errors = find_errors(separate_words)
        if len(errors) == 0:
            corrected_words.extend(separate_words)
            return True
        elif try_correction(separate_words):
            return True

    print("Nenhuma correção encontrada.")
    return False


def verification_correction(array_info):
    global index_word
    global enchant_dict

    results = TreatDictionaries.define_language(array_info[1])
    enchant_dict = results[0]
    custom_corrections = results[1]
    array = TreatData.clean_text(array_info[0])
    wrong_words = find_errors(array)

    if index_word == -1:
        return corrected_words

    for word in array:
        if word in wrong_words:
            # Give preference for words in our dictionary
            if not return_custom_corrections(word):
                # Uses Enchant to suggest a correction
                if not return_enchant_corrections(word):
                    if not find_words(word):
                        print("Não descobriu uma palavra")
                else:
                    corrected_words.append(return_enchant_corrections(word))
            else:
                corrected_words.append(return_custom_corrections(word))
        else:
            corrected_words.append(word)


def custom_spell_check(array_info):
    verification_correction(array_info)

    corrected_text = ""
    # Returns the text with the elements removed before
    if corrected_words is not None:
        for word in corrected_words:
            if word.isnumeric() or word.isalpha():
                corrected_text += " " + str(word)
            else:
                corrected_text += word

    print(corrected_text)
    return corrected_text


input_info = ["açõEs açores caÇhorão", "pt_BR"]
custom_spell_check(input_info)
