import enchant

class TreatDictionaries:
    custom_corrections_file = []

    def define_language(language):
        global custom_corrections_file
        enchant_dict = None
        if language == "en_US":
            custom_corrections_file = "../dict/dictionary_english.txt"
            enchant_dict = enchant.Dict('en_US')
        elif language == "es_MX":
            custom_corrections_file = "../dict/dictionary_spanish.txt"
            enchant_dict = enchant.Dict('es_MX')
        else:
            custom_corrections_file = "../dict/dictionary_portuguese.txt"
            enchant_dict = enchant.Dict('pt_BR')
        return list([enchant_dict, TreatDictionaries.open_file_custom_corrections()])

    # Open and modify the file with custom corrections
    def open_file_custom_corrections():
        custom_corrections = {}
        with open(custom_corrections_file, "r") as file:
            for line in file:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    incorrect_word, correct_word = parts[0], parts[1]
                    custom_corrections[incorrect_word] = correct_word

        return custom_corrections
