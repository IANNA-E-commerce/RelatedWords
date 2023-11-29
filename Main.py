import scripts.SuggestProducts as Suggest
from scripts.SpellingChecker import SpellingChecker
from scripts.SuggestProducts import SuggestProducts

class Main:
    input_info = ["açõEs açores caÇhorão vou", "pt_BR"]
    print("input_info 1: ", input_info)
    phrase_treated = SpellingChecker.custom_spell_check(input_info)
    print("phrase_treated: ", phrase_treated)
    print("input_info[1]: ", input_info[1])
    products = SuggestProducts.main([phrase_treated, input_info[1]])
    print("products: ", products)

    SuggestProducts.main(["bomba ip21", "es_MX"])
